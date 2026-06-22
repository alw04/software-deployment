from lib.build_systems.binary import BinaryPackage


class Tcoffee(BinaryPackage):
    """T-Coffee is a multiple sequence alignment package."""

    homepage = "https://tcoffee.crg.eu/"
    url = (
        "https://s3.eu-central-1.amazonaws.com/tcoffee-packages/Archives/T-COFFEE_distribution_Version_{version}.tar.gz"
    )

    versions = [
        "13.46.0.919e8c6b",
    ]

    def install(self):
        self.install_binary(self.build_dir / "bin" / "linux" / "t_coffee")
