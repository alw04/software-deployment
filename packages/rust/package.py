from lib.package import Package


class Rust(Package):
    """The Rust programming language toolchain."""

    homepage = "https://www.rust-lang.org"
    url = "https://static.rust-lang.org/dist/rustc-{version}-src.tar.gz"

    versions = [
        "1.85.0",
    ]
