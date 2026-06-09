from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Pspp(AutotoolsPackage):
    """GNU PSPP is a program for statistical analysis of sampled data."""

    homepage = "https://www.gnu.org/software/pspp/"
    url = "https://ftp.gnu.org/gnu/pspp/pspp-{version}.tar.gz"

    versions = [
        "2.1.0",
    ]

    depends_on = [
        Dependency("texinfo", type="build"),
        Dependency("cairo"),
        Dependency("pango"),
        Dependency("gsl"),
        Dependency("readline"),
    ]

    def configure_args(self):
        return [
            "--without-gui",
        ]
