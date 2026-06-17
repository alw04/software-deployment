from lib.build_systems.autotools import AutotoolsPackage


class Samtools(AutotoolsPackage):
    """SAM Tools provide various utilities for manipulating alignments in
    the SAM format, including sorting, merging, indexing and generating
    alignments in a per-position format"""

    homepage = "https://www.htslib.org"
    url = "https://github.com/samtools/samtools/releases/download/{version}/samtools-{version}.tar.bz2"

    versions = [
        "1.21",
    ]
