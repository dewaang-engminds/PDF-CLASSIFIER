import logging
from pathlib import Path


def setup_logger(name: str = "CATEGORIZE", log_to_file: bool = True):
    """
    Creates a global logger for both console and file output.
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", "%Y-%m-%d %H:%M:%S")

    sh = logging.StreamHandler()
    sh.setFormatter(fmt)
    logger.addHandler(sh)

    if log_to_file:
        log_dir = Path("data/logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_dir / "run.log")
        fh.setFormatter(fmt)
        logger.addHandler(fh)

    return logger