from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LeavePage(BasePage):
    """
    Page Object for Assign Leave
    """

    # -------------------------
    # Navigation
    # -------------------------

    LEAVE_MENU = (
        By.XPATH,
        "//span[normalize-space()='Leave']"
    )

    ASSIGN_LEAVE = (
        By.XPATH,
        "//a[normalize-space()='Assign Leave']"
    )

    # -------------------------
    # Form Fields
    # -------------------------

    EMPLOYEE_NAME = (
        By.XPATH,
        "//input[@placeholder='Type for hints...']"
    )

    LEAVE_TYPE = (
        By.XPATH,
        "//label[text()='Leave Type']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]"
    )

    FROM_DATE = (
        By.XPATH,
        "//label[text()='From Date']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )

    TO_DATE = (
        By.XPATH,
        "//label[text()='To Date']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )

    COMMENTS = (
        By.TAG_NAME,
        "textarea"
    )

    ASSIGN_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and normalize-space()='Assign']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//p[contains(@class,'oxd-text--toast-message')]"
    )

    CONFIRM_POPUP = (
        By.XPATH,
        "//p[normalize-space()='Confirm Leave Assignment']"
    )

    OK_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Ok']"
    )

    # -------------------------
    # Navigation
    # -------------------------

    def open_assign_leave(self):
        self.click(self.LEAVE_MENU)
        self.click(self.ASSIGN_LEAVE)

    # -------------------------
    # Employee
    # -------------------------

    def select_employee(self, employee):

        self.enter_text(self.EMPLOYEE_NAME, employee)

        option = (
            By.XPATH,
            f"//span[contains(normalize-space(),'{employee}')]"
        )

        self.wait_for_clickable(option).click()

    # -------------------------
    # Leave Type
    # -------------------------

    def select_leave_type(self, leave_type):

        self.click(self.LEAVE_TYPE)

        option = (
            By.XPATH,
            f"//div[@role='option']//span[normalize-space()='{leave_type}']"
        )

        self.wait_for_clickable(option).click()

    # -------------------------
    # Dates
    # -------------------------

    def set_from_date(self, date):

        element = self.find(self.FROM_DATE)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(date)

    def set_to_date(self, date):

        element = self.find(self.TO_DATE)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(date)

    # -------------------------
    # Comments
    # -------------------------

    def enter_comments(self, comments):

        self.enter_text(self.COMMENTS, comments)

    # -------------------------
    # Submit
    # -------------------------

    def click_assign(self):

        self.click(self.ASSIGN_BUTTON)

    # -------------------------
    # Complete Flow
    # -------------------------
    def handle_confirmation_popup(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.CONFIRM_POPUP)
            )

            self.click(self.OK_BUTTON)

        except TimeoutException:
            # Popup did not appear
            pass
    def assign_leave(
            self,
            employee,
            leave_type,
            from_date,
            to_date,
            comments
    ):

        self.select_employee(employee)

        self.select_leave_type(leave_type)

        self.set_from_date(from_date)

        self.set_to_date(to_date)

        self.enter_comments(comments)

        self.click_assign()

        # Handle insufficient leave popup if it appears
        self.handle_confirmation_popup()

    # -------------------------
    # Validation
    # -------------------------

    def leave_assigned_successfully(self):

        return self.is_displayed(
            self.SUCCESS_MESSAGE
        )