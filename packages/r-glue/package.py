from lib.build_systems.r import RPackage


class RGlue(RPackage):
    """Interpreted String Literals.

    An implementation of interpreted string literals, inspired by Python's
    Literal String Interpolation <https://www.python.org/dev/peps/pep-0498/>
    and Docstrings <https://www.python.org/dev/peps/pep-0257/> and Julia's
    Triple-Quoted String Literals <https://docs.julialang.org/en/stable/
    manual/strings/#triple-quoted-string-literals>."""

    homepage = "https://glue.tidyverse.org/"
    cran = "glue"

    versions = [
        "1.8.1",
    ]
