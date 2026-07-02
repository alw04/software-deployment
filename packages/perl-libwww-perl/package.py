from lib.build_systems.perl import PerlPackage
from lib.dependency import Dependency


class PerlLibwwwPerl(PerlPackage):
    """The libwww-perl collection is a set of Perl modules which provides
    a simple and consistent application programming interface to the
    World-Wide Web. The main focus of the library is to provide classes and
    functions that allow you to write WWW clients."""

    homepage = "https://github.com/libwww-perl/libwww-perl"
    url = "http://search.cpan.org/CPAN/authors/id/O/OA/OALDERS/libwww-perl-{version}.tar.gz"

    versions = [
        "6.68",
    ]

    depends_on = [
        Dependency("perl-http-message", type=("build", "run")),
        Dependency("perl-clone", type=("build", "run")),
        Dependency("perl-uri", type=("build", "run")),
        Dependency("perl-http-date", type=("build", "run")),
        Dependency("perl-try-tiny", type=("build", "run")),
    ]
