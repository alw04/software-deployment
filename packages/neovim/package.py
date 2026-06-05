from lib.build_systems.binary import BinaryPackage


class Neovim(BinaryPackage):
    """Neovim: Vim-fork focused on extensibility and usability"""

    homepage = "https://neovim.io"
    url = "https://github.com/neovim/neovim/releases/download/v{version}/nvim-linux-x86_64.tar.gz"

    versions = [
        "0.11.3",
    ]
