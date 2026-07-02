from lib.build_systems.r import RPackage
from lib.dependency import Dependency


class RScales(RPackage):
    """Scale Functions for Visualization.

    Graphical scales map data to aesthetics, and provide methods for
    automatically determining breaks and labels for axes and legends."""

    homepage = "https://scales.r-lib.org/"
    cran = "scales"

    versions = [
        "1.4.0",
    ]

    depends_on = [
        Dependency("r-cli", type=("build", "run")),
        Dependency("r-farver", type=("build", "run")),
        Dependency("r-glue", type=("build", "run")),
        Dependency("r-labeling", type=("build", "run")),
        Dependency("r-lifecycle", type=("build", "run")),
        Dependency("r-r6", type=("build", "run")),
        Dependency("r-rlang", type=("build", "run")),
        Dependency("r-viridislite", type=("build", "run")),
        Dependency("r-rcolorbrewer", type=("build", "run")),
    ]
