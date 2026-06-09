from lib.build_systems.cmake import CMakePackage
from lib.dependency import Dependency


class Gdal(CMakePackage):
    """GDAL: Geospatial Data Abstraction Library.

    GDAL is a translator library for raster and vector geospatial data formats that
    is released under an MIT style Open Source License by the Open Source Geospatial
    Foundation. As a library, it presents a single raster abstract data model and
    single vector abstract data model to the calling application for all supported
    formats. It also comes with a variety of useful command line utilities for data
    translation and processing.
    """

    homepage = "https://www.gdal.org/"
    url = "https://download.osgeo.org/gdal/{version}/gdal-{version}.tar.xz"

    versions = [
        "3.11.4",
    ]

    depends_on = [
        Dependency("proj"),
        Dependency("sqlite"),
        Dependency("libtiff"),
    ]
