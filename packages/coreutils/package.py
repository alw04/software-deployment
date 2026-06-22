from lib.build_systems.autotools import AutotoolsPackage


class Coreutils(AutotoolsPackage):
    """The GNU Core Utilities are the basic file, shell and text
    manipulation utilities of the GNU operating system.  These are
    the core utilities which are expected to exist on every
    operating system.
    """

    homepage = "https://www.gnu.org/software/coreutils/"
    url = "https://ftp.gnu.org/gnu/coreutils/coreutils-{version}.tar.xz"

    versions = [
        "9.7",
    ]
