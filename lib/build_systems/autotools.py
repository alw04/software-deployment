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

    def setup_build_env(self):
        for dep in self.dependencies.values():
            prefix = Path(dep.prefix)

            include = prefix / "include"
            lib = prefix / "lib"
            lib64 = prefix / "lib64"
            pkgconfig = prefix / "lib" / "pkgconfig"
            pkgconfig64 = prefix / "lib64" / "pkgconfig"

            if include.is_dir():
                self.env["CPPFLAGS"] = self.env.get("CPPFLAGS", "") + f" -I{include}"

            if lib.is_dir():
                self.env["LDFLAGS"] = self.env.get("LDFLAGS", "") + f" -L{lib}"

            if lib64.is_dir():
                self.env["LDFLAGS"] = self.env.get("LDFLAGS", "") + f" -L{lib64}"

            pc_path = None
            if pkgconfig.is_dir():
                pc_path = pkgconfig
            elif pkgconfig64.is_dir():
                pc_path = pkgconfig64

            if pc_path:
                self.env["PKG_CONFIG_PATH"] = self.env.get("PKG_CONFIG_PATH", "") + f":{pc_path}"

    def configure_args(self) -> list[str]:
        return []

    def make_args(self) -> list[str]:
        return []

    def install_args(self) -> list[str]:
        return []

    def configure(self):
        self.run_cmd(["./configure", f"--prefix={self.prefix}", *self.configure_args()], cwd=self.build_dir)

    def build(self):
        self.run_cmd(["make", f"-j{self.build_jobs()}", *self.make_args()], cwd=self.build_dir)

    def install(self):
        self.run_cmd(["make", "install", *self.install_args()], cwd=self.build_dir)
