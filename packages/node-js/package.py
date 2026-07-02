from lib.build_systems.autotools import AutotoolsPackage


class Nodejs(AutotoolsPackage):
    """Node.js is an open-source, cross-platform JavaScript runtime environment."""

    homepage = "https://nodejs.org/"
    url = "https://nodejs.org/dist/v{version}/node-v{version}.tar.gz"

    versions = [
        "22.16.0",
    ]
