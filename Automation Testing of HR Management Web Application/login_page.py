from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for OrangeHRM Login Page
    """

    # ==========================
    # Locators
    # ==========================

    USERNAME = (
        By.NAME,
        "username"
    )

    PASSWORD = (
        By.NAME,
        "password"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    ERROR_MESSAGE = (
        By.XPATH,
        "//p[contains(@class,'oxd-alert-content-text')]"
    )

    FORGOT_PASSWORD = (
        By.XPATH,
        "//p[contains(@class,'orangehrm-login-forgot-header')]"
    )

    USER_DROPDOWN = (
        By.XPATH,
        "//span[@class='oxd-userdropdown-tab']"
    )

    LOGOUT = (
        By.XPATH,
        "//a[text()='Logout']"
    )

    DASHBOARD = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    RESET_PASSWORD_HEADER = (
        By.XPATH,
        "//h6[text()='Reset Password']"
    )

    # ==========================
    # Login
    # ==========================

    def login(self, username, password):
        self.wait_for_visibility(self.USERNAME)
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    # ==========================
    # Validation
    # ==========================

    def is_login_successful(self):
        """
        Returns True if Dashboard appears.
        """

        try:
            return self.is_displayed(self.DASHBOARD)

        except TimeoutException:
            return False

    def get_error_message(self):
        """
        Returns invalid credential message.
        """

        if self.is_displayed(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)

        return ""

    # ==========================
    # Logout
    # ==========================

    def logout(self):
        """
        Logout from application.
        """

        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT)

    # ==========================
    # Forgot Password
    # ==========================

    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD)

    def is_reset_password_page(self):
        return self.is_displayed(
            self.RESET_PASSWORD_HEADER
        )

    # ==========================
    # Login Page Validation
    # ==========================

    def username_visible(self):
        return self.is_displayed(self.USERNAME)

    def password_visible(self):
        return self.is_displayed(self.PASSWORD)

    def login_button_visible(self):
        return self.is_displayed(self.LOGIN_BUTTON)

    # ==========================
    # Complete Login Validation
    # ==========================

    def verify_login_page(self):

        return (
            self.username_visible()
            and self.password_visible()
            and self.login_button_visible()
        )