from lib.build_systems.cmake import CMakePackage


class Eigen(CMakePackage):
    """Eigen is a C++ template library for linear algebra matrices,
    vectors, numerical solvers, and related algorithms.
    """

    homepage = "https://eigen.tuxfamily.org/"
    url = "https://gitlab.com/libeigen/eigen/-/archive/{version}/eigen-{version}.tar.gz"

    versions = [
        "3.4.0",
    ]
