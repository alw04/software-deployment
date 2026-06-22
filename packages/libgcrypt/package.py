from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Libgcrypt(AutotoolsPackage):
    """Cryptographic library based on the code from GnuPG."""

    homepage = "https://gnupg.org/software/libgcrypt/index.html"
    url = "https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-{version}.tar.bz2"

    versions = [
        "1.11.1",
    ]

    depends_on = [
        Dependency("libgpgerror", type="build"),
    ]
