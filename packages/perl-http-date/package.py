from lib.build_systems.perl import PerlPackage


class PerlHttpDate(PerlPackage):
    """Date conversion routines"""

    homepage = "https://metacpan.org/pod/HTTP::Date"
    url = "https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Date-{version}.tar.gz"

    versions = [
        "6.06",
    ]
