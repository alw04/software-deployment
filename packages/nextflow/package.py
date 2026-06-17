from lib.build_systems.binary import BinaryPackage
from lib.dependency import Dependency


class Nextflow(BinaryPackage):
    """Data-driven computational pipelines."""

    homepage = "https://www.nextflow.io"
    url = "https://github.com/nextflow-io/nextflow/releases/download/v{version}/nextflow"

    versions = [
        "25.04.6",
        "26.04.3",
    ]

    depends_on = [
        Dependency("openjdk", type="run"),
    ]

    phases = (
        "download",
        "install",
    )

    def install(self):
        self.install_binary(self.download_file)
