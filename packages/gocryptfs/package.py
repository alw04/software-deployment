from lib.build_systems.go import GoPackage


class Gocryptfs(GoPackage):
    """Encrypted overlay filesystem written in Go"""

    homepage = "https://nuetzlich.net/gocryptfs/"
    url = "https://github.com/rfjakob/gocryptfs/releases/download/v{version}/gocryptfs_v{version}_src.tar.gz"

    versions = [
        "2.5.1",
    ]
