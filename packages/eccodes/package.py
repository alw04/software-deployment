from lib.build_systems.cmake import CMakePackage
from lib.dependency import Dependency


class Eccodes(CMakePackage):
    """ecCodes is a package developed by ECMWF for processing meteorological
    data in GRIB (1/2), BUFR (3/4) and GTS header formats."""

    homepage = "https://software.ecmwf.int/wiki/display/ECC/ecCodes+Home"
    url = "https://confluence.ecmwf.int/download/attachments/45757960/eccodes-{version}-Source.tar.gz?api=v2"

    versions = [
        "2.41.0",
    ]

    depends_on = [
        Dependency("netcdfc"),
        Dependency("libaec"),
    ]
