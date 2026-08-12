from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    LOGIN = (By.ID, "login-btn")

    SIGNUP = (
        By.XPATH,
        "//button[contains(text(),'Sign up')]"
    )

    COURSES = (
        By.XPATH,
        "//p[text()='Courses']"
    )

    LIVE_CLASSES = (
        By.XPATH,
        "//p[text()='LIVE Classes']"
    )

    PRACTICE = (
        By.XPATH,
        "//p[text()='Practice']"
    )

    DOBBY = (
        By.XPATH,
        "//div[@id='zsiq_float']"

    )

    def login_visible(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.LOGIN)
            ).is_displayed()
        except:
            return False

    def click_login(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "email")
            )
        )

    def signup_visible(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.SIGNUP)
            ).is_displayed()
        except:
            return False

    def click_signup(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.SIGNUP)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def signup_page_displayed(self):
        try:
            self.wait.until(
                lambda d: "register" in d.current_url.lower()
            )
            return True
        except:
            return False

    def courses_visible(self):
        return self.exists(self.COURSES)

    def live_classes_visible(self):
        return self.exists(self.LIVE_CLASSES)

    def practice_visible(self):
        return self.exists(self.PRACTICE)

    def dobby_visible(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.DOBBY)
            ).is_displayed()
        except:
            return False