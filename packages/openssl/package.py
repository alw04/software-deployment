from lib.build_systems.autotools import AutotoolsPackage


class Openssl(AutotoolsPackage):
    """OpenSSL is an open source project that provides a robust, commercial-grade, and
    full-featured toolkit for the Transport Layer Security (TLS) and Secure Sockets Layer (SSL)
    protocols. It is also a general-purpose cryptography library."""

    homepage = "https://www.openssl.org"
    url = "https://www.openssl.org/source/openssl-{version}.tar.gz"

    versions = [
        "3.4.1",
    ]

    def configure(self):
        self.run_cmd(["./Configure", f"--prefix={self.prefix}", f"--openssldir={self.prefix}/ssl"], cwd=self.build_dir)
