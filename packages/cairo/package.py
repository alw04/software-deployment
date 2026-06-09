from lib.build_systems.meson import MesonPackage


class Cairo(MesonPackage):
    """Cairo is a 2D graphics library with support for multiple output
    devices."""

    homepage = "https://www.cairographics.org/"
    url = "https://www.cairographics.org/releases/cairo-{version}.tar.xz"

    versions = [
        "1.18.2",
    ]
