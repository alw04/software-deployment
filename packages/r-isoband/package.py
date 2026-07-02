from lib.build_systems.r import RPackage
from lib.dependency import Dependency


class RIsoband(RPackage):
    """Generate Isolines and Isobands from Regularly Spaced Elevation Grids.

    A fast C++ implementation to generate contour lines (isolines) and contour
    polygons (isobands) from regularly spaced grids containing elevation
    data."""

    homepage = "https://isoband.r-lib.org/"
    cran = "isoband"

    versions = [
        "0.3.0",
    ]

    depends_on = [
        Dependency("r-cli", type=("build", "run")),
        Dependency("r-rlang", type=("build", "run")),
        Dependency("r-cpp11", type=("build", "run")),
    ]
