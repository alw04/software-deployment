from lib.build_systems.binary import BinaryPackage


class Uv(BinaryPackage):
    """An extremely fast Python package and project manager, written in Rust."""

    homepage = "https://docs.astral.sh/uv/"
    url = "https://github.com/astral-sh/uv/releases/download/{version}/uv-x86_64-unknown-linux-gnu.tar.gz"

    versions = [
        "0.11.21",
    ]

    def install(self):
        self.install_binary(self.build_dir / "uv")
        self.install_binary(self.build_dir / "uvx")
