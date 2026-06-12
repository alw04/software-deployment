from __future__ import annotations

import inspect
import os
import re
import shutil
import subprocess
import tarfile
import urllib.request
import zipfile
from datetime import date
from pathlib import Path

from lib.dependency import Dependency
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

    @property
    def name(self) -> str:
        return self.__class__.__name__.lower()

    @classmethod
    def description(cls) -> str:
        return inspect.getdoc(cls) or ""

    @classmethod
    def short_description(cls) -> str:
        text = " ".join(cls.description().split())
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
            raise ValueError(f"{self.name}: unsupported version '{version}'.\nAvailable versions: {versions}")

        self.version = version
        self.ctx = ctx
        self.dependencies: dict[str, Package] = {}
        self.env: dict[str, str] = {
            "PATH": os.environ.get("PATH", ""),
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
    def build_dependencies(self) -> list[Package]:
        return [self.dependencies[dep.name] for dep in self.depends_on if "build" in dep.types]

    @property
    def link_dependencies(self) -> list[Package]:
        return [self.dependencies[dep.name] for dep in self.depends_on if "link" in dep.types]

    @property
    def run_dependencies(self) -> list[Package]:
        return [self.dependencies[dep.name] for dep in self.depends_on if "run" in dep.types]

    def dep(self, name: str) -> Package:
        return self.dependencies[name]

    conflicts: list[str] = []

    @property
    def root(self):
        return self.ctx.config.software_root

    @property
    def prefix(self) -> Path:
        return self.root / self.ctx.config.apps / self.name / self.version

    @property
    def build_path(self) -> Path:
        return self.root / self.ctx.config.builds / self.name / self.version

    @property
    def download_path(self) -> Path:
        return self.root / self.ctx.config.downloads / self.name / self.version

    @property
    def modulefile(self) -> Path:
        return self.root / self.ctx.config.modulefiles / self.name / f"{self.version}.lua"

    source_subdir: str = "."

    @property
    def build_dir(self) -> Path:
        return self.build_path / self.source_subdir

    def append_env(self, key: str, value: str, sep: str = " "):
        if self.env.get(key):
            self.env[key] += f"{sep}{value}"
        else:
            self.env[key] = value

    def apply_build_path(self):
        for dep in self.build_dependencies:
            bin_dir = Path(dep.prefix) / "bin"
            if bin_dir.is_dir():
                self.append_env("PATH", str(bin_dir), sep=":")

    link_libs: list[str] = []

    def apply_link_env(self):
        pass

    def run_cmd(self, args: list[str], *, cwd: str | Path | None = None, env: dict[str, str] | None = None):
        cmd_env = self.env | (env or {})

        cmd_str = " ".join(map(str, args))
        self.log.info("cmd=%s", cmd_str)
        self.log.debug("cwd=%s", cwd or os.getcwd())
        self.log.debug("env=%s", cmd_env)

        if self.ctx.debug:
            subprocess.run(
                args,
                cwd=cwd,
                env=cmd_env,
                check=True,
            )
        else:
            subprocess.run(
                args,
                cwd=cwd,
                env=cmd_env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                text=True,
                check=True,
            )

    def install_file(self, src: Path, dst: Path, mode: int | None = None):
        dst.parent.mkdir(parents=True, exist_ok=True)

        tmp = dst.with_name(dst.name + ".tmp")

        if tmp.exists():
            tmp.unlink()

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

        if tmp.exists() or tmp.is_symlink():
            tmp.unlink()

        tmp.symlink_to(target)

        tmp.replace(link)

    def install_directory(self, src: Path, dst: Path):
        tmp = dst.with_name(dst.name + ".tmp")

        if tmp.exists():
            shutil.rmtree(tmp)

        shutil.copytree(src, tmp)

        if dst.exists():
            shutil.rmtree(dst)

        tmp.replace(dst)

    def atomic_write(self, path: Path, content: str):
        tmp = path.with_name(path.name + ".tmp")
        tmp.write_text(content)
        tmp.replace(path)

    def url_for_version(self, version: str) -> str:
        if self.urls_by_version:
            if version in self.urls_by_version:
                return self.urls_by_version[version]

            raise ValueError(f"{self.name}: no download URL defined for version '{version}'")

        if self.url:
            return self.url.format(version=version)

        raise NotImplementedError(
            f"{self.name}: no download URL source defined (set 'url', 'urls_by_version', or override url_for_version()"
        )

    jobs: int | None = None

    @property
    def build_jobs(self) -> int:
        if self.jobs is not None:
            if self.jobs < 1:
                raise ValueError(f"{self.name}: jobs must be >= 1 (got {self.jobs})")
            return self.jobs

        return os.cpu_count() or 1

    phases: tuple = (
        "download",
        "extract",
        "configure",
        "build",
        "install",
    )

    def download(self):
        url = self.url_for_version(self.version)

        filename = url.split("/")[-1]
        self.download_file = self.download_path / filename

        if self.download_file.exists() and not self.ctx.args.force:
            return

        self.download_path.mkdir(parents=True, exist_ok=True)

        tmp = self.download_file.with_name(self.download_file.name + ".part")

        if tmp.exists():
            tmp.unlink()

        try:
            urllib.request.urlretrieve(url, tmp)
            tmp.replace(self.download_file)
        except Exception:
            if tmp.exists():
                tmp.unlink()
            raise

    def extract(self):
        if self.build_path.exists() and not self.ctx.args.force:
            return

        tmp_dir = self.build_path.with_suffix(".tmp")

        if tmp_dir.exists():
            shutil.rmtree(tmp_dir)

        if self.build_path.exists():
            shutil.rmtree(self.build_path)

        tmp_dir.mkdir(parents=True, exist_ok=True)

        try:
            if zipfile.is_zipfile(self.download_file):
                with zipfile.ZipFile(self.download_file) as zf:
                    zf.extractall(tmp_dir)

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
                raise ValueError(f"{self.name}: unknown archive format: {self.download_file}")

            tmp_dir.replace(self.build_path)

        except Exception:
            if tmp_dir.exists():
                shutil.rmtree(tmp_dir)
            raise

    def configure(self):
        pass

    def build(self):
        pass

    def install(self):
        raise NotImplementedError(f"{self.name}: install() not implemented")

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

    def extra_module_paths(self) -> dict[str, list[Path]]:
        return {}

    @property
    def module_paths(self) -> list[tuple[str, Path]]:
        paths = []

        for relpath, var in self.module_path_map.items():
            path = self.prefix / relpath
            if path.exists():
                paths.append((var, path))

        for base in reversed(self.__class__.__mro__):
            if "extra_module_paths" not in base.__dict__:
                continue

            extra = base.extra_module_paths(self)

            for var, path_list in extra.items():
                for path in path_list:
                    if not path.exists():
                        self.log.warning(f"skipping missing module path: {var} -> {path}")
                        continue

                    paths.append((var, path))

        return paths

    def module_env(self) -> dict[str, str]:
        return {}

    def write_modulefile(self):
        template = self.ctx.jinja_env.get_template("lmod_modulefile.lua.j2")

        context = {
            "name": self.name,
            "version": self.version,
            "description": self.description().replace("\n", "\n  "),
            "short_description": self.short_description(),
            "homepage": self.homepage,
            "dependencies": [dep.name for dep in self.run_dependencies],
            "conflicts": self.conflicts,
            "paths": self.module_paths,
            "env": self.module_env(),
            "generated_date": date.today().isoformat(),
        }

        content = template.render(**context)

        self.modulefile.parent.mkdir(parents=True, exist_ok=True)
        self.atomic_write(self.modulefile, content)

    def run(self):
        print(f"\n==> {self.name}@{self.version}")
        self.apply_build_path()
        self.apply_link_env()

        for phase in self.phases:
            print(phase)
            getattr(self, phase)()

        print("write_modulefile")
        self.write_modulefile()
