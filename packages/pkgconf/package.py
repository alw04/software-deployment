from lib.build_systems.autotools import AutotoolsPackage


class Pkgconf(AutotoolsPackage):
    """pkgconf is a program which helps to configure compiler and linker
    flags for development frameworks. It is similar to pkg-config from
    freedesktop.org, providing additional functionality while also
    maintaining compatibility."""

    homepage = "http://pkgconf.org/"
    url = "https://distfiles.ariadne.space/pkgconf/pkgconf-{version}.tar.xz"

    versions = [
        "2.5.1",
    ]
