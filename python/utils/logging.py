import logging
import argparse


def setup_logger(log_level=logging.INFO, log_file=None):
    """
    Configures logging with the specified level and optional file output.

    Args:
        log_level (int, optional): The logging level. Defaults to logging.INFO.
        log_file (str, optional): The path to the log file. Defaults to None.
    """

    try:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )

        handlers = []
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        handlers.append(console_handler)

        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            handlers.append(file_handler)

        logging.basicConfig(level=log_level, handlers=handlers)

    except Exception as e:
        print(f"Error configuring logger: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log level and file options")
    parser.add_argument(
        "-l", "--log-level", choices=logging.getLevelNames(), help="Set log level"
    )
    parser.add_argument("-f", "--log-file", help="Path to the log file")
    args = parser.parse_args()

    setup_logger(
        logging.getLevelName(args.log_level) if args.log_level else logging.INFO,
        args.log_file,
    )

    logging.debug("This is a debug message.")
    logging.info("This is an informational message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")
