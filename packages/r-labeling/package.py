from lib.build_systems.r import RPackage


class RLabeling(RPackage):
    """Axis Labeling.

    Provides a range of axis labeling algorithms."""

    homepage = "https://CRAN.R-project.org/package=labeling"
    cran = "labeling"

    versions = [
        "0.4.3",
    ]
