from lib.build_systems.autotools import AutotoolsPackage


class Npth(AutotoolsPackage):
    """nPth is a library to provide the GNU Pth API and thus a
    non-preemptive threads implementation."""

    homepage = "https://gnupg.org/software/npth/index.html"
    url = "https://gnupg.org/ftp/gcrypt/npth/npth-{version}.tar.bz2"

    versions = [
        "1.7",
    ]
