from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Udunits(AutotoolsPackage):
    """Automated units conversion"""

    homepage = "https://www.unidata.ucar.edu/software/udunits"
    url = "https://downloads.unidata.ucar.edu/udunits/{version}/udunits-{version}.tar.gz"

    versions = [
        "2.2.28",
    ]

    depends_on = [
        Dependency("expat"),
    ]
