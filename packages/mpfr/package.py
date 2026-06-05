from lib.build_systems.autotools import AutotoolsPackage


class Mpfr(AutotoolsPackage):
    """The MPFR library is a C library for multiple-precision
    floating-point computations with correct rounding."""

    homepage = "https://www.mpfr.org/"
    url = "https://ftp.gnu.org/gnu/mpfr/mpfr-{version}.tar.xz"

    versions = [
        "4.2.0",
    ]
