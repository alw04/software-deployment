from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Gnupg(AutotoolsPackage):
    """GNU Pretty Good Privacy (PGP) package."""

    homepage = "https://gnupg.org/index.html"
    url = "https://gnupg.org/ftp/gcrypt/gnupg/gnupg-{version}.tar.bz2"

    versions = [
        "2.5.11",
    ]

    depends_on = [
        Dependency("libgpgerror", type=("build", "link")),
        Dependency("libgcrypt", type=("build", "link")),
        Dependency("libassuan", type=("build", "link")),
        Dependency("libksba", type=("build", "link")),
        Dependency("npth", type=("build", "link")),
        Dependency("sqlite"),
        Dependency("openldap"),
    ]
