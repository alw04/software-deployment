from lib.package import Package


class Cuda(Package):
    """CUDA is a parallel computing platform and programming model invented
    by NVIDIA. It enables dramatic increases in computing performance by
    harnessing the power of the graphics processing unit (GPU)."""

    homepage = "https://developer.nvidia.com/cuda-zone"

    urls_by_version = {
        "12.9.0": "https://developer.download.nvidia.com/compute/cuda/12.9.0/local_installers/cuda_12.9.0_575.51.03_linux.run",
    }

    versions = [
        "12.9.0",
    ]

    phases = (
        "download",
        "install",
    )

    def install(self):
        installer = self.download_path

        installer.chmod(0o755)

        self.run_cmd([str(installer), "--silent", "--toolkit", f"--toolkitpath={self.prefix}"], cwd=self.download_dir)
