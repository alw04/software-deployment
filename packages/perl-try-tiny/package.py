from lib.build_systems.perl import PerlPackage


class PerlTryTiny(PerlPackage):
    """Minimal try/catch with proper preservation of $@"""

    homepage = "https://metacpan.org/pod/Try::Tiny"
    url = "http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Try-Tiny-{version}.tar.gz"

    versions = [
        "0.31",
    ]
