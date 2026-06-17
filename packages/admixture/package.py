from lib.build_systems.binary import BinaryPackage


class Admixture(BinaryPackage):
    """ADMIXTURE is a software tool for maximum likelihood estimation
    of individual ancestries from multilocus SNP genotype datasets.
    It uses the same statistical model as STRUCTURE but calculates
    estimates much more rapidly using a fast numerical optimization algorithm.
    """

    homepage = "https://dalexander.github.io/admixture/"
    url = "https://dalexander.github.io/admixture/binaries/admixture_linux-{version}.tar.gz"

    versions = [
        "1.4.0",
        "1.3.0",
    ]

    def install(self):
        source_dir = self.build_dir

        nested = source_dir / f"admixture_linux-{self.version}"
        if nested.is_dir():
            source_dir = nested

        self.install_binary(source_dir / "admixture")
