from behave import *
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("User logged into Zen Portal")
def login_first(context):

    context.driver.get(URL)

    login = LoginPage(context.driver)

    login.enter_username(USERNAME)
    login.enter_password(PASSWORD)
    login.click_login()

@when("User clicks Logout button")
def click_logout(context):

    dashboard = DashboardPage(context.driver)
    dashboard.logout_from_application()



@then("User should logout successfully")
def verify_logout(context):

    assert "login" in context.driver.current_url.lower()