from lib.build_systems.binary import BinaryPackage


class CodeServer(BinaryPackage):
    """code-server is VS Code running on a remote server,
    accessible through the browser."""

    homepage = "https://coder.com/docs/code-server/latest"
    url = "https://github.com/coder/code-server/releases/download/v{version}/code-server-{version}-linux-amd64.tar.gz"

    versions = [
        "4.96.4",
    ]
