from lib.package import Package


class MakefilePackage(Package):
    abstract = True

    phases = (
        "download",
        "extract",
        "configure",
        "build",
        "install",
    )

    def make_args(self) -> list[str]:
        return []

    def install_args(self) -> list[str]:
        return []

    def build(self):
        self.run_cmd(["make", f"-j{self.build_jobs}", *self.make_args()], cwd=self.build_dir)

    def install(self):
        self.run_cmd(["make", "install", *self.install_args()], cwd=self.build_dir)
