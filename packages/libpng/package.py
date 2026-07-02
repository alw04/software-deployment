from lib.build_systems.cmake import CMakePackage


class Libpng(CMakePackage):
    """libpng is the official PNG reference library."""

    homepage = "http://www.libpng.org/pub/png/libpng.html"
    url = "https://prdownloads.sourceforge.net/libpng/libpng-{version}.tar.xz"

    versions = [
        "1.6.47",
    ]
