from lib.build_systems.cmake import CMakePackage


class Geos(CMakePackage):
    """GEOS (Geometry Engine, Open Source).

    GEOS is a C/C++ library for computational geometry with a focus on algorithms used in
    geographic information systems (GIS) software. It implements the OGC Simple Features
    geometry model and provides all the spatial functions in that standard as well as many
    others. GEOS is a core dependency of PostGIS, QGIS, GDAL, and Shapely.
    """

    homepage = "https://libgeos.org/"
    url = "https://download.osgeo.org/geos/geos-{version}.tar.bz2"

    versions = [
        "3.14.0",
    ]
