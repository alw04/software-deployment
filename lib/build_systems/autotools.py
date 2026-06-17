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
                self.prepend_env("CPPFLAGS", f"-I{include}")

            for libdir in ("lib", "lib64"):
                lib_path = prefix / libdir
                if lib_path.is_dir():
                    self.prepend_env("LDFLAGS", f"-L{lib_path} -Wl,-rpath,{lib_path}")

                pkgconfig = lib_path / "pkgconfig"
                if pkgconfig.is_dir():
                    self.prepend_env("PKG_CONFIG_PATH", str(pkgconfig), sep=":")

        for lib_name in self.link_libs:
            self.prepend_env("LDLIBS", f"-l{lib_name}")

    def configure_args(self) -> list[str]:
        return []

    def make_args(self) -> list[str]:
        return []

    def install_args(self) -> list[str]:
        return []

    def configure(self):
        configure = self.build_dir / "configure"
        self.run_cmd(
            [str(configure), f"--prefix={self.prefix}", *self.configure_args()],
            cwd=self.build_dir,
        )

    def build(self):
        self.run_cmd(["make", f"-j{self.build_jobs}", *self.make_args()], cwd=self.build_dir)

    def install(self):
        self.run_cmd(["make", "install", *self.install_args()], cwd=self.build_dir)
