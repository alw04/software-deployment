from lib.build_systems.r import RPackage
from lib.dependency import Dependency


class RVctrs(RPackage):
    """Vector Helpers.

    Defines new notions of prototype and size that are used to provide tools
    for consistent and well-founded type-coercion and size-recycling, and are
    in turn connected to ideas of type- and size-stability useful for analyzing
    function interfaces."""

    homepage = "https://vctrs.r-lib.org/"
    cran = "vctrs"

    versions = [
        "0.7.3",
    ]

    depends_on = [
        Dependency("r-cli", type=("build", "run")),
        Dependency("r-glue", type=("build", "run")),
        Dependency("r-lifecycle", type=("build", "run")),
        Dependency("r-rlang", type=("build", "run")),
    ]
