from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = (By.ID, "email")

    PASSWORD = (By.ID, "password")

    LOGIN = (
        By.XPATH,
        "//a[@id='login-btn']"
    )

    PROFILE = (
        By.XPATH,
        "//img[contains(@class,'gravatar')]"
    )

    LOGOUT = (
        By.ID,
        "signout"
    )

    ERROR = (
        By.XPATH,
        "//div[contains(@class,'invalid-feedback')]"

    )

    def login_page_displayed(self):
        return self.exists(self.EMAIL)

    def login(self, email, password):

        self.type(self.EMAIL, email)

        self.type(self.PASSWORD, password)

        self.click(self.LOGIN)

    def is_logged_in(self):
        self.wait.until(
            EC.visibility_of_element_located(self.PROFILE)
        )
        return True

    def invalid_login_message(self):
        try:
            error = self.wait.until(
                EC.visibility_of_element_located(self.ERROR)
            )
            return "Incorrect Email or Password" in error.text
        except:
            return False

    def logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.PROFILE)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT)
        ).click()