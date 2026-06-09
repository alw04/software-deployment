from lib.build_systems.autotools import AutotoolsPackage


class Curl(AutotoolsPackage):
    """cURL is an open source command line tool and library for
    transferring data with URL syntax"""

    homepage = "https://curl.se/"
    url = "https://curl.haxx.se/download/curl-{version}.tar.xz"

    versions = [
        "8.15.0",
    ]

    def configure_args(self):
        return [
            "--with-ssl",
        ]
