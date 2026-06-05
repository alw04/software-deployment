from lib.build_systems.autotools import AutotoolsPackage


class Cmake(AutotoolsPackage):
    """A cross-platform, open-source build system. CMake is a family of
    tools designed to build, test and package software.
    """

    homepage = "https://www.cmake.org"
    url = "https://github.com/Kitware/CMake/releases/download/v{version}/cmake-{version}.tar.gz"

    versions = [
        "3.30.9",
    ]
