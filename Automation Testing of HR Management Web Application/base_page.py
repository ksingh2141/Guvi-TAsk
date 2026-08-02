from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException
)
from selenium.webdriver.common.by import By
import os
from datetime import datetime


class BasePage:
    """
    Base Page containing common reusable Selenium methods.
    Every page class should inherit from this class.
    """

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # -----------------------------
    # Wait Methods
    # -----------------------------

    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_presence(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    # -----------------------------
    # Element Actions
    # -----------------------------

    def click(self, locator):
        try:
            self.wait_for_clickable(locator).click()

        except (
            TimeoutException,
            ElementClickInterceptedException
        ) as e:
            print(f"Click failed: {e}")
            self.take_screenshot("click_error")
            raise

    def enter_text(self, locator, text):
        try:
            element = self.wait_for_visibility(locator)
            element.clear()
            element.send_keys(text)

        except TimeoutException as e:
            print(f"Unable to enter text: {e}")
            self.take_screenshot("enter_text_error")
            raise

    def get_text(self, locator):
        try:
            return self.wait_for_visibility(locator).text

        except TimeoutException:
            return ""

    def get_attribute(self, locator, attribute):
        try:
            return self.wait_for_visibility(locator).get_attribute(attribute)

        except TimeoutException:
            return ""

    # -----------------------------
    # Validation Methods
    # -----------------------------

    def is_displayed(self, locator):
        try:
            return self.wait_for_visibility(locator).is_displayed()

        except (
            TimeoutException,
            NoSuchElementException
        ):
            return False

    def is_enabled(self, locator):
        try:
            return self.wait_for_visibility(locator).is_enabled()

        except (
            TimeoutException,
            NoSuchElementException
        ):
            return False

    # -----------------------------
    # Browser Methods
    # -----------------------------

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    # -----------------------------
    # Screenshot Utility
    # -----------------------------

    def take_screenshot(self, name):

        folder = "screenshots"

        if not os.path.exists(folder):
            os.makedirs(folder)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"{folder}/{name}_{timestamp}.png"

        self.driver.save_screenshot(filename)

    # -----------------------------
    # Generic Finders
    # -----------------------------

    def find(self, locator):
        return self.wait_for_presence(locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    # -----------------------------
    # Scroll
    # -----------------------------

    def scroll_into_view(self, locator):
        element = self.find(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

    # -----------------------------
    # JavaScript Click
    # -----------------------------

    def js_click(self, locator):
        element = self.find(locator)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # -----------------------------
    # Wait Until Invisible
    # -----------------------------

    def wait_until_invisible(self, locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    # -----------------------------
    # Dropdown Utility
    # -----------------------------

    def select_dropdown_by_text(self, locator, text):
        from selenium.webdriver.support.ui import Select

        dropdown = Select(
            self.wait_for_visibility(locator)
        )

        dropdown.select_by_visible_text(text)