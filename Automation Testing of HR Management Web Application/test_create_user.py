import time
import random

from config.config import URL
from config.config import USERNAME
from config.config import PASSWORD

from pages.login_page import LoginPage
from pages.admin_page import AdminPage


def test_create_new_user(driver):

    driver.get(URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    admin = AdminPage(driver)

    admin.open_admin()

    admin.click_add()

    unique_username = f"automation{random.randint(1000,9999)}"

    admin.create_user(
        role="Admin",
        employee="Ranga Akunuri",
        status="Enabled",
        username=unique_username,
        password="Admin@12345"
    )

    time.sleep(2)

    assert admin.user_created_successfully()