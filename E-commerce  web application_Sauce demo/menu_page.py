from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MenuPage(BasePage):
    """
    Page Object for the left navigation menu.
    """

    MENU_BUTTON = (
        By.ID,
        "react-burger-menu-btn"
    )

    ALL_ITEMS = (
        By.ID,
        "inventory_sidebar_link"
    )

    ABOUT = (
        By.ID,
        "about_sidebar_link"
    )

    LOGOUT = (
        By.ID,
        "logout_sidebar_link"
    )

    RESET_APP_STATE = (
        By.ID,
        "reset_sidebar_link"
    )

    CLOSE_MENU = (
        By.ID,
        "react-burger-cross-btn"
    )

    def open_menu(self):
        """
        Open the hamburger menu.
        """

        self.wait.until(
            EC.element_to_be_clickable(
                self.MENU_BUTTON
            )
        ).click()

        # Wait for menu item to become visible.
        self.wait.until(
            EC.visibility_of_element_located(
                self.RESET_APP_STATE
            )
        )

    def close_menu(self):
        """
        Close the hamburger menu.
        """

        self.wait.until(
            EC.element_to_be_clickable(
                self.CLOSE_MENU
            )
        ).click()

    def logout(self):
        """
        Open menu and logout.
        """

        self.open_menu()

        self.wait.until(
            EC.element_to_be_clickable(
                self.LOGOUT
            )
        ).click()

    def reset_app_state(self):
        """
        Reset the SauceDemo application state.

        The menu is expected to already be open when this
        method is called.
        """

        reset_button = self.wait.until(
            EC.visibility_of_element_located(
                self.RESET_APP_STATE
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            reset_button
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.RESET_APP_STATE
            )
        )

        try:
            reset_button.click()

        except Exception:
            # Fallback for SauceDemo's animated side menu.
            self.driver.execute_script(
                "arguments[0].click();",
                reset_button
            )