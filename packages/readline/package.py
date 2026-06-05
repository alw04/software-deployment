from lib.build_systems.autotools import AutotoolsPackage


class Readline(AutotoolsPackage):
    """The GNU Readline library provides a set of functions for use by
    applications that allow users to edit command lines as they are typed in.
    Both Emacs and vi editing modes are available. The Readline library
    includes additional functions to maintain a list of previously-entered
    command lines, to recall and perhaps reedit those lines, and perform
    csh-like history expansion on previous commands."""

    homepage = "https://tiswww.case.edu/php/chet/readline/rltop.html"
    url = "https://ftp.gnu.org/gnu/readline/readline-{version}.tar.gz"

    versions = [
        "8.3",
    ]

    def configure_args(self):
        return [
            "--with-curses",
            "--with-shared-termcap-library",
        ]
