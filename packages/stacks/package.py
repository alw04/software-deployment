from lib.build_systems.autotools import AutotoolsPackage


class Stacks(AutotoolsPackage):
    """Stacks is a software pipeline for building loci from short-read
    sequences, such as those generated on the Illumina platform."""

    homepage = "https://catchenlab.life.illinois.edu/stacks/"
    url = "https://catchenlab.life.illinois.edu/stacks/source/stacks-{version}.tar.gz"

    versions = [
        "2.53",
    ]
