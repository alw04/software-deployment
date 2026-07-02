from lib.build_systems.r import RPackage


class RRlang(RPackage):
    """Functions for Base Types and Core R and 'Tidyverse' Features.

    A toolbox for working with base types, core R features like the condition
    system, and core 'Tidyverse' features like tidy evaluation."""

    homepage = "https://rlang.r-lib.org/"
    cran = "rlang"

    versions = [
        "1.2.0",
    ]
