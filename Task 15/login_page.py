from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    txt_username = (By.NAME, "username")
    txt_password = (By.NAME, "password")
    btn_login = (By.XPATH, "//button[@type='submit']")

    dashboard = (By.XPATH, "//h6[text()='Dashboard']")

    user_dropdown = (By.CLASS_NAME, "oxd-userdropdown-tab")
    logout_link = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located(self.txt_username)
        ).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(
            *self.txt_password
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.btn_login)
        ).click()

    def is_login_successful(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.dashboard)
            )
            return True
        except:
            return False

    def logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.user_dropdown)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()