from lib.build_systems.autotools import AutotoolsPackage


class Ncurses(AutotoolsPackage):
    """The ncurses (new curses) library is a free software emulation of
    curses in System V Release 4.0, and more. It uses terminfo format,
    supports pads and color and multiple highlights and forms
    characters and function-key mapping, and has all the other
    SYSV-curses enhancements over BSD curses."""

    homepage = "https://invisible-island.net/ncurses/ncurses.html"
    url = "https://ftp.gnu.org/gnu/ncurses/ncurses-{version}.tar.gz"

    versions = [
        "6.3",
    ]

    def configure_args(self):
        return [
            "--with-shared",
            "--with-termlib",
            "--enable-widec",
        ]
