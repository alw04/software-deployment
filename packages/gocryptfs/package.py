import shutil

from lib.dependency import Dependency
from lib.package import Package


class Gocryptfs(Package):
    """Encrypted overlay filesystem written in Go"""

    homepage = "https://nuetzlich.net/gocryptfs/"
    url = "https://github.com/rfjakob/gocryptfs/releases/download/v{version}/gocryptfs_v{version}_src.tar.gz"

    versions = [
        "2.5.1",
    ]

    depends_on = [
        Dependency("go", type="build"),
    ]

    def build(self):
        self.run_cmd(["./build-without-openssl.bash"], cwd=self.build_dir)

    def install(self):
        bin_src = self.build_dir / "gocryptfs"
        bin_dst = self.prefix / "bin"

        bin_dst.mkdir(parents=True, exist_ok=True)

        shutil.copy2(bin_src, bin_dst / "gocryptfs")
