from lib.build_systems.makefile import MakefilePackage


class Stringtie(MakefilePackage):
    """StringTie is a fast and highly efficient assembler of RNA-Seq alignments
    into potential transcripts."""

    homepage = "https://ccb.jhu.edu/software/stringtie"
    url = "https://github.com/gpertea/stringtie/archive/v{version}.tar.gz"

    versions = [
        "3.0.0",
    ]

    def install(self):
        self.install_binary(self.build_dir / "stringtie")
