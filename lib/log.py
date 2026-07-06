import argparse
import logging

from lib.term import TermInfo


class LogFormatter(logging.Formatter):
    LEVEL_COLORS = {
        logging.INFO: "green",
        logging.DEBUG: "blue",
        logging.WARNING: "yellow",
        logging.ERROR: "red",
        logging.CRITICAL: "red",
    }

    def __init__(self, term: TermInfo):
        super().__init__("[%(levelname)s] %(name)s: %(message)s")
        self.term = term

    def format(self, record: logging.LogRecord) -> str:
        color_name = self.LEVEL_COLORS.get(record.levelno)
        color = getattr(self.term, color_name, "") if color_name else ""

        original_levelname = record.levelname

        if color:
            record.levelname = f"{color}{original_levelname}{self.term.reset}"

        try:
            return super().format(record)
        finally:
            record.levelname = original_levelname


def setup_logging(args: argparse.Namespace, term: TermInfo):
    if args.debug:
        level = logging.DEBUG
    elif args.verbose:
        level = logging.INFO
    else:
        level = logging.WARNING

    handler = logging.StreamHandler()
    handler.setFormatter(LogFormatter(term))

    logging.basicConfig(level=level, handlers=[handler])

    # silence noisy loggers
    logging.getLogger("urllib3").setLevel(logging.WARNING)
