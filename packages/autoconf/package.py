from lib.build_systems.autotools import AutotoolsPackage


class Autoconf(AutotoolsPackage):
    """Autoconf -- system configuration part of autotools"""

    homepage = "https://www.gnu.org/software/autoconf/"
    url = "https://ftp.gnu.org/gnu/autoconf/autoconf-{version}.tar.gz"

    versions = [
        "2.72",
    ]
