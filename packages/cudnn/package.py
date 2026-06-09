from lib.build_systems.binary import BinaryPackage


class Cudnn(BinaryPackage):
    """NVIDIA cuDNN is a GPU-accelerated library of primitives for deep
    neural networks"""

    homepage = "https://developer.nvidia.com/cudnn"
    url = "https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-x86_64/cudnn-linux-x86_64-{version}_cuda12-archive.tar.xz"

    versions = [
        "9.23.0.39",
    ]
