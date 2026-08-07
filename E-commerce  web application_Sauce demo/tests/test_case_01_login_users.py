import pytest

from config.config import URL, PASSWORD
from pages.login_page import LoginPage
from utilities.logger import LogGenerator


logger = LogGenerator.get_logger()


@pytest.mark.tc1
@pytest.mark.login
@pytest.mark.parametrize(
    "username, expected_success",
    [
        ("standard_user", True),
        ("problem_user", True),
        ("performance_glitch_user", True),
        ("error_user", True),
        ("visual_user", True),
        ("locked_out_user", False),
    ]
)
def test_login_with_predefined_users(
    driver,
    username,
    expected_success
):
    """
    TC1:
    Login with various predefined SauceDemo users.

    Expected:
        Valid users should successfully log in.
        Locked-out user should be rejected.
    """

    logger.info(f"TC1 started - User: {username}")

    login_page = LoginPage(driver)

    try:
        login_page.open(URL)

        login_page.login(
            username,
            PASSWORD
        )

        if expected_success:

            assert login_page.is_login_successful(), (
                f"Login failed for valid user: {username}"
            )

            logger.info(
                f"Login successful: {username}"
            )

        else:

            error_message = login_page.get_error_message()

            assert error_message.strip(), (
                "Expected an error message for locked user."
            )

            assert "locked out" in error_message.lower(), (
                f"Unexpected error message: {error_message}"
            )

            logger.info(
                f"Locked user correctly rejected: {username}"
            )

    except Exception as error:

        logger.error(
            f"TC1 failed for {username}: {error}"
        )

        raise