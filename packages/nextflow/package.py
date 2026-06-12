from lib.dependency import Dependency
from lib.build_systems.binary import BinaryPackage


class Nextflow(BinaryPackage):
    """Data-driven computational pipelines."""

    homepage = "https://www.nextflow.io"
    url = "https://github.com/nextflow-io/nextflow/releases/download/v{version}/nextflow"

    versions = [
        "25.04.6",
    ]

    depends_on = [
        # Dependency("java", type="run"),
    ]

    phases = (
        "download",
        "install",
    )

    def install(self):
        self.install_binary(self.download_file)
