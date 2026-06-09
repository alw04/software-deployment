from lib.build_systems.autotools import AutotoolsPackage


class Sqlite(AutotoolsPackage):
    """SQLite is a C-language library that implements a small, fast,
    self-contained, high-reliability, full-featured, SQL database engine.
    """

    homepage = "https://www.sqlite.org"

    urls_by_version = {
        "3.50.4": "https://sqlite.org/2025/sqlite-autoconf-3500400.tar.gz",
    }

    versions = [
        "3.50.4",
    ]
