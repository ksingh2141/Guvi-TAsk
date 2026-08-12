import pytest

from config.config import URL
from pages.login_page import LoginPage
from utilities.logger import LogGenerator


logger = LogGenerator.get_logger()


@pytest.mark.tc2
@pytest.mark.login
@pytest.mark.parametrize(
    "username, password",
    [
        ("invalid_user", "invalid_password"),
        ("admin", "admin"),
        ("standard_user", "wrong_password"),
        ("test_user", "secret_sauce"),
        ("", ""),
        ("standard_user", ""),
        ("", "secret_sauce"),
        ("!@#$%", "123456"),
    ]
)
def test_invalid_login(
    driver,
    username,
    password
):
    """
    TC2:
    Attempt login with invalid credentials.

    Expected:
        Access should be denied and an error message
        should be displayed.
    """

    logger.info(
        f"TC2 started - Username: {username}"
    )

    login_page = LoginPage(driver)

    try:
        login_page.open(URL)

        login_page.login(
            username,
            password
        )

        error_message = login_page.get_error_message()

        logger.info(
            f"Error message: {error_message}"
        )

        assert error_message.strip(), (
            "Expected login error message."
        )

        assert not login_page.is_login_successful(), (
            f"Invalid credentials were accepted: {username}"
        )

        logger.info(
            f"TC2 passed - Invalid login rejected: {username}"
        )

    except Exception as error:

        logger.error(
            f"TC2 failed - {username}: {error}"
        )

        raise