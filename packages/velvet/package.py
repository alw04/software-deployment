from lib.build_systems.makefile import MakefilePackage


class Velvet(MakefilePackage):
    """Velvet is a de novo genomic assembler specially designed for short read
    sequencing technologies."""

    homepage = "https://github.com/dzerbino/velvet"
    url = "https://github.com/dzerbino/velvet/archive/refs/tags/v{version}.tar.gz"

    versions = [
        "1.2.10",
    ]

    def make_args(self):
        return [
            "OPENMP=1",
        ]

    def install(self):
        self.install_binary(self.build_dir / "velvetg")
        self.install_binary(self.build_dir / "velveth")
