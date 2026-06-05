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

    homepage: str | None = None
    url: str | None = None

    versions: list[str] = []

    @classmethod
    def default_version(cls) -> str:
        if not cls.versions:
            raise ValueError(f"{cls.__name__} defines no versions")

        return cls.versions[0]

    depends_on: list[Dependency] = []

    @classmethod
    def dependencies_spec(cls) -> list[Dependency]:
        deps = []

        for base in reversed(cls.__mro__):
            deps.extend(getattr(base, "depends_on", []))

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

    jobs: int | None = None

    phases: tuple = (
        "download",
        "extract",
        "configure",
        "build",
        "install",
    )

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

        subprocess.run(args, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=None, text=True, check=True)

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

        urllib.request.urlretrieve(url, tmp)
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

                    p = Path(m.name)

                    if strip and p.parts and p.parts[0] == strip_dir:
                        p = Path(*p.parts[1:])

                    if not p or str(p) in (".", ""):
                        continue

                    if p.is_absolute():
                        continue

                    if ".." in p.parts:
                        continue

                    if (m.issym() or m.islnk()) and m.linkname:
                        if Path(m.linkname).is_absolute():
                            continue

                    if not p:
                        continue

                    m.name = str(p)
                    tf.extract(m, self.build_dir)

        else:
            raise ValueError(f"{self.name}: unknown archive format: {self.download_path}")

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
            "description": self.description().replace("\n", "\n  "),
            "short_description": self.short_description(),
            "homepage": self.homepage,
            "dependencies": self.run_dependencies,
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
            print(f"{self.name}@{self.version} {phase}")
            # method = getattr(self, phase, None)
            # if method is None:
            #     raise ValueError(f"{self.name}: unknown phase '{phase}'")
            method()
            self.write_modulefile()
