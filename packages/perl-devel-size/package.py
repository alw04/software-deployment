from lib.build_systems.perl import PerlPackage


class PerlDevelSize(PerlPackage):
    """Devel::Size - Perl extension for finding the memory usage of Perl variables"""

    homepage = "https://metacpan.org/pod/Devel::Size"
    url = "https://cpan.metacpan.org/authors/id/N/NW/NWCLARK/Devel-Size-{version}.tar.gz"

    versions = [
        "0.83",
    ]
