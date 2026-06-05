from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class R(AutotoolsPackage):
    """R is 'GNU S', a freely available language and environment for
    statistical computing and graphics which provides a wide variety of
    statistical and graphical techniques: linear and nonlinear modelling,
    statistical tests, time series analysis, classification, clustering, etc.
    Please consult the R project homepage for further information."""

    homepage = "https://www.r-project.org"

    def url_for_version(self, version):
        major = version.split(".")[0]
        return f"https://cloud.r-project.org/src/base/R-{major}/R-{version}.tar.gz"

    versions = [
        "4.5.1",
    ]

    depends_on = [
        Dependency("readline"),
    ]

    def configure_args(self):
        return [
            "--with-x=no",
            "--enable-R-shlib",
        ]
