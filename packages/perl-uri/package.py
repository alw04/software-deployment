from lib.build_systems.perl import PerlPackage


class PerlUri(PerlPackage):
    """Uniform Resource Identifiers (absolute and relative)"""

    homepage = "https://metacpan.org/pod/URI"
    url = "http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/URI-{version}.tar.gz"

    versions = [
        "5.08",
    ]
