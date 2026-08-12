from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    USERNAME = (
        By.NAME,
        "username"
    )

    RESET_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    CANCEL_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Cancel']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//h6[text()='Reset Password link sent successfully']"
    )

    def enter_username(self, username):
        self.enter_text(self.USERNAME, username)

    def click_reset(self):
        self.click(self.RESET_BUTTON)

    def reset_password(self, username):
        self.enter_username(username)
        self.click_reset()

    def is_reset_page_displayed(self):
        return self.is_displayed(self.SUCCESS_MESSAGE)