from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Renameutils(AutotoolsPackage):
    """The file renaming utilities (renameutils for short) are a set of programs
    designed to make renaming of files faster and less cumbersome."""

    homepage = "https://www.nongnu.org/renameutils/"
    url = "https://download.savannah.gnu.org/releases/renameutils/renameutils-{version}.tar.gz"

    versions = [
        # 0.12.0: broken upstream autotools install rules.
        # src/Makefile.am contains "($bindir)" instead of "$(bindir)", which breaks
        # variable expansion during install and results in mkdir -p (indir).
        # Requires patching + autoreconf -fi before build.
        "0.12.0",
    ]

    depends_on = [
        Dependency("readline"),
    ]
