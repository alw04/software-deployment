from lib.build_systems.cmake import CMakePackage


class Bamtools(CMakePackage):
    """C++ API & command-line toolkit for working with BAM data."""

    homepage = "https://github.com/pezmaster31/bamtools"
    url = "https://github.com/pezmaster31/bamtools/archive/v{version}.tar.gz"

    versions = [
        "2.5.2",
    ]
