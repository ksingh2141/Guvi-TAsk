import pytest

from config.config import (
    URL,
    STANDARD_USER,
    PASSWORD
)

from pages.login_page import LoginPage
from utilities.logger import LogGenerator


logger = LogGenerator.get_logger()


@pytest.mark.tc3
@pytest.mark.login
def test_logout_functionality(driver):
    """
    TC3:
    Validate logout functionality.

    Expected:
        User should be redirected to the login screen
        after logout.
    """

    logger.info("TC3 started - Logout functionality")

    login_page = LoginPage(driver)

    try:
        login_page.open(URL)

        login_page.login(
            STANDARD_USER,
            PASSWORD
        )

        assert login_page.is_login_successful(), (
            "User was not successfully logged in."
        )

        assert login_page.is_menu_visible(), (
            "Menu button is not visible."
        )

        login_page.logout()

        assert login_page.is_login_page(), (
            "User was not redirected to login page "
            "after logout."
        )

        logger.info(
            "TC3 passed - Logout successful"
        )

    except Exception as error:

        logger.error(
            f"TC3 failed - Logout: {error}"
        )

        raise