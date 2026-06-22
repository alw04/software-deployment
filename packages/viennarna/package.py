from lib.build_systems.autotools import AutotoolsPackage


class Viennarna(AutotoolsPackage):
    """The ViennaRNA Package consists of a C code library and several
    stand-alone programs for the prediction and comparison of RNA secondary
    structures.
    """

    homepage = "https://www.tbi.univie.ac.at/RNA/"

    def url_for_version(self, version):
        major_minor = ".".join(version.split(".")[:2]).replace(".", "_")
        return f"https://www.tbi.univie.ac.at/RNA/download/sourcecode/{major_minor}_x/ViennaRNA-{version}.tar.gz"

    versions = [
        "2.6.4",
    ]
