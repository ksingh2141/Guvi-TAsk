from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class AdminPage(BasePage):
    """
    Page Object for Admin Module
    """

    # ==========================
    # Navigation
    # ==========================

    ADMIN_MENU = (
        By.XPATH,
        "//span[text()='Admin']"
    )

    ADD_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Add']"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//p[contains(@class,'oxd-text--toast-message')]"
    )

    # ==========================
    # User Role Dropdown
    # ==========================

    USER_ROLE = (
        By.XPATH,
        "//label[text()='User Role']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]"
    )
    # ==========================
    # Employee Name
    # ==========================

    EMPLOYEE_NAME = (
        By.XPATH,
        "//input[@placeholder='Type for hints...']"
    )

    # ==========================
    # Status Dropdown
    # ==========================

    STATUS = (
        By.XPATH,
        "//label[text()='Status']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]"
    )

    # ==========================
    # Input Fields
    # ==========================

    USERNAME = (
        By.XPATH,
        "//label[text()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )

    PASSWORD = (
        By.XPATH,
        "//label[text()='Password']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )

    CONFIRM_PASSWORD = (
        By.XPATH,
        "//label[text()='Confirm Password']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )

    # ==========================
    # Search
    # ==========================

    SEARCH_USERNAME = (
        By.XPATH,
        "(//input[contains(@class,'oxd-input')])[2]"
    )

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )

    USER_RECORD = (
        By.XPATH,
        "//div[@role='row']"
    )

    # ==========================
    # Navigation
    # ==========================

    def open_admin(self):
        self.click(self.ADMIN_MENU)

    def click_add(self):
        self.click(self.ADD_BUTTON)

    # ==========================
    # Dropdown Helper
    # ==========================

    def select_dropdown(self, locator, value):
        self.click(locator)

        option = (
            By.XPATH,
            f"//div[@role='option']//span[normalize-space()='{value}']"
        )

        self.wait_for_clickable(option).click()

    # ==========================
    # Employee Selection
    # ==========================

    def enter_employee_name(self, employee):

        self.enter_text(self.EMPLOYEE_NAME, employee)

        option = (
            By.XPATH,
            "//div[@role='listbox']//span"
        )

        self.wait_for_clickable(option).click()
    # ==========================
    # Create User
    # ==========================

    def create_user(
            self,
            role,
            employee,
            status,
            username,
            password
    ):

        self.select_dropdown(
            self.USER_ROLE,
            role
        )

        self.enter_employee_name(
            employee
        )

        self.select_dropdown(
            self.STATUS,
            status
        )

        self.enter_text(
            self.USERNAME,
            username
        )

        self.enter_text(
            self.PASSWORD,
            password
        )

        self.enter_text(
            self.CONFIRM_PASSWORD,
            password
        )

        self.click(
            self.SAVE_BUTTON
        )

    # ==========================
    # Success
    # ==========================

    def user_created_successfully(self):

        try:

            return self.is_displayed(
                self.SUCCESS_MESSAGE
            )

        except:

            return False

    # ==========================
    # Search User
    # ==========================

    def search_user(self, username):

        self.enter_text(
            self.SEARCH_USERNAME,
            username
        )

        self.click(
            self.SEARCH_BUTTON
        )

    # ==========================
    # Verify User Exists
    # ==========================

    def is_user_present(self, username):

        locator = (
            By.XPATH,
            f"//div[@role='cell'][contains(.,'{username}')]"
        )

        return self.is_displayed(locator)