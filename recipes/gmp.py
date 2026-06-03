from lib.build_systems.autotools import AutotoolsPackage


class Gmp(AutotoolsPackage):
    """GMP is a free library for arbitrary precision arithmetic, operating
    on signed integers, rational numbers, and floating-point numbers."""

    homepage = "https://gmplib.org"
    url = "https://ftp.gnu.org/gnu/gmp/gmp-{version}.tar.xz"

    versions = [
        "6.2.1",
    ]
