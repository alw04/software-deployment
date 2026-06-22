from lib.build_systems.binary import BinaryPackage


class Uclust(BinaryPackage):
    """The UCLUST algorithm divides a set of sequences into clusters.
    UCLUST is not designed for OTU clustering."""

    homepage = "https://drive5.com/usearch/manual/uclust_algo.html"
    url = "https://drive5.com/uclust/uclustq{version}_i86linux64"

    versions = [
        "1.2.22",
    ]

    phases = (
        "download",
        "install",
    )

    def install(self):
        self.install_binary(self.download_file, name="uclust")
