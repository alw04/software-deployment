from lib.build_systems.autotools import AutotoolsPackage


class Mvapich2(AutotoolsPackage):
    """Mvapich2 is a High-Performance MPI Library for clusters with diverse
    networks (InfiniBand, Omni-Path, Ethernet/iWARP, and RoCE) and computing
    platforms (x86 (Intel and AMD), ARM and OpenPOWER)"""

    homepage = "https://mvapich.cse.ohio-state.edu/userguide/userguide_spack/"
    url = "https://mvapich.cse.ohio-state.edu/download/mvapich/mv2/mvapich2-{version}.tar.gz"

    versions = [
        "2.3.7",
    ]
