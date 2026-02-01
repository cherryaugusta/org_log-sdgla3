from org_log.log_setup import configure_logger
from org_log.log_writer import log_info, log_warning, log_error


def main() -> None:
    """
    Entry point demonstrating organizational logging usage.
    """

    logger_name = "org.application"

    # Configure logger once at application startup
    configure_logger(
        logger_name=logger_name,
        log_file="logs/app.log"
    )

    # Write log messages
    log_info(logger_name, "Application started")
    log_warning(logger_name, "Low disk space detected")
    log_error(logger_name, "Unhandled exception occurred")


if __name__ == "__main__":
    main()
