from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Mpc(AutotoolsPackage):
    """Gnu Mpc is a C library for the arithmetic of complex numbers
    with arbitrarily high precision and correct rounding of the
    result."""

    homepage = "https://www.multiprecision.org"
    url = "https://ftp.gnu.org/gnu/mpc/mpc-{version}.tar.gz"

    versions = [
        "1.3.1",
    ]

    depends_on = [
        Dependency("mpfr"),
    ]

    def configure_args(self):
        return [
            f"--with-mpfr={self.dependencies['mpfr'].prefix}",
        ]
