from lib.build_systems.makefile import MakefilePackage
from lib.dependency import Dependency


class Usearch(MakefilePackage):
    """USEARCH is a unique sequence analysis tool with thousands of users
    world-wide."""

    homepage = "https://www.drive5.com/usearch/"
    url = "https://github.com/rcedgar/usearch12/archive/refs/tags/v{version}.tar.gz"

    versions = [
        "12.0-beta1",
    ]

    source_subdir = "src"

    depends_on = [
        Dependency("ccache", type="build"),
        Dependency("glibc"),
    ]

    def install(self):
        major = self.version.split(".")[0]
        self.install_binary(self.build_path / "bin" / f"usearch{major}", name="usearch")
