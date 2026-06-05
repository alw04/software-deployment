from lib.build_systems.autotools import AutotoolsPackage


class Zlib(AutotoolsPackage):
    """A free, general-purpose, legally unencumbered lossless
    data-compression library.
    """

    homepage = "https://zlib.net"
    url = "http://zlib.net/fossils/zlib-{version}.tar.gz"

    versions = [
        "1.3.1",
    ]
