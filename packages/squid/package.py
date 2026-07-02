from lib.build_systems.autotools import AutotoolsPackage


class Squid(AutotoolsPackage):
    """C function library for sequence analysis."""

    homepage = "http://eddylab.org/software.html"
    url = "http://eddylab.org/software/squid/squid-{version}.tar.gz"

    versions = [
        "1.9g",
    ]
