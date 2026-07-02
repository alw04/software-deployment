from lib.build_systems.perl import PerlPackage


class PerlHttpMessage(PerlPackage):
    """HTTP style message (base class)"""

    homepage = "https://metacpan.org/pod/HTTP::Message"
    url = "http://search.cpan.org/CPAN/authors/id/O/OA/OALDERS/HTTP-Message-{version}.tar.gz"

    versions = [
        "6.45",
    ]
