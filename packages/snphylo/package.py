from lib.package import Package


class Snphylo(Package):
    """A pipeline to generate a phylogenetic tree from huge SNP data"""

    homepage = "http://chibba.pgml.uga.edu/snphylo/"
    url = "https://github.com/thlee/SNPhylo/archive/refs/tags/{version}.tar.gz"

    versions = [
        "20180901",
    ]

    def install(self):
        self.install_binary(self.build_dir / "snphylo.sh", name="snphylo")
        self.install_file(self.build_dir / "snphylo.cfg", self.prefix / "bin" / "snphylo.cfg")
