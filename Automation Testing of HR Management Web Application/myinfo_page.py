from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MyInfoPage(BasePage):
    """
    Page Object for My Info Module
    """

    MY_INFO = (
        By.XPATH,
        "//span[normalize-space()='My Info']"
    )

    PERSONAL_DETAILS = (
        By.XPATH,
        "//a[normalize-space()='Personal Details']"
    )

    CONTACT_DETAILS = (
        By.XPATH,
        "//a[normalize-space()='Contact Details']"
    )

    EMERGENCY_CONTACTS = (
        By.XPATH,
        "//a[normalize-space()='Emergency Contacts']"
    )

    DEPENDENTS = (
        By.XPATH,
        "//a[normalize-space()='Dependents']"
    )

    IMMIGRATION = (
        By.XPATH,
        "//a[normalize-space()='Immigration']"
    )

    JOB = (
        By.XPATH,
        "//a[normalize-space()='Job']"
    )

    SALARY = (
        By.XPATH,
        "//a[normalize-space()='Salary']"
    )

    TAX_EXEMPTIONS = (
        By.XPATH,
        "//a[normalize-space()='Tax Exemptions']"
    )

    REPORT_TO = (
        By.XPATH,
        "//a[normalize-space()='Report-to']"
    )

    QUALIFICATIONS = (
        By.XPATH,
        "//a[normalize-space()='Qualifications']"
    )

    MEMBERSHIPS = (
        By.XPATH,
        "//a[normalize-space()='Memberships']"
    )

    def open_my_info(self):
        self.click(self.MY_INFO)

    def verify_all_tabs(self):

        tabs = [
            self.PERSONAL_DETAILS,
            self.CONTACT_DETAILS,
            self.EMERGENCY_CONTACTS
        ]

        for tab in tabs:
            if not self.is_displayed(tab):
                return False

        return True

    def click_tab(self, locator):
        self.click(locator)