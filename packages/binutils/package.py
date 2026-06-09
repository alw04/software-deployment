from lib.build_systems.autotools import AutotoolsPackage


class Binutils(AutotoolsPackage):
    """GNU binutils, which contain the linker, assembler, objdump and others"""

    homepage = "https://www.gnu.org/software/binutils/"
    url = "https://ftp.gnu.org/gnu/binutils/binutils-{version}.tar.xz"

    versions = [
        "2.44",
    ]
