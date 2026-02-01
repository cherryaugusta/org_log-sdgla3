import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def configure_logger(
    logger_name: str,
    log_file: str,
    level: int = logging.INFO,
    max_bytes: int = 5_000_000,
    backup_count: int = 5
) -> logging.Logger:
    """
    Configure and return a named logger with rotation support.

    Parameters
    ----------
    logger_name : str
        Unique name for the logger instance.
    log_file : str
        Path to the log file.
    level : int
        Logging level (default: logging.INFO).
    max_bytes : int
        Maximum size of a log file before rotation.
    backup_count : int
        Number of rotated log files to keep.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    # Ensure log directory exists
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Create or retrieve a named logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is reconfigured
    if logger.handlers:
        return logger

    # Define log message format
    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )

    # Create rotating file handler
    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    # Attach handler to logger
    logger.addHandler(file_handler)

    # Disable propagation to root logger
    logger.propagate = False

    return logger
