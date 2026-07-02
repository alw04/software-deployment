from lib.build_systems.r import RPackage
from lib.dependency import Dependency


class RGgplot2(RPackage):
    """Create Elegant Data Visualisations Using the Grammar of Graphics.

    A system for 'declaratively' creating graphics, based on "The Grammar of
    Graphics". You provide the data, tell 'ggplot2' how to map variables to
    aesthetics, what graphical primitives to use, and it takes care of the
    details."""

    homepage = "https://ggplot2.tidyverse.org/"
    cran = "ggplot2"

    versions = [
        "4.0.3",
    ]

    depends_on = [
        Dependency("r-cli", type=("build", "run")),
        Dependency("r-gtable", type=("build", "run")),
        Dependency("r-isoband", type=("build", "run")),
        Dependency("r-lifecycle", type=("build", "run")),
        Dependency("r-rlang", type=("build", "run")),
        Dependency("r-s7", type=("build", "run")),
        Dependency("r-scales", type=("build", "run")),
        Dependency("r-vctrs", type=("build", "run")),
        Dependency("r-withr", type=("build", "run")),
        Dependency("r-glue", type=("build", "run")),
        Dependency("r-r6", type=("build", "run")),
        Dependency("r-farver", type=("build", "run")),
        Dependency("r-rcolorbrewer", type=("build", "run")),
    ]
