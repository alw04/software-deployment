from lib.build_systems.autotools import AutotoolsPackage


class Tcl(AutotoolsPackage):
    """Tcl (Tool Command Language) is a very powerful but easy to learn dynamic
    programming language, suitable for a very wide range of uses, including web and
    desktop applications, networking, administration, testing and many more. Open source
    and business-friendly, Tcl is a mature yet evolving language that is truly cross
    platform, easily deployed and highly extensible."""

    homepage = "https://www.tcl.tk/"
    url = "https://downloads.sourceforge.net/project/tcl/Tcl/{version}/tcl{version}-src.tar.gz"

    versions = [
        "8.6.11",
    ]

    configure_directory = "unix"

    def configure_args(self):
        return [
            "--enable-threads",
        ]
