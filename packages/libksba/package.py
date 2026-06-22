from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Libksba(AutotoolsPackage):
    """Libksba is a library to make the tasks of working with X.509
    certificates, CMS data and related objects easier.
    """

    homepage = "https://gnupg.org/software/libksba/index.html"
    url = "https://gnupg.org/ftp/gcrypt/libksba/libksba-{version}.tar.bz2"

    versions = [
        "1.6.7",
    ]

    depends_on = [
        Dependency("libgpgerror", type="build"),
    ]
