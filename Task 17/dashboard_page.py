from playwright.sync_api import TimeoutError


class DashboardPage:

    def __init__(self, page):

        self.page = page

        self.popup_close = page.locator(
            "button[aria-label='Close popup']"
        )

        self.profile_menu = page.locator(
            "//div[@class = 'profile-click-icon-div']"
        )

        self.logout_btn = page.locator(
            "text=Log out"
        )

    def logout(self):

        try:
            self.profile_menu.click()

            self.logout_btn.wait_for(
                state="visible",
                timeout=5000
            )

            self.logout_btn.click()

        except TimeoutError:
            print("Logout button not found")