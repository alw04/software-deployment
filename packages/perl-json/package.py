from lib.build_systems.perl import PerlPackage


class PerlJson(PerlPackage):
    """JSON (JavaScript Object Notation) encoder/decoder"""

    homepage = "https://metacpan.org/pod/JSON"
    url = "http://search.cpan.org/CPAN/authors/id/I/IS/ISHIGAKI/JSON-{version}.tar.gz"

    versions = [
        "4.10",
    ]
