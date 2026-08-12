from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
)
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    Base Page containing reusable Selenium methods.

    All Page Object classes inherit from this class.
    Common Selenium actions and explicit waits are centralized here.
    """

    def __init__(self, driver, timeout=15):
        """
        Initialize BasePage.

        Args:
            driver: Selenium WebDriver instance.
            timeout: Explicit wait timeout in seconds.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        """
        Wait until an element is clickable and click it.

        Args:
            locator: Selenium locator tuple.

        Raises:
            Exception: If the element cannot be clicked.
        """
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )
            element.click()

        except (TimeoutException, ElementClickInterceptedException) as e:
            raise Exception(
                f"Unable to click element: {locator}. Error: {e}"
            ) from e

    def type(self, locator, text):
        """
        Clear a text field and enter the supplied text.

        Args:
            locator: Selenium locator tuple.
            text: Text to enter.
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            element.clear()
            element.send_keys(text)

        except TimeoutException as e:
            raise Exception(
                f"Unable to enter text into element: {locator}"
            ) from e

    def get_text(self, locator):
        """
        Get visible text from an element.

        Args:
            locator: Selenium locator tuple.

        Returns:
            str: Visible element text.
        """
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            ).text

        except TimeoutException:
            return ""

    def get_element(self, locator):
        """
        Return a visible WebElement.

        Args:
            locator: Selenium locator tuple.

        Returns:
            WebElement: Located Selenium element.
        """
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def get_elements(self, locator):
        """
        Return all matching WebElements.

        Args:
            locator: Selenium locator tuple.

        Returns:
            list[WebElement]: Matching elements.
        """
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def is_displayed(self, locator):
        """
        Check whether an element is visible.

        Args:
            locator: Selenium locator tuple.

        Returns:
            bool: True if visible, otherwise False.
        """
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()

        except TimeoutException:
            return False

    def is_present(self, locator):
        """
        Check whether an element is present in the DOM.

        Args:
            locator: Selenium locator tuple.

        Returns:
            bool: True if present, otherwise False.
        """
        try:
            self.wait.until(
                EC.presence_of_element_located(locator)
            )
            return True

        except TimeoutException:
            return False

    def get_attribute(self, locator, attribute):
        """
        Get an element attribute value.

        Args:
            locator: Selenium locator tuple.
            attribute: Attribute name.

        Returns:
            str: Attribute value.
        """
        return self.get_element(locator).get_attribute(attribute)

    def wait_for_url_contains(self, text):
        """
        Wait until the current URL contains the supplied text.

        Args:
            text: Text expected in the URL.

        Returns:
            bool: True when condition is satisfied.
        """
        return self.wait.until(
            EC.url_contains(text)
        )

    def wait_for_title_contains(self, text):
        """
        Wait until the page title contains the supplied text.

        Args:
            text: Text expected in the title.

        Returns:
            bool: True when condition is satisfied.
        """
        return self.wait.until(
            EC.title_contains(text)
        )

    def scroll_to_element(self, locator):
        """
        Scroll an element into the visible browser area.

        Args:
            locator: Selenium locator tuple.
        """
        element = self.get_element(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def js_click(self, locator):
        """
        Click an element using JavaScript.

        Args:
            locator: Selenium locator tuple.
        """
        element = self.get_element(locator)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def take_screenshot(self, file_name):
        """
        Capture a screenshot of the current browser state.

        Args:
            file_name: Complete screenshot file path.
        """
        self.driver.save_screenshot(file_name)

    def page_title(self):
        """
        Return the current page title.

        Returns:
            str: Page title.
        """
        return self.driver.title

    def current_url(self):
        """
        Return the current URL.

        Returns:
            str: Current URL.
        """
        return self.driver.current_url