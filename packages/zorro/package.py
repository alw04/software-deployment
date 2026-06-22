from lib.build_systems.binary import BinaryPackage


class Zorro(BinaryPackage):
    """ZORRO is a probabilistic masking program that assigns
    confidence scores to each column in a multiple seqeunce alignment.
    These scores can then be used to account for alignment accuracy
    in phylogenetic inference pipelines.
    """

    homepage = "https://sourceforge.net/projects/probmask/"
    url = "https://sourceforge.net/projects/probmask/files/zorro_linux_x86_64"

    versions = [
        "latest",
    ]

    phases = (
        "download",
        "install",
    )

    def install(self):
        self.install_binary(self.download_file)
