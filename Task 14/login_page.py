from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    # Locators
    username = (By.XPATH,"//input[@id=':r1:']")
    password = (By.XPATH,"//input[@id=':r2:']")
    login_btn = (By.XPATH,"//button[@type = 'submit']")

    popup = (
        By.XPATH,
        "//button[@aria-label='Close popup']"
    )

    profile = (By.XPATH,"//div[@class = 'user-name-div']")

    logout = (By.XPATH,"//div[@class='user-avatar-menu' and text()='Log out']")

    def enter_username(self,uname):

        self.wait.until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(uname)


    def enter_password(self,pwd):

        self.wait.until(
            EC.visibility_of_element_located(self.password)
        ).send_keys(pwd)


    def click_login(self):

        self.wait.until(
            EC.element_to_be_clickable(self.login_btn)
        ).click()


    def login(self,uname,pwd):

        self.enter_username('kundansingh2141@gmail.com')
        self.enter_password('Arcpk@8929')
        self.click_login()


    def close_popup(self):

        try:
            self.wait.until(
                EC.element_to_be_clickable(self.popup)
            ).click()

            print("Popup closed")

        except TimeoutException:

            print("Popup not available")

    def logout_user(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.profile
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.logout
            )
        ).click()