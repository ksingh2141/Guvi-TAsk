from config.config import URL
from pages.login_page import LoginPage


def test_login_fields(driver):

    driver.get(URL)

    login = LoginPage(driver)

    assert login.username_visible()

    assert login.password_visible()

    assert login.login_button_visible()