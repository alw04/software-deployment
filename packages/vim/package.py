from lib.build_systems.autotools import AutotoolsPackage


class Vim(AutotoolsPackage):
    """Vim is a highly configurable text editor built to enable efficient text
    editing. It is an improved version of the vi editor distributed with most
    UNIX systems.  Vim is often called a "programmer's editor," and so useful
    for programming that many consider it an entire IDE. It's not just for
    programmers, though. Vim is perfect for all kinds of text editing, from
    composing email to editing configuration files.
    """

    homepage = "https://www.vim.org"
    url = "https://github.com/vim/vim/archive/v{version}.tar.gz"

    versions = [
        "9.1.1194",
    ]
