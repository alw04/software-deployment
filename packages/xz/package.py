from lib.build_systems.autotools import AutotoolsPackage


class Xz(AutotoolsPackage):
    """XZ Utils is free general-purpose data compression software with
    high compression ratio. XZ Utils were written for POSIX-like systems,
    but also work on some not-so-POSIX systems. XZ Utils are the successor
    to LZMA Utils."""

    homepage = "https://tukaani.org/xz/"
    url = "https://github.com/tukaani-project/xz/releases/download/v{version}/xz-{version}.tar.xz"

    versions = [
        "5.8.3",
    ]
