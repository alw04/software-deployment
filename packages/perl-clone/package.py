from lib.build_systems.perl import PerlPackage


class PerlClone(PerlPackage):
    """Clone - recursively copy Perl datatypes"""

    homepage = "https://metacpan.org/pod/Clone"
    url = "https://cpan.metacpan.org/authors/id/G/GA/GARU/Clone-{version}.tar.gz"

    versions = [
        "0.46",
    ]
