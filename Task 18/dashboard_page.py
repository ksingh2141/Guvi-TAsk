from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    from selenium.common.exceptions import TimeoutException

    popup_close = (
        By.XPATH,
        "//button[@aria-label='Close popup']"
    )

    def close_popup_if_present(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.popup_close)
            ).click()
            print("Popup closed")
        except TimeoutException:
            print("Popup not displayed")

    profile_icon = (
        By.XPATH,
        "//div[contains(@class,'profile-click-icon-div')]"
    )

    logout_btn = (
        By.XPATH,
        "//div[text()='Log out']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_profile_icon(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.profile_icon)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def click_logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.logout_btn)
        ).click()

    def logout_from_application(self):
        self.close_popup_if_present()
        self.click_profile_icon()
        self.click_logout()

        WebDriverWait(self.driver, 20).until(
            EC.url_contains("login")
        )

