import logging


def _get_logger(logger_name: str) -> logging.Logger:
    """
    Retrieve a configured logger by name.

    Parameters
    ----------
    logger_name : str
        Name of the logger.

    Returns
    -------
    logging.Logger
        Logger instance.
    """
    return logging.getLogger(logger_name)


def log_info(logger_name: str, message: str) -> None:
    """
    Log an informational message.

    Parameters
    ----------
    logger_name : str
        Logger name.
    message : str
        Message to log.
    """
    _get_logger(logger_name).info(message)


def log_warning(logger_name: str, message: str) -> None:
    """
    Log a warning message.

    Parameters
    ----------
    logger_name : str
        Logger name.
    message : str
        Message to log.
    """
    _get_logger(logger_name).warning(message)


def log_error(logger_name: str, message: str) -> None:
    """
    Log an error message.

    Parameters
    ----------
    logger_name : str
        Logger name.
    message : str
        Message to log.
    """
    _get_logger(logger_name).error(message)
