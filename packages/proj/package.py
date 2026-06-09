from lib.build_systems.cmake import CMakePackage
from lib.dependency import Dependency


class Proj(CMakePackage):
    """PROJ is a generic coordinate transformation software, that transforms
    geospatial coordinates from one coordinate reference system (CRS) to
    another. This includes cartographic projections as well as geodetic
    transformations."""

    homepage = "https://proj.org/"
    url = "https://download.osgeo.org/proj/proj-{version}.tar.gz"

    versions = [
        "9.4.1",
    ]

    depends_on = [
        Dependency("sqlite", type=("build", "link")),
        Dependency("libtiff"),
    ]
