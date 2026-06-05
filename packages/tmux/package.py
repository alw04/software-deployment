from lib.build_systems.autotools import AutotoolsPackage


class Tmux(AutotoolsPackage):
    """Tmux is a terminal multiplexer.

    What is a terminal multiplexer? It lets you switch easily between several
    programs in one terminal, detach them (they keep running in the
    background) and reattach them to a different terminal. And do a lot more.
    """

    homepage = "https://tmux.github.io"
    url = "https://github.com/tmux/tmux/releases/download/{version}/tmux-{version}.tar.gz"

    versions = [
        "3.5a",
    ]
