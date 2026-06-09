from lib.build_systems.autotools import AutotoolsPackage


class Sparsehash(AutotoolsPackage):
    """Sparse and dense hash-tables for C++ by Google"""

    homepage = "https://github.com/sparsehash/sparsehash"
    url = "https://github.com/sparsehash/sparsehash/archive/sparsehash-{version}.tar.gz"

    versions = [
        "2.0.4",
    ]
