from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class NetcdfFortran(AutotoolsPackage):
    """NetCDF (network Common Data Form) is a set of software libraries and
    machine-independent data formats that support the creation, access, and
    sharing of array-oriented scientific data. This is the Fortran
    distribution."""

    homepage = "https://www.unidata.ucar.edu/software/netcdf"
    url = "https://downloads.unidata.ucar.edu/netcdf-fortran/{version}/netcdf-fortran-{version}.tar.gz"

    versions = [
        "4.6.2",
    ]

    depends_on = [
        Dependency("netcdf-c"),
    ]
