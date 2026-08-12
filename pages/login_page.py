from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Login Page Object
    """

    USERNAME = (By.ID, "user-name")

    PASSWORD = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "login-button")

    ERROR = (By.XPATH, "//h3[@data-test='error']")

    MENU = (By.ID, "react-burger-menu-btn")

    LOGOUT = (By.ID, "logout_sidebar_link")

    INVENTORY = (By.ID, "inventory_container")

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        return self.is_displayed(self.INVENTORY)

    def get_error_message(self):
        return self.get_text(self.ERROR)

    def is_menu_visible(self):
        return self.is_displayed(self.MENU)

    def logout(self):
        self.click(self.MENU)
        self.click(self.LOGOUT)

    def is_login_page(self):
        return self.is_displayed(self.LOGIN_BUTTON)