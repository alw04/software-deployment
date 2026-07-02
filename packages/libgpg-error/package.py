from lib.build_systems.autotools import AutotoolsPackage


class LibgpgError(AutotoolsPackage):
    """Common error values for all GnuPG components."""

    homepage = "https://www.gnupg.org/related_software/libgpg-error/index.en.html"
    url = "https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-{version}.tar.bz2"

    versions = [
        "1.55",
    ]
