from lib.build_systems.makefile import MakefilePackage
from lib.dependency import Dependency


class Kentutils(MakefilePackage):
    """Jim Kent command line bioinformatic utilities and libraries"""

    homepage = "https://genome.cse.ucsc.edu/"
    url = "https://hgdownload.cse.ucsc.edu/admin/exe/userApps.archive/userApps.v{version}.src.tgz"

    versions = [
        "478",
    ]

    depends_on = [
        Dependency("libpng", type="build"),
        Dependency("mariadb-c-client", type="build"),
        Dependency("util-linux-uuid"),
    ]

    def make_args(self):
        return [
            f"COPT=-I{self.dep('util-linux-uuid').prefix}/include",
        ]

    def install(self):
        self.install_directory(self.build_dir / "bin", self.prefix / "bin")
