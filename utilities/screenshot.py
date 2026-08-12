import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver, test_name):

        os.makedirs("screenshots", exist_ok=True)

        time_stamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_name = (
            f"screenshots/{test_name}_{time_stamp}.png"
        )

        driver.save_screenshot(file_name)

        return file_name