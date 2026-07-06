import os
import shutil
import sys


class TermInfo:
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37

    def __init__(self):
        self.supports_color = self.check_color_support()

        self.reset = "\033[0m" if self.supports_color else ""
        self.bold = "\033[1m" if self.supports_color else ""
        self.dim = "\033[2m" if self.supports_color else ""

        self.black = self.fg(self.BLACK)
        self.red = self.fg(self.RED)
        self.green = self.fg(self.GREEN)
        self.yellow = self.fg(self.YELLOW)
        self.blue = self.fg(self.BLUE)
        self.magenta = self.fg(self.MAGENTA)
        self.cyan = self.fg(self.CYAN)
        self.white = self.fg(self.WHITE)

        self.bg_black = self.bg(self.BLACK)
        self.bg_red = self.bg(self.RED)
        self.bg_green = self.bg(self.GREEN)
        self.bg_yellow = self.bg(self.YELLOW)
        self.bg_blue = self.bg(self.BLUE)
        self.bg_magenta = self.bg(self.MAGENTA)
        self.bg_cyan = self.bg(self.CYAN)
        self.bg_white = self.bg(self.WHITE)

    def fg(self, code: int) -> str:
        return f"\033[{code}m" if self.supports_color else ""

    def bg(self, code: int) -> str:
        return f"\033[{code + 10}m" if self.supports_color else ""

    def check_color_support(self) -> bool:
        if "NO_COLOR" in os.environ:
            return False
        if "FORCE_COLOR" in os.environ:
            return True
        if not self.is_tty:
            return False
        if os.environ.get("COLORTERM") in ("truecolor", "24bit"):
            return True

        term = os.environ.get("TERM", "").lower()
        color_terms = ("color", "ansi", "xterm", "screen", "tmux", "linux")
        return any(keyword in term for keyword in color_terms)

    @property
    def is_tty(self) -> bool:
        return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

    @property
    def columns(self) -> int:
        return shutil.get_terminal_size(fallback=(80, 24)).columns

    @property
    def rows(self) -> int:
        return shutil.get_terminal_size(fallback=(80, 24)).lines
