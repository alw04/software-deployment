from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Renameutils(AutotoolsPackage):
    """The file renaming utilities (renameutils for short) are a set of programs
    designed to make renaming of files faster and less cumbersome."""

    homepage = "https://www.nongnu.org/renameutils/"
    url = "https://download.savannah.gnu.org/releases/renameutils/renameutils-{version}.tar.gz"

    versions = [
        "0.12.0",
    ]

    depends_on = [
        Dependency("readline"),
    ]
