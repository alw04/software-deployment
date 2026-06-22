from lib.build_systems.autotools import AutotoolsPackage


class Findutils(AutotoolsPackage):
    """The GNU Find Utilities are the basic directory searching
    utilities of the GNU operating system."""

    homepage = "https://www.gnu.org/software/findutils/"
    url = "https://ftp.gnu.org/gnu/findutils/findutils-{version}.tar.xz"

    versions = [
        "4.10.0",
    ]
