from lib.build_systems.binary import BinaryPackage


class Go(BinaryPackage):
    """The golang compiler and build environment"""

    homepage = "https://go.dev"
    url = "https://go.dev/dl/go{version}.linux-amd64.tar.gz"

    versions = [
        "1.25.1",
    ]
