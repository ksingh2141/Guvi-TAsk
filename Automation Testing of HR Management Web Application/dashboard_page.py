from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class DashboardPage(BasePage):
    """
    Page Object for OrangeHRM Dashboard
    """

    # ==========================
    # Dashboard Header
    # ==========================

    DASHBOARD_HEADER = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    # ==========================
    # Left Menu Items
    # ==========================

    ADMIN = (
        By.XPATH,
        "//span[text()='Admin']"
    )

    PIM = (
        By.XPATH,
        "//span[text()='PIM']"
    )

    LEAVE = (
        By.XPATH,
        "//span[text()='Leave']"
    )

    TIME = (
        By.XPATH,
        "//span[text()='Time']"
    )

    RECRUITMENT = (
        By.XPATH,
        "//span[text()='Recruitment']"
    )

    MY_INFO = (
        By.XPATH,
        "//span[text()='My Info']"
    )

    PERFORMANCE = (
        By.XPATH,
        "//span[text()='Performance']"
    )

    DASHBOARD_MENU = (
        By.XPATH,
        "//span[text()='Dashboard']"
    )

    # ==========================
    # Dashboard Validation
    # ==========================

    def is_dashboard_loaded(self):
        """
        Returns True if Dashboard page is loaded.
        """
        return self.is_displayed(self.DASHBOARD_HEADER)

    # ==========================
    # Generic Menu Methods
    # ==========================

    def click_admin(self):
        self.click(self.ADMIN)

    def click_pim(self):
        self.click(self.PIM)

    def click_leave(self):
        self.click(self.LEAVE)

    def click_time(self):
        self.click(self.TIME)

    def click_recruitment(self):
        self.click(self.RECRUITMENT)

    def click_my_info(self):
        self.click(self.MY_INFO)

    def click_performance(self):
        self.click(self.PERFORMANCE)

    def click_dashboard(self):
        self.click(self.DASHBOARD_MENU)

    # ==========================
    # Menu Visibility
    # ==========================

    def menu_visibility(self):
        """
        Returns visibility status of all required menu items.
        """

        return {
            "Admin": self.is_displayed(self.ADMIN),
            "PIM": self.is_displayed(self.PIM),
            "Leave": self.is_displayed(self.LEAVE),
            "Time": self.is_displayed(self.TIME),
            "Recruitment": self.is_displayed(self.RECRUITMENT),
            "My Info": self.is_displayed(self.MY_INFO),
            "Performance": self.is_displayed(self.PERFORMANCE),
            "Dashboard": self.is_displayed(self.DASHBOARD_MENU)
        }

    # ==========================
    # Verify All Menus Visible
    # ==========================

    def are_all_menus_visible(self):
        """
        Returns True only if all required menus are visible.
        """

        return all(self.menu_visibility().values())

    # ==========================
    # Verify All Menus Clickable
    # ==========================

    def verify_all_menus_clickable(self):
        """
        Clicks each menu one by one.
        Returns True if all clicks succeed.
        """

        menu_list = [
            self.ADMIN,
            self.PIM,
            self.LEAVE,
            self.TIME,
            self.RECRUITMENT,
            self.MY_INFO,
            self.PERFORMANCE,
            self.DASHBOARD_MENU
        ]

        try:
            for menu in menu_list:
                self.click(menu)

            return True

        except TimeoutException:
            return False