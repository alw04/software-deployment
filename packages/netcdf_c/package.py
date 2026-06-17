from lib.build_systems.cmake import CMakePackage
from lib.dependency import Dependency


class NetcdfC(CMakePackage):
    """NetCDF (network Common Data Form) is a set of software libraries and
    machine-independent data formats that support the creation, access, and
    sharing of array-oriented scientific data. This is the C distribution."""

    homepage = "https://www.unidata.ucar.edu/software/netcdf"
    url = "https://github.com/Unidata/netcdf-c/archive/refs/tags/v{version}.tar.gz"

    versions = [
        "4.9.3",
    ]

    depends_on = [
        Dependency("hdf5"),
    ]

    link_libs = [
        "hdf5",
    ]
