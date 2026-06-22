from lib.build_systems.autotools import AutotoolsPackage


class Grep(AutotoolsPackage):
    """Grep searches one or more input files for lines containing a match to
    a specified pattern"""

    homepage = "https://www.gnu.org/software/grep/"
    url = "https://ftp.gnu.org/gnu/grep/grep-{version}.tar.xz"

    versions = [
        "3.11",
    ]
