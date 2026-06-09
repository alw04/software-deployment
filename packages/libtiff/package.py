from lib.build_systems.cmake import CMakePackage


class Libtiff(CMakePackage):
    """LibTIFF - Tag Image File Format (TIFF) Library and Utilities."""

    homepage = "http://www.simplesystems.org/libtiff/"
    url = "https://download.osgeo.org/libtiff/tiff-{version}.tar.gz"

    versions = [
        "4.7.0",
    ]
