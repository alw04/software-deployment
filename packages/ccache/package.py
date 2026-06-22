from lib.build_systems.cmake import CMakePackage


class Ccache(CMakePackage):
    """ccache is a compiler cache. It speeds up recompilation by caching
    previous compilations and detecting when the same compilation is being done
    again."""

    homepage = "https://ccache.dev/"
    url = "https://github.com/ccache/ccache/releases/download/v{version}/ccache-{version}.tar.gz"

    versions = [
        "4.10.2",
    ]
