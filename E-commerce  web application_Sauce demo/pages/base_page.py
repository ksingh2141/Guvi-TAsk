from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException
)


class BasePage:
    """
    Base Page containing reusable Selenium methods.
    All Page Objects inherit from this class.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        """Wait until element is clickable and click."""
        try:
            self.wait.until(
                EC.element_to_be_clickable(locator)
            ).click()
        except (TimeoutException, ElementClickInterceptedException) as e:
            raise Exception(f"Unable to click element {locator}\n{e}")

    def type(self, locator, text):
        """Clear textbox and enter text."""
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            raise Exception(f"Unable to enter text into {locator}")

    def get_text(self, locator):
        """Return visible text."""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            ).text
        except TimeoutException:
            return ""

    def get_element(self, locator):
        """Return WebElement."""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def get_elements(self, locator):
        """Return list of WebElements."""
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def is_displayed(self, locator):
        """Check if element is displayed."""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except Exception:
            return False

    def get_attribute(self, locator, attribute):
        """Read element attribute."""
        return self.get_element(locator).get_attribute(attribute)

    def wait_for_url_contains(self, text):
        """Wait until URL contains text."""
        return self.wait.until(
            EC.url_contains(text)
        )

    def wait_for_title_contains(self, text):
        """Wait until title contains text."""
        return self.wait.until(
            EC.title_contains(text)
        )

    def scroll_to_element(self, locator):
        """Scroll element into view."""
        element = self.get_element(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

    def js_click(self, locator):
        """JavaScript click."""
        element = self.get_element(locator)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def take_screenshot(self, file_name):
        """Save screenshot."""
        self.driver.save_screenshot(file_name)

    def page_title(self):
        return self.driver.title

    def current_url(self):
        return self.driver.current_url