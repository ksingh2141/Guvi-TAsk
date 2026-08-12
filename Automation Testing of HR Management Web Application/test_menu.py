from config.config import URL
from config.config import USERNAME
from config.config import PASSWORD

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_verify_main_menu(driver):

    driver.get(URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    dashboard = DashboardPage(driver)

    assert dashboard.is_dashboard_loaded()

    assert dashboard.are_all_menus_visible()

    assert dashboard.verify_all_menus_clickable()