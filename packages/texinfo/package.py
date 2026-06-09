from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Texinfo(AutotoolsPackage):
    """Texinfo is the official documentation format of the GNU project.

    It was invented by Richard Stallman and Bob Chassell many years ago,
    loosely based on Brian Reid's Scribe and other formatting languages
    of the time. It is used by many non-GNU projects as well."""

    homepage = "https://www.gnu.org/software/texinfo/"
    url = "https://ftp.gnu.org/gnu/texinfo/texinfo-{version}.tar.gz"

    versions = [
        "7.2",
    ]

    depends_on = [
        Dependency("ruby"),
    ]
