from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    username = (By.ID, ":r1:")
    password = (By.ID, ":r2:")
    login_btn = (By.XPATH, "//button[@type= 'submit']")
    error_msg = (
        By.XPATH,"//*[contains(text(),'Invalid email!')]")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, uname):
        self.driver.find_element(*self.username).send_keys(uname)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def is_username_displayed(self):
        try:
            return self.driver.find_element(*self.username).is_displayed()
        except NoSuchElementException:
            return False

    def is_password_displayed(self):
        try:
            return self.driver.find_element(*self.password).is_displayed()
        except NoSuchElementException:
            return False

    def is_login_button_enabled(self):
        return self.driver.find_element(*self.login_btn).is_enabled()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_msg)
        ).text