from lib.build_systems.r import RPackage


class RR6(RPackage):
    """Encapsulated Classes with Reference Semantics.

    The R6 package allows the creation of classes with reference semantics,
    similar to R's built-in reference classes. Compared to reference classes,
    R6 classes are simpler and lighter-weight, and they are not built on S4
    classes so they do not require the methods package. These classes allow
    public and private members, and they support inheritance, even when the
    classes are defined in different packages."""

    homepage = "https://r6.r-lib.org/articles/Introduction.html"
    cran = "R6"

    versions = [
        "2.6.1",
    ]
