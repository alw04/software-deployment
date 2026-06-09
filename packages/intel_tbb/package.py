from lib.build_systems.cmake import CMakePackage


class IntelTbb(CMakePackage):
    """Widely used C++ template library for task parallelism.
    Intel Threading Building Blocks (Intel TBB) lets you easily write parallel
    C++ programs that take full advantage of multicore performance, that are
    portable and composable, and that have future-proof scalability.
    """

    homepage = "https://www.threadingbuildingblocks.org/"
    url = "https://github.com/oneapi-src/oneTBB/archive/v{version}.tar.gz"

    versions = [
        "2022.0.0",
    ]
