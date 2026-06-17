from pathlib import Path

from lib.dependency import Dependency
from lib.package import Package


class MesonPackage(Package):
    abstract = True

    phases = (
        "download",
        "extract",
        "configure",
        "build",
        "install",
    )

    depends_on = [
        Dependency("meson", type="build"),
        Dependency("ninja", type="build"),
    ]

    def apply_link_env(self):
        for dep in self.link_dependencies:
            prefix = Path(dep.prefix)

            include = prefix / "include"
            if include.is_dir():
                self.prepend_env("CFLAGS", f"-I{include}")

            for libdir in ("lib", "lib64"):
                lib = prefix / libdir
                if lib.is_dir():
                    self.prepend_env("LDFLAGS", f"-L{lib} -Wl,-rpath,{lib}")

                pkgconfig = lib / "pkgconfig"
                if pkgconfig.is_dir():
                    self.prepend_env("PKG_CONFIG_PATH", str(pkgconfig), sep=":")

        for lib_name in self.link_libs:
            self.append_env("LDFLAGS", f"-l{lib_name}")

    def meson_args(self) -> list[str]:
        return []

    def configure(self):
        self.run_cmd(
            [
                "meson",
                "setup",
                str(self.build_path / "build"),
                str(self.build_dir),
                f"--prefix={self.prefix}",
                *self.meson_args(),
            ]
        )

    def build(self):
        self.run_cmd(["meson", "compile", "-C", str(self.build_path / "build")])

    def install(self):
        self.run_cmd(["meson", "install", "-C", str(self.build_path / "build")])
