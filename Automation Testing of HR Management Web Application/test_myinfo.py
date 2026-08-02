from config.config import URL
from config.config import USERNAME
from config.config import PASSWORD

from pages.login_page import LoginPage
from pages.myinfo_page import MyInfoPage


def test_myinfo_menu(driver):

    driver.get(URL)

    login = LoginPage(driver)

    login.login(USERNAME, PASSWORD)

    myinfo = MyInfoPage(driver)

    myinfo.open_my_info()

    assert myinfo.verify_all_tabs()