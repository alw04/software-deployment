from lib.build_systems.autotools import AutotoolsPackage


class Git(AutotoolsPackage):
    """Git is a free and open source distributed version control
    system designed to handle everything from small to very large
    projects with speed and efficiency.
    """

    homepage = "https://git-scm.com"
    url = "https://mirrors.edge.kernel.org/pub/software/scm/git/git-{version}.tar.gz"

    versions = [
        "2.48.1",
    ]
