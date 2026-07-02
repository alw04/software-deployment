from lib.dependency import Dependency
from lib.package import Package


class GoPackage(Package):
    abstract = True

    phases = (
        "download",
        "extract",
        "build",
        "install",
    )

    depends_on = [
        Dependency("go", type="build"),
    ]

    def apply_toolchain_env(self):
        gopath = self.build_dir / ".gopath"
        gomodcache = self.build_dir / ".gomodcache"
        gocache = self.build_dir / ".gocache"

        for d in (gopath, gomodcache, gocache):
            d.mkdir(parents=True, exist_ok=True)

        self.env.update(
            {
                "GOPATH": str(gopath),
                "GOMODCACHE": str(gomodcache),
                "GOCACHE": str(gocache),
            }
        )

    def build(self):
        self.run_cmd(["go", "build", "-o", self.name, str(self.build_dir)], cwd=self.build_dir)

    def install(self):
        self.install_binary(self.build_dir / self.name)
