from pathlib import Path

from lib.dependency import Dependency
from lib.package import Package


class CMakePackage(Package):
    abstract = True

    phases = (
        "download",
        "extract",
        "configure",
        "build",
        "install",
    )

    depends_on = [
        Dependency("cmake", type="build"),
    ]

    def apply_link_env(self):
        for dep in self.link_dependencies:
            prefix = Path(dep.prefix)

            self.prepend_env("CMAKE_PREFIX_PATH", str(prefix), sep=":")

            include = prefix / "include"
            if include.is_dir():
                self.prepend_env("CMAKE_INCLUDE_PATH", str(include), sep=":")

            for libdir in ("lib", "lib64"):
                lib = prefix / libdir

                if lib.is_dir():
                    self.prepend_env("CMAKE_LIBRARY_PATH", str(lib), sep=":")
                    self.prepend_env("LDFLAGS", f"-L{lib} -Wl,-rpath,{lib}")

                pkgconfig = lib / "pkgconfig"
                if pkgconfig.is_dir():
                    self.prepend_env("PKG_CONFIG_PATH", str(pkgconfig), sep=":")

        for lib_name in self.link_libs:
            self.append_env("LDFLAGS", f"-l{lib_name}")

    def extra_module_paths(self):
        return {
            "CMAKE_PREFIX_PATH": [self.prefix],
        }

    def cmake_args(self) -> list[str]:
        return []

    def configure(self):
        self.run_cmd(
            [
                "cmake",
                "-S",
                str(self.build_dir),
                "-B",
                str(self.build_path / "build"),
                f"-DCMAKE_INSTALL_PREFIX={self.prefix}",
                *self.cmake_args(),
            ],
        )

    def build(self):
        self.run_cmd(["cmake", "--build", str(self.build_path / "build"), "--parallel", str(self.build_jobs)])

    def install(self):
        self.run_cmd(["cmake", "--install", str(self.build_path / "build")])
