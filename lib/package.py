import os
import shutil
import subprocess
import tarfile
import zipfile
from datetime import date
from inspect import getdoc
from pathlib import Path
from urllib.request import urlretrieve

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
    def name(self) -> str:
        return self.__class__.__name__.lower()

    @property
    def description(self) -> str:
        return getdoc(self) or ""

    homepage: str | None = None
    url: str | None = None

    versions: list[str] = []

    @classmethod
    def default_version(cls) -> str:
        if not cls.versions:
            raise ValueError(f"{cls.__name__} defines no versions")

        return cls.versions[0]

    depends_on: list[Dependency] = []
    conflicts: list[str] = []

    jobs: int | None = None

    phases: tuple = ()

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
        self.env: dict[str, str] = {}

    @property
    def prefix(self) -> Path:
        return self.ctx.config.apps / self.name / self.version

    @property
    def build_dir(self) -> Path:
        return self.ctx.config.builds / self.name / self.version

    @property
    def download_dir(self) -> Path:
        return self.ctx.config.downloads / self.name / self.version

    @property
    def modulefile(self) -> Path:
        return self.ctx.config.modulefiles / self.name / f"{self.version}.lua"

    def run_cmd(self, args: list[str], *, cwd=None):
        env = os.environ.copy()
        env.update(self.env)

        subprocess.run(args, check=True, cwd=cwd, env=env)

    def url_for_version(self, version: str) -> str:
        if self.url is None:
            raise NotImplementedError(f"{self.name} must define 'url' or override url_for_version()")

        return self.url.format(version=version)

    def build_jobs(self) -> int:
        if self.jobs is not None:
            return int(self.jobs)

        if self.ctx.config.jobs == "auto":
            return os.cpu_count() or 1

        return int(self.ctx.config.jobs)

    def download(self):
        url = self.url_for_version(self.version)

        filename = url.split("/")[-1]
        self.download_path = self.download_dir / filename

        if self.download_path.exists() and not self.ctx.args.force:
            return

        self.download_dir.mkdir(parents=True, exist_ok=True)

        tmp = self.download_path.with_suffix(self.download_path.suffix + ".part")

        if tmp.exists():
            tmp.unlink()

        urlretrieve(url, tmp)
        tmp.replace(self.download_path)

    def extract(self):
        if self.build_dir.exists() and any(self.build_dir.iterdir()):
            if not self.ctx.args.force:
                return

            shutil.rmtree(self.build_dir)

        self.build_dir.mkdir(parents=True, exist_ok=True)

        if zipfile.is_zipfile(self.download_path):
            with zipfile.ZipFile(self.download_path) as zf:
                zf.extractall(self.build_dir)

        elif tarfile.is_tarfile(self.download_path):
            with tarfile.open(self.download_path, "r:*") as tf:
                members = tf.getmembers()

                paths = [Path(m.name) for m in members if m.name]
                top_dirs = {p.parts[0] for p in paths if len(p.parts) > 1}

                strip = len(top_dirs) == 1
                strip_dir = next(iter(top_dirs)) if strip else None

                for m in members:
                    if not m.name or m.name == ".":
                        continue

                    if ".." in m.name:
                        continue

                    p = Path(m.name)

                    if strip and p.parts and p.parts[0] == strip_dir:
                        p = Path(*p.parts[1:])

                    if not p:
                        continue

                    m.name = str(p)
                    tf.extract(m, self.build_dir)

        else:
            raise ValueError(f"{self.name}: unknown archive format: {self.download_path}")

    def configure(self):
        raise NotImplementedError

    def build(self):
        raise NotImplementedError

    def install(self):
        raise NotImplementedError

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

    def extra_module_paths(self) -> list[tuple[str, Path]]:
        return []

    @property
    def module_paths(self) -> list[tuple[str, Path]]:
        paths = []

        for relpath, var in self.module_path_map.items():
            path = self.prefix / relpath

            if path.exists():
                paths.append((var, path))

        paths.extend(self.extra_module_paths())

        return paths

    def write_modulefile(self):
        template = self.ctx.jinja_env.get_template("lmod_modulefile.lua.j2")

        context = {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "homepage": self.homepage,
            "dependencies": self.dependencies,
            "conflicts": self.conflicts,
            "paths": self.module_paths,
            "generated_date": date.today().isoformat(),
        }

        content = template.render(**context)

        self.modulefile.parent.mkdir(parents=True, exist_ok=True)

        tmp = self.modulefile.with_suffix(".tmp")
        tmp.write_text(content)
        tmp.replace(self.modulefile)

    def run(self):
        for phase in self.phases:
            method = getattr(self, phase)
            # method = getattr(self, phase, None)
            # if method is None:
            #     raise ValueError(f"{self.name}: unknown phase '{phase}'")

            if phase in {"configure", "build", "install"}:
                marker = self.build_dir / f".{phase}"

                if marker.exists() and not self.ctx.args.force:
                    continue

                method()
                marker.touch()
            else:
                method()

        self.write_modulefile()
