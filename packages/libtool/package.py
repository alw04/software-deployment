from lib.build_systems.autotools import AutotoolsPackage


class Libtool(AutotoolsPackage):
    """libtool -- library building part of autotools."""

    homepage = "https://www.gnu.org/software/libtool/"
    url = "https://ftp.gnu.org/gnu/libtool/libtool-{version}.tar.gz"

    versions = [
        "2.4.7",
    ]
