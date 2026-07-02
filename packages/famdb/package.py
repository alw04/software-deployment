from lib.dependency import Dependency
from lib.package import Package


class Famdb(Package):
    """FamDB is a modular HDF5-based export format and query tool
    developed for offline access to the Dfam database of
    transposable element and repetitive DNA families.
    """

    homepage = "https://github.com/Dfam-consortium/famdb"
    url = "https://github.com/Dfam-consortium/FamDB/archive/refs/tags/{version}.tar.gz"

    versions = [
        "3.0.0",
    ]

    depends_on = [
        Dependency("h5py", type="run"),
    ]

    def install(self):
        self.install_directory(self.build_dir, self.prefix / "bin")
