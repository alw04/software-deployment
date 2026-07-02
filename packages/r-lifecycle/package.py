from lib.build_systems.r import RPackage
from lib.dependency import Dependency


class RLifecycle(RPackage):
    """Manage the Life Cycle of your Package Functions.

    Manage the life cycle of your exported functions with shared conventions,
    documentation badges, and non-invasive deprecation warnings. The
    'lifecycle' package defines four development stages (experimental,
    maturing, stable, and questioning) and three deprecation stages
    (soft-deprecated, deprecated, and defunct). It makes it easy to insert
    badges corresponding to these stages in your documentation. Usage of
    deprecated functions are signalled with increasing levels of non-invasive
    verbosity."""

    homepage = "https://lifecycle.r-lib.org/"
    cran = "lifecycle"

    versions = [
        "1.0.5",
    ]

    depends_on = [
        Dependency("r-cli", type=("build", "run")),
        Dependency("r-rlang", type=("build", "run")),
    ]
