from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.config import URL, EMAIL, PASSWORD


def test_verify_url(driver):
    driver.get(URL)
    assert "guvi.in" in driver.current_url


def test_verify_title(driver):
    driver.get(URL)
    assert "Learn to code in your native language" in driver.title


def test_login_button(driver):
    driver.get(URL)
    home = HomePage(driver)

    assert home.login_visible()

    home.click_login()

    login = LoginPage(driver)

    assert login.login_page_displayed()


def test_signup_button(driver):
    driver.get(URL)
    home = HomePage(driver)

    assert home.signup_visible()


def test_signup_navigation(driver):
    driver.get(URL)
    home = HomePage(driver)

    home.click_signup()

    assert home.signup_page_displayed()


def test_valid_login(driver):
    driver.get(URL)

    HomePage(driver).click_login()

    login = LoginPage(driver)

    login.login(EMAIL, PASSWORD)

    assert login.is_logged_in()


def test_invalid_login(driver):
    driver.get(URL)

    HomePage(driver).click_login()

    login = LoginPage(driver)

    login.login("abc@gmail.com", "123456")

    assert login.invalid_login_message()


def test_menu_items(driver):
    driver.get(URL)

    home = HomePage(driver)

    assert home.courses_visible()
    assert home.live_classes_visible()
    assert home.practice_visible()


def test_dobby(driver):
    driver.get(URL)

    home = HomePage(driver)

    assert home.dobby_visible()


def test_logout(driver):
    driver.get(URL)

    HomePage(driver).click_login()

    login = LoginPage(driver)

    login.login(EMAIL, PASSWORD)

    assert login.is_logged_in()

    login.logout()

    assert HomePage(driver).login_visible()