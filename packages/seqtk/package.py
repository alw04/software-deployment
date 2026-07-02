from lib.build_systems.makefile import MakefilePackage


class Seqtk(MakefilePackage):
    """Toolkit for processing sequences in FASTA/Q formats."""

    homepage = "https://github.com/lh3/seqtk"
    url = "https://github.com/lh3/seqtk/archive/v{version}.tar.gz"

    versions = [
        "1.4",
    ]

    def install(self):
        self.install_binary(self.build_dir / "seqtk")
