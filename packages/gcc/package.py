from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Gcc(AutotoolsPackage):
    """The GNU Compiler Collection includes front ends for C, C++, Objective-C,
    Fortran, Ada, and Go, as well as libraries for these languages."""

    homepage = "https://gcc.gnu.org"
    url = "https://ftp.gnu.org/gnu/gcc/gcc-{version}/gcc-{version}.tar.gz"

    versions = [
        "15.2.0",
        "12.2.0",
    ]

    depends_on = [
        Dependency("gmp"),
        Dependency("mpfr"),
        Dependency("mpc"),
    ]

    def configure_args(self):
        return [
            "--enable-languages=c,c++,fortran",
            "--disable-multilib",
            f"--with-gmp={self.dep('gmp').prefix}",
            f"--with-mpfr={self.dep('mpfr').prefix}",
            f"--with-mpc={self.dep('mpc').prefix}",
        ]
