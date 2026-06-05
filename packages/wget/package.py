from lib.build_systems.autotools import AutotoolsPackage


class Wget(AutotoolsPackage):
    """GNU Wget is a free software package for retrieving files using
    HTTP, HTTPS and FTP, the most widely-used Internet protocols. It is a
    non-interactive commandline tool, so it may easily be called from scripts,
    cron jobs, terminals without X-Windows support, etc."""

    homepage = "https://www.gnu.org/software/wget/"
    url = "https://ftp.gnu.org/gnu/wget/wget-{version}.tar.gz"

    versions = [
        "1.24.5",
    ]
