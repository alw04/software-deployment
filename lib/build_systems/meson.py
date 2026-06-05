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

    def meson_args(self) -> list[str]:
        return []

    def configure(self):
        self.run_cmd(["meson", "setup", "build", f"--prefix={self.prefix}", *self.meson_args()], cwd=self.build_dir)

    def build(self):
        self.run_cmd(["meson", "compile", "-C", "build"], cwd=self.build_dir)

    def install(self):
        self.run_cmd(["meson", "install", "-C", "build"], cwd=self.build_dir)
