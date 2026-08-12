from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
import time


class ClaimPage(BasePage):

    CLAIM_MENU = (By.XPATH, "//span[text()='Claim']")

    ASSIGN_CLAIM = (
        By.XPATH,
        "//button[contains(.,'Assign Claim')]"
    )

    EMPLOYEE = (
        By.XPATH,
        "//label[contains(normalize-space(),'Employee Name')]/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )

    EVENT = (
        By.XPATH,
        "(//label[contains(normalize-space(),'Event')]/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')])[1]"
    )

    CURRENCY = (
        By.XPATH,
        "(//label[contains(normalize-space(),'Currency')]/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')])[1]"
    )

    REMARK = (
        By.XPATH,
        "//textarea"
    )

    CREATE = (
        By.XPATH,
        "//button[normalize-space()='Create']"
    )

    SUCCESS = (
        By.XPATH,
        "//div[contains(@class,'oxd-toast-content')]"
    )

    def open_claim(self):
        self.click(self.CLAIM_MENU)

    def click_assign_claim(self):
        self.click(self.ASSIGN_CLAIM)

    def create_claim(self, employee, event, currency, remark):

        # Wait until page opens
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[text()='Create Claim Request']")
            )
        )

        # Employee
        self.enter_text(self.EMPLOYEE, employee)

        # Wait for autocomplete
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@role='listbox'] | //div[contains(@class,'oxd-autocomplete-dropdown')]")
            )
        )

        self.driver.find_element(
            By.XPATH,
            f"//span[normalize-space()='{employee}']"
        ).click()

        # Event
        self.click(self.EVENT)

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[normalize-space()='{event}']")
            )
        ).click()

        # Currency
        self.click(self.CURRENCY)

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[normalize-space()='{currency}']")
            )
        ).click()

        # Remarks
        self.enter_text(self.REMARK, remark)

        # Create
        self.click(self.CREATE)

    def claim_created(self):
        try:
            WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located(self.SUCCESS)
            )
            return True
        except:
            return False