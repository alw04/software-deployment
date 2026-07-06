from lib.build_systems.cmake import CMakePackage


class Racon(CMakePackage):
    """Ultrafast consensus module for raw de novo genome assembly of long
    uncorrected reads."""

    homepage = "https://github.com/lbcb-sci/racon"
    url = "https://github.com/lbcb-sci/racon/archive/refs/tags/{version}.tar.gz"

    versions = [
        "1.5.0",
    ]

    def cmake_args(self):
        return [
            "-Dracon_build_tests=OFF",
        ]
