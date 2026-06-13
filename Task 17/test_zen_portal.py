import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import Config


class TestZenPortal:

    def test_successful_login(self, setup):

        page = setup

        login = LoginPage(page)

        login.open_url(Config.URL)

        login.login(
            Config.USERNAME,
            Config.PASSWORD
        )

        page.wait_for_load_state("networkidle")

        assert "dashboard" in page.url.lower()

    def test_unsuccessful_login(self, setup):

        page = setup

        login = LoginPage(page)

        login.open_url(Config.URL)

        login.login(
            Config.INVALID_USERNAME,
            Config.INVALID_PASSWORD
        )

        page.wait_for_timeout(3000)

        assert page.url == "https://www.zenclass.in/login"

    def test_username_inputbox(self, setup):

        page = setup

        login = LoginPage(page)

        login.open_url(Config.URL)

        assert login.validate_username_box()

    def test_password_inputbox(self, setup):

        page = setup

        login = LoginPage(page)

        login.open_url(Config.URL)

        assert login.validate_password_box()

    def test_submit_button(self, setup):

        page = setup

        login = LoginPage(page)

        login.open_url(Config.URL)

        assert login.validate_submit_button()

    def test_logout_functionality(self, setup):

        page = setup

        login = LoginPage(page)

        login.open_url(Config.URL)

        login.login(
            Config.USERNAME,
            Config.PASSWORD
        )

        dashboard = DashboardPage(page)

        self.popup_close = page.locator(
            "button[aria-label='Close popup']"
        ).click()
        

        dashboard.logout()

        page.wait_for_timeout(3000)

        assert "login" in page.url.lower()