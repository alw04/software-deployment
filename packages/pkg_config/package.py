from lib.build_systems.autotools import AutotoolsPackage


class PkgConfig(AutotoolsPackage):
    """pkg-config is a helper tool used when compiling applications
    and libraries"""

    homepage = "https://www.freedesktop.org/wiki/Software/pkg-config/"
    url = "https://pkgconfig.freedesktop.org/releases/pkg-config-{version}.tar.gz"

    versions = [
        "0.29.1",
    ]
