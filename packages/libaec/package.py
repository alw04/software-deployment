from lib.build_systems.cmake import CMakePackage


class Libaec(CMakePackage):
    """Libaec provides fast lossless compression of 1 up to 32 bit wide signed
    or unsigned integers (samples). It implements Golomb-Rice compression
    method under the BSD license and includes a free drop-in replacement for
    the SZIP library.
    """

    homepage = "https://gitlab.dkrz.de/k202009/libaec"
    url = "https://gitlab.dkrz.de/api/v4/projects/k202009%2Flibaec/repository/archive.tar.gz?sha=v{version}"

    versions = [
        "1.1.4",
    ]
