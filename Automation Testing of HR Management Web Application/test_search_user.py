from config.config import URL
from config.config import USERNAME
from config.config import PASSWORD

from pages.login_page import LoginPage
from pages.admin_page import AdminPage


def test_search_user(driver):

    driver.get(URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    admin = AdminPage(driver)

    admin.open_admin()

    admin.search_user(USERNAME)

    assert admin.is_user_present(USERNAME)