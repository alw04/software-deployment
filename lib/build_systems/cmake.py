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
