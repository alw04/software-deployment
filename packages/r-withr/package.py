from lib.build_systems.r import RPackage


class RWithr(RPackage):
    """Run Code 'With' Temporarily Modified Global State.

    A set of functions to run code 'with' safely and temporarily modified
    global state. Many of these functions were originally a part of the
    'devtools' package, this provides a simple package with limited
    dependencies to provide access to these functions."""

    homepage = "https://withr.r-lib.org/"
    cran = "withr"

    versions = [
        "3.0.3",
    ]
