from lib.build_systems.makefile import MakefilePackage
from lib.dependency import Dependency


class Tabixpp(MakefilePackage):
    """This is a C++ wrapper around tabix project which abstracts
    some of the details of opening and jumping in tabix-indexed files."""

    homepage = "https://github.com/vcflib/tabixpp"
    url = "https://github.com/vcflib/tabixpp/archive/refs/tags/v{version}.tar.gz"

    versions = [
        "1.1.2",
    ]

    depends_on = [
        Dependency("htslib"),
    ]

    def configure(self):
        self.install_directory(self.dep("htslib").build_dir, self.build_dir / "htslib")
