from lib.build_systems.autotools import AutotoolsPackage


class Glibc(AutotoolsPackage):
    """The GNU C Library provides many of the low-level components used
    directly by programs written in the C or C++ languages."""

    homepage = "https://www.gnu.org/software/libc/"
    url = "https://ftp.gnu.org/gnu/libc/glibc-{version}.tar.gz"

    versions = [
        "2.39",
    ]
