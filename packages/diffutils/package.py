from lib.build_systems.autotools import AutotoolsPackage


class Diffutils(AutotoolsPackage):
    """GNU Diffutils is a package of several programs related to finding
    differences between files."""

    homepage = "https://www.gnu.org/software/diffutils/"
    url = "https://ftp.gnu.org/gnu/diffutils/diffutils-{version}.tar.xz"

    versions = [
        "3.12",
    ]
