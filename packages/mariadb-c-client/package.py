from lib.build_systems.cmake import CMakePackage


class MariadbCClient(CMakePackage):
    """MariaDB turns data into structured information in a wide array of
    applications, ranging from banking to websites. It is an enhanced,
    drop-in replacement for MySQL. MariaDB is used because it is fast,
    scalable and robust, with a rich ecosystem of storage engines,
    plugins and many other tools make it very versatile for a wide
    variety of use cases. This package comprises only the standalone 'C
    Connector', which enables connections to MariaDB and MySQL servers.
    """

    homepage = "https://mariadb.org/about/"
    url = "https://archive.mariadb.org//connector-c-{version}/mariadb-connector-c-{version}-src.tar.gz"

    versions = [
        "3.4.5",
    ]

    def install(self):
        super().install()
        self.install_symlink(self.prefix / "bin" / "mariadb_config", self.prefix / "bin" / "mysql_config")
