from lib.build_systems.cmake import CMakePackage


class Armadillo(CMakePackage):
    """Armadillo is a high quality linear algebra library (matrix maths)
    for the C++ language, aiming towards a good balance between speed and
    ease of use."""

    homepage = "https://arma.sourceforge.net/"
    url = "http://sourceforge.net/projects/arma/files/armadillo-{version}.tar.xz"

    versions = [
        "14.4.1",
    ]
