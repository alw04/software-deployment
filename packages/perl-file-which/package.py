from lib.build_systems.perl import PerlPackage


class PerlFileWhich(PerlPackage):
    """Perl implementation of the which utility as an API"""

    homepage = "https://metacpan.org/pod/File::Which"
    url = "http://search.cpan.org/CPAN/authors/id/P/PL/PLICEASE/File-Which-{version}.tar.gz"

    versions = [
        "1.27",
    ]
