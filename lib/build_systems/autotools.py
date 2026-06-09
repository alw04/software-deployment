from pathlib import Path

from lib.package import Package


class AutotoolsPackage(Package):
    abstract = True

    phases = (
        "download",
        "extract",
        "configure",
        "build",
        "install",
    )

    def apply_link_env(self):
        for dep in self.link_dependencies:
            prefix = Path(dep.prefix)

            include = prefix / "include"
            if include.is_dir():
                self.append_env("CPPFLAGS", f"-I{include}")

            for libdir in ("lib", "lib64"):
                lib = prefix / libdir
                if lib.is_dir():
                    self.append_env("LDFLAGS", f"-L{lib} -Wl,-rpath,{lib}")

                pkgconfig = lib / "pkgconfig"
                if pkgconfig.is_dir():
                    self.append_env("PKG_CONFIG_PATH", str(pkgconfig), sep=":")

    configure_directory = "."

    def configure_args(self) -> list[str]:
        return []

    def make_args(self) -> list[str]:
        return []

    def install_args(self) -> list[str]:
        return []

    def configure(self):
        self.run_cmd(
            ["./configure", f"--prefix={self.prefix}", *self.configure_args()],
            cwd=self.build_dir / self.configure_directory,
        )

    def build(self):
        self.run_cmd(
            ["make", f"-j{self.build_jobs()}", *self.make_args()], cwd=self.build_dir / self.configure_directory
        )

    def install(self):
        self.run_cmd(["make", "install", *self.install_args()], cwd=self.build_dir / self.configure_directory)
