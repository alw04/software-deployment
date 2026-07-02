from lib.build_systems.r import RPackage


class RRcolorbrewer(RPackage):
    """ColorBrewer Palettes.

    Provides color schemes for maps (and other graphics) designed by Cynthia
    Brewer as described at https://colorbrewer2.org/"""

    homepage = "http://colorbrewer2.org"
    cran = "RColorBrewer"

    versions = [
        "1.1-3",
    ]
