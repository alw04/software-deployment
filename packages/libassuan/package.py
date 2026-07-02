from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Libassuan(AutotoolsPackage):
    """Libassuan is a small library implementing the so-called Assuan protocol."""

    homepage = "https://gnupg.org/software/libassuan/index.html"
    url = "https://gnupg.org/ftp/gcrypt/libassuan/libassuan-{version}.tar.bz2"

    versions = [
        "3.0.2",
    ]

    depends_on = [
        Dependency("libgpg-error", type="build"),
    ]
