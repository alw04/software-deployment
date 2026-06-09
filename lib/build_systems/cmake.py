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

            self.append_env("CMAKE_PREFIX_PATH", str(prefix), sep=":")

            include = prefix / "include"
            if include.is_dir():
                self.append_env("CMAKE_INCLUDE_PATH", str(include), sep=":")

            for libdir in ("lib", "lib64"):
                lib = prefix / libdir

                if lib.is_dir():
                    self.append_env("CMAKE_LIBRARY_PATH", str(lib), sep=":")
                    self.append_env("LDFLAGS", f"-L{lib} -Wl,-rpath,{lib}")

                pkgconfig = lib / "pkgconfig"
                if pkgconfig.is_dir():
                    self.append_env("PKG_CONFIG_PATH", str(pkgconfig), sep=":")

    def cmake_args(self) -> list[str]:
        return []

    def configure(self):
        self.run_cmd(
            ["cmake", "-B", "build", f"-DCMAKE_INSTALL_PREFIX={self.prefix}", *self.cmake_args()], cwd=self.build_dir
        )

    def build(self):
        self.run_cmd(["cmake", "--build", "build", "--parallel", str(self.build_jobs())], cwd=self.build_dir)

    def install(self):
        self.run_cmd(["cmake", "--install", "build"], cwd=self.build_dir)
