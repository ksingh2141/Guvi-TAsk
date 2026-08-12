import logging
import os


class LogGenerator:
    """
    Creates application logger.
    """

    @staticmethod
    def get_logger():

        os.makedirs("logs", exist_ok=True)

        logger = logging.getLogger("SauceDemo")

        if logger.hasHandlers():
            return logger

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(
            "logs/automation.log"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger