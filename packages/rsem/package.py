from lib.build_systems.makefile import MakefilePackage


class Rsem(MakefilePackage):
    """RSEM is a software package for estimating gene and isoform expression
    levels from RNA-Seq data."""

    homepage = "https://deweylab.github.io/RSEM/"
    url = "https://github.com/deweylab/RSEM/archive/v{version}.tar.gz"

    versions = [
        "1.3.3",
    ]

    def install_args(self):
        return [
            f"prefix={self.prefix}",
        ]
