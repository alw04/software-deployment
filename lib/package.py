import inspect
import os
import re
import shutil
import subprocess
import tarfile
import zipfile
from datetime import date
from pathlib import Path

import requests

from lib.dependency import Dependency
from lib.exceptions import UndeclaredDependencyError
from lib.pkgloader import register_package


class Package:
    abstract = True

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.__dict__.get("abstract", False):
            return

        register_package(cls)

    @property
    def log(self):
        return self.ctx.log

    homepage: str | None = None
    url: str | None = None
    urls_by_version: dict[str, str] | None = None
    versions: list[str] = []
    jobs: int | None = None

    @property
    def name(self) -> str:
        return self.__class__.__module__.rsplit(".", 1)[-1].lower()

    @classmethod
    def description(cls) -> str | None:
        return inspect.getdoc(cls)

    @classmethod
    def short_description(cls) -> str | None:
        desc = cls.description()
        if not desc:
            return None

        text = " ".join(desc.split())
        parts = re.split(r"\.\s+", text, maxsplit=1)
        return parts[0] + ("." if len(parts) > 1 else "")

    @classmethod
    def default_version(cls) -> str:
        if not cls.versions:
            raise ValueError(f"{cls.__name__} defines no versions")
        return cls.versions[0]

    def __init__(self, version, ctx):
        if version is None:
            version = self.default_version()

        if version not in self.versions:
            default = self.default_version()
            versions = ", ".join(f"{v} (default)" if v == default else v for v in self.versions)
            raise ValueError(f"{self.name}: unsupported version {version!r}.\nAvailable versions: {versions}")

        if self.jobs is not None and (not isinstance(self.jobs, int) or self.jobs < 1):
            raise ValueError(f"{self.name}: jobs must be an integer >= 1 (got {self.jobs!r})")

        self.version = version
        self.ctx = ctx
        self.dependencies: dict[str, Package] = {}
        self.env: dict[str, str] = {
            "PATH": "/usr/bin:/bin:/usr/local/bin",
        }

    depends_on: list[Dependency] = []

    @classmethod
    def dependencies_spec(cls) -> list[Dependency]:
        seen = set()
        deps = []

        for base in reversed(cls.__mro__):
            for dep in getattr(base, "depends_on", []):
                if dep.name in seen:
                    continue
                seen.add(dep.name)
                deps.append(dep)
        return deps

    @property
    def build_dependencies(self) -> list["Package"]:
        return [self.dependencies[dep.name] for dep in self.dependencies_spec() if "build" in dep.types]

    @property
    def link_dependencies(self) -> list["Package"]:
        return [self.dependencies[dep.name] for dep in self.dependencies_spec() if "link" in dep.types]

    @property
    def run_dependencies(self) -> list["Package"]:
        return [self.dependencies[dep.name] for dep in self.dependencies_spec() if "run" in dep.types]

    def dep(self, name: str) -> "Package":
        try:
            return self.dependencies[name]
        except KeyError:
            raise UndeclaredDependencyError(self.name, name) from None

    conflicts: list[str] = []

    @classmethod
    def conflicts_spec(cls) -> list[str]:
        seen = set()
        conflict_list = []

        for base in reversed(cls.__mro__):
            for conflict in getattr(base, "conflicts", []):
                if conflict in seen:
                    continue
                seen.add(conflict)
                conflict_list.append(conflict)
        return conflict_list

    @property
    def root(self) -> Path:
        return self.ctx.config.software_root

    @property
    def prefix(self) -> Path:
        return self.root / self.ctx.config.APPS_DIR / self.name / self.version

    @property
    def build_path(self) -> Path:
        return self.root / self.ctx.config.BUILDS_DIR / self.name / self.version

    @property
    def download_path(self) -> Path:
        return self.root / self.ctx.config.DOWNLOADS_DIR / self.name / self.version

    @property
    def modulefile(self) -> Path:
        return self.root / self.ctx.config.MODULEFILES_DIR / self.name / f"{self.version}.lua"

    source_subdir: str = "."

    @property
    def build_dir(self) -> Path:
        return self.build_path / self.source_subdir

    @property
    def build_jobs(self) -> int:
        return self.jobs or self.ctx.config.jobs

    def append_env(self, key: str, value: str, sep: str = " "):
        existing = self.env.get(key)
        self.env[key] = f"{existing}{sep}{value}" if existing else value

    def prepend_env(self, key: str, value: str, sep: str = " "):
        existing = self.env.get(key)
        self.env[key] = f"{value}{sep}{existing}" if existing else value

    def additonal_build_env(self) -> dict[str, list[Path]]:
        return {}

    def apply_build_env_from_deps(self):
        for dep in self.build_dependencies:
            bin_dir = dep.prefix / "bin"
            if bin_dir.is_dir():
                self.prepend_env("PATH", str(bin_dir), sep=":")

            for base in reversed(dep.__class__.__mro__):
                if "additional_build_env" not in base.__dict__:
                    continue

                additional = base.additional_build_env(dep)

                for var, paths in additional.items():
                    for path in paths:
                        if not path.exists():
                            self.log.warning(f"skipping missing env path: {var} -> {path}")
                            continue

                        self.prepend_env(var, str(path), sep=":")

    link_libs: list[str] = []

    def apply_toolchain_env(self):
        pass

    def run_cmd(
        self,
        args: list[str],
        *,
        cwd: str | Path | None = None,
        env: dict[str, str] | None = None,
        input: str | None = None,
    ):
        cmd_env = self.env | (env or {})

        term = self.ctx.term

        cmd_str = " ".join(map(str, args))

        # fmt: off
        self.log.debug(
            "Running command:\n"
            "  Command: %s\n"
            "  Directory: %s\n"
            "  Environment: %s",
            cmd_str,
            cwd or os.getcwd(),
            cmd_env,
        )
        # fmt: on

        if self.ctx.debug:
            subprocess.run(
                args,
                cwd=cwd,
                env=cmd_env,
                check=True,
                text=True,
                input=input,
            )
        else:
            try:
                subprocess.run(
                    args,
                    cwd=cwd,
                    env=cmd_env,
                    capture_output=True,
                    check=True,
                    text=True,
                    input=input,
                )
            except subprocess.CalledProcessError as e:

                def capture_tail(stream_name: str, stream_text: str) -> str:
                    TAIL_LINES = 50

                    if not stream_text:
                        return ""

                    lines = stream_text.strip().splitlines()
                    total_lines = len(lines)
                    truncated = total_lines > TAIL_LINES
                    selected_lines = lines[-TAIL_LINES:]

                    stat_label = f" {stream_name} ({min(TAIL_LINES, total_lines)}/{total_lines} lines) "
                    remaining_width = max(term.columns - len(stat_label) - 10, 10)

                    header = f" {term.dim}------{term.reset}{term.bold}{stat_label}{term.reset}{term.dim}{'-' * remaining_width}{term.reset}\n"
                    footer = f" {term.dim}{'-' * (term.columns - 4)}{term.reset}\n"

                    block_str = header
                    if truncated:
                        block_str += f"    {term.dim}[... older output truncated ...]{term.reset}\n"

                    for line in selected_lines:
                        block_str += f"    {line}\n"

                    block_str += footer
                    return block_str

                msg = (
                    f"Command failed with exit code {e.returncode}\n"
                    f"  {term.red}Command: {cmd_str}{term.reset}\n"
                    f"  {term.red}Directory: {cwd or os.getcwd()}{term.reset}\n"
                    f"  {term.red}Environment: {cmd_env}{term.reset}\n"
                )

                if e.stdout:
                    msg += "\n" + capture_tail("STDOUT", e.stdout)

                if e.stderr:
                    msg += "\n" + capture_tail("STDERR", e.stderr)

                self.log.error(msg)
                raise

    def install_file(self, src: Path, dst: Path, mode: int | None = None):
        dst.parent.mkdir(parents=True, exist_ok=True)

        tmp = dst.with_name(dst.name + ".tmp")
        tmp.unlink(missing_ok=True)

        shutil.copyfile(src, tmp)

        if mode is not None:
            tmp.chmod(mode)

        tmp.replace(dst)

    def install_binary(self, src: Path, name: str | None = None):
        dst = self.prefix / "bin" / (name or src.name)
        self.install_file(src, dst, mode=0o755)

    def install_symlink(self, target: str | Path, link: Path):
        link.parent.mkdir(parents=True, exist_ok=True)

        tmp = link.with_name(link.name + ".tmp")
        tmp.unlink(missing_ok=True)
        tmp.symlink_to(target)
        tmp.replace(link)

    def install_directory(self, src: Path, dst: Path):
        tmp = dst.with_name(dst.name + ".tmp")

        try:
            shutil.rmtree(tmp, ignore_errors=True)
            shutil.rmtree(dst, ignore_errors=True)

            shutil.copytree(src, tmp)
            tmp.replace(dst)

        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def atomic_write(self, path: Path, content: str):
        tmp = path.with_name(path.name + ".tmp")
        tmp.write_text(content)
        tmp.replace(path)

    def url_for_version(self, version: str) -> str:
        if self.urls_by_version:
            if version in self.urls_by_version:
                return self.urls_by_version[version]

            raise ValueError(f"{self.name}: no download URL defined for version {version!r}")

        if self.url:
            try:
                return self.url.format(version=version)
            except (ValueError, KeyError) as e:
                raise ValueError(f"{self.name}: invalid URL template {self.url!r}: {e}") from e

        raise NotImplementedError(
            f"{self.name}: no download URL source defined (set 'url', 'urls_by_version', or override url_for_version()"
        )

    phases: tuple = (
        "download",
        "extract",
        "configure",
        "build",
        "install",
    )

    download_headers: dict[str, str] = {
        # "User-Agent": (
        #     "Mozilla/5.0 (X11; Linux x86_64) "
        #     "AppleWebKit/537.36 (KHTML, like Gecko) "
        #     "Chrome/137.0.0.0 Safari/537.36"
        # )
    }

    def download(self):
        url = self.url_for_version(self.version)

        filename = url.split("/")[-1]
        self.download_file = self.download_path / filename
        self.download_path.mkdir(parents=True, exist_ok=True)

        if self.download_file.is_file() and not self.ctx.args.force:
            self.log.info("skipping download, file already exists: %s", self.download_file)
            return

        tmp = self.download_file.with_name(self.download_file.name + ".part")

        tmp.unlink(missing_ok=True)

        self.log.info("downloading file: %s -> %s", url, self.download_file)

        try:
            with requests.get(url, stream=True, headers=self.download_headers, timeout=60) as r:
                r.raise_for_status()

                chunk_size = 1024 * 1024

                with open(tmp, "wb") as f:
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        if chunk:
                            f.write(chunk)

            tmp.replace(self.download_file)
            self.log.info("download complete")

        finally:
            tmp.unlink(missing_ok=True)

    def extract(self):
        if self.build_path.exists() and not self.ctx.args.force:
            self.log.info("skipping extract, build directory already exists: %s", self.build_path)
            return

        tmp_dir = self.build_path.with_name(self.build_path.name + ".tmp")
        shutil.rmtree(tmp_dir, ignore_errors=True)
        tmp_dir.mkdir(parents=True, exist_ok=True)

        self.log.info("extracting archive: %s -> %s", self.download_file, self.build_path)

        try:
            if zipfile.is_zipfile(self.download_file):
                with zipfile.ZipFile(self.download_file) as zf:
                    namelist = zf.namelist()

                    paths = [Path(n) for n in namelist if n]
                    top_dirs = {p.parts[0] for p in paths if len(p.parts) > 1}

                    strip = len(top_dirs) == 1
                    strip_dir = next(iter(top_dirs)) if strip else None

                    for info in zf.infolist():
                        if not info.filename:
                            continue

                        p = Path(info.filename)

                        if strip and p.parts and p.parts[0] == strip_dir:
                            p = Path(*p.parts[1:])

                        if not p.parts or str(p) in (".", ""):
                            continue

                        if p.is_absolute():
                            continue

                        if ".." in p.parts:
                            continue

                        target = tmp_dir / p

                        if info.is_dir():
                            target.mkdir(parents=True, exist_ok=True)
                        else:
                            target.parent.mkdir(parents=True, exist_ok=True)
                            with zf.open(info) as src, target.open("wb") as dst:
                                shutil.copyfileobj(src, dst)

            elif tarfile.is_tarfile(self.download_file):
                with tarfile.open(self.download_file, "r:*") as tf:
                    members = tf.getmembers()

                    paths = [Path(m.name) for m in members if m.name]
                    top_dirs = {p.parts[0] for p in paths if len(p.parts) > 1}

                    strip = len(top_dirs) == 1
                    strip_dir = next(iter(top_dirs)) if strip else None

                    valid_members = []
                    for m in members:
                        if not m.name or m.name == ".":
                            continue

                        p = Path(m.name)

                        if strip and p.parts and p.parts[0] == strip_dir:
                            p = Path(*p.parts[1:])

                        if not p or str(p) in (".", ""):
                            continue

                        if p.is_absolute():
                            continue

                        if ".." in p.parts:
                            continue

                        if m.islnk() and m.linkname:
                            lp = Path(m.linkname)
                            if strip and lp.parts and lp.parts[0] == strip_dir:
                                lp = Path(*lp.parts[1:])
                            m.linkname = str(lp)

                        if (m.issym() or m.islnk()) and m.linkname:
                            if Path(m.linkname).is_absolute():
                                continue

                        m.name = str(p)
                        valid_members.append(m)

                    tf.extractall(tmp_dir, members=valid_members, filter="data")

            else:
                raise RuntimeError(
                    f"Unsupported archive format for {self.name}@{self.version}\n" f"File: {self.download_file}"
                )

            shutil.rmtree(self.build_path, ignore_errors=True)
            tmp_dir.replace(self.build_path)
            self.log.info("extract complete")

        finally:
            shutil.rmtree(tmp_dir, ignore_errors=True)

    def configure(self):
        pass

    def build(self):
        pass

    def install(self):
        raise NotImplementedError(f"{self.name}: install() not implemented")

    @property
    def is_installed(self) -> bool:
        return self.prefix.exists() and any(self.prefix.iterdir())

    module_path_map: dict[str, str] = {
        "bin": "PATH",
        "sbin": "PATH",
        "lib": "LD_LIBRARY_PATH",
        "lib64": "LD_LIBRARY_PATH",
        "include": "CPATH",
        "share/man": "MANPATH",
        "man": "MANPATH",
        "lib/pkgconfig": "PKG_CONFIG_PATH",
        "lib64/pkgconfig": "PKG_CONFIG_PATH",
        "share/pkgconfig": "PKG_CONFIG_PATH",
    }

    def modulefile_prepend_path(self) -> dict[str, list[Path]]:
        return {}

    @property
    def module_paths(self) -> list[tuple[str, Path]]:
        module_paths = []

        for relpath, var in self.module_path_map.items():
            full_path = self.prefix / relpath
            if full_path.exists():
                module_paths.append((var, full_path))

        for base in reversed(self.__class__.__mro__):
            if "modulefile_prepend_path" not in base.__dict__:
                continue

            prepend_paths = base.modulefile_prepend_path(self)

            for var, path_list in prepend_paths.items():
                for path in path_list:
                    if not path.exists():
                        self.log.warning(f"skipping missing module path: {var} -> {path}")
                        continue

                    module_paths.append((var, path))

        return module_paths

    def modulefile_setenv(self) -> dict[str, str]:
        return {}

    shell_functions: dict[str, str] = {}

    def format_shell_command(self, cmd: str) -> str:
        return cmd

    def render_shell_functions(self) -> dict[str, dict[str, str]]:
        out = {}

        for name, cmd in self.shell_functions.items():
            cmd = self.format_shell_command(cmd)

            out[name] = {
                "bash": f'{cmd} "$@"',
                "csh": f"{cmd} $*",
            }

        return out

    def write_modulefile(self):
        template = self.ctx.jinja_env.get_template("lmod_modulefile.lua.j2")

        desc = self.description()
        if desc:
            desc = desc.replace("\n", "\n  ")
        else:
            desc = "(none)"

        context = {
            "name": self.name,
            "version": self.version,
            "description": desc,
            "short_description": self.short_description(),
            "homepage": self.homepage or "(none)",
            "dependencies": [dep.name for dep in self.run_dependencies],
            "conflicts": self.conflicts_spec(),
            "paths": self.module_paths,
            "env": self.modulefile_setenv(),
            "shell_functions": self.render_shell_functions(),
            "generated_date": date.today().isoformat(),
        }

        content = template.render(**context)

        self.modulefile.parent.mkdir(parents=True, exist_ok=True)
        self.atomic_write(self.modulefile, content)

        self.log.info("wrote modulefile to %s", self.modulefile)

    def run(self):
        self.apply_build_env_from_deps()
        self.apply_toolchain_env()

        for phase in self.phases:
            print(phase)
            getattr(self, phase)()

        print("write_modulefile")
        self.write_modulefile()
