from lib.build_systems.r import RPackage


class RS7(RPackage):
    """A new object oriented programming system designed to
    be a successor to S3 and S4. It includes formal class, generic,
    and method specification, and a limited form of multiple dispatch.
    """

    homepage = "https://rconsortium.github.io/S7/"
    cran = "S7"

    versions = [
        "0.2.2",
    ]
