import logging
import os


class LogGenerator:

    @staticmethod
    def loggen():

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logger = logging.getLogger()

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(
            "logs/automation.log",
            mode="a"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger