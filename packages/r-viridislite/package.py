from lib.build_systems.r import RPackage


class RViridislite(RPackage):
    """Colorblind-Friendly Color Maps (Lite Version).

    Color maps designed to improve graph readability for readers with common
    forms of color blindness and/or color vision deficiency. The color maps are
    also perceptually-uniform, both in regular form and also when converted to
    black-and-white for printing. This is the 'lite' version of the 'viridis'
    package that also contains 'ggplot2' bindings for discrete and continuous
    color and fill scales and can be found at
    <https://cran.r-project.org/package=viridis>."""

    homepage = "https://sjmgarnier.github.io/viridisLite/"
    cran = "viridisLite"

    versions = [
        "0.4.3",
    ]
