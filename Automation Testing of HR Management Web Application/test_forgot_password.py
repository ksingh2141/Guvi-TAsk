import os
import pytest

from config.config import URL, USERNAME
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


def test_forgot_password(driver):

    driver.get(URL)

    login = LoginPage(driver)

    login.click_forgot_password()

    forgot = ForgotPasswordPage(driver)

    forgot.reset_password(USERNAME)

    try:
        assert forgot.is_reset_page_displayed(), (
            "Forgot Password validation failed. "
            "Reset Password page was not displayed."
        )

    except AssertionError as e:

        os.makedirs(
            "reports/screenshots",
            exist_ok=True
        )

        screenshot = (
            "reports/screenshots/"
            "forgot_password_failure.png"
        )

        driver.save_screenshot(screenshot)

        pytest.fail(
            f"{str(e)}\n"
            f"Known Issue: OrangeHRM server may return 502 Bad Gateway.\n"
            f"Screenshot: {screenshot}"
        )