from lib.build_systems.autotools import AutotoolsPackage


class AutoMake(AutotoolsPackage):
    """Automake -- make file builder part of autotools"""

    homepage = "https://www.gnu.org/software/automake/"
    url = "https://ftp.gnu.org/gnu/automake/automake-{version}.tar.gz"

    versions = [
        "1.16.5",
    ]
