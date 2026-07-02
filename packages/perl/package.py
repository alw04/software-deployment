from lib.build_systems.autotools import AutotoolsPackage


class Perl(AutotoolsPackage):  # Not Autotools, but follows a similar workflow
    """Perl 5 is a highly capable, feature-rich programming language with over
    27 years of development."""

    homepage = "https://www.perl.org"
    url = "http://www.cpan.org/src/5.0/perl-{version}.tar.gz"

    versions = [
        "5.36.0",
    ]

    def configure(self):
        self.run_cmd(
            [str(self.build_dir / "Configure"), "-des", f"-Dprefix={self.prefix}", "-Dusethreads"], cwd=self.build_dir
        )
