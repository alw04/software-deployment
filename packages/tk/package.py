from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Tk(AutotoolsPackage):
    """Tk is a graphical user interface toolkit that takes developing desktop
    applications to a higher level than conventional approaches. Tk is the standard GUI
    not only for Tcl, but for many other dynamic languages, and can produce rich, native
    applications that run unchanged across Windows, Mac OS X, Linux and more."""

    homepage = "https://www.tcl.tk"
    url = "https://downloads.sourceforge.net/project/tcl/Tcl/{version}/tk{version}-src.tar.gz"

    versions = [
        "8.6.11",
    ]

    depends_on = [
        Dependency("tcl", type=("link", "run")),
    ]

    configure_directory = "unix"

    def configure_args(self):
        return [
            "--enable-threads",
            f"--with-tcl={self.dep('tcl').prefix}/lib",
        ]
