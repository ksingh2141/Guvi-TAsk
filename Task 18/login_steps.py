from behave import *

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.config import *
import allure

@given("User launches Zen Portal")
def launch_application(context):

    context.driver.get(URL)
    context.login = LoginPage(context.driver)

@when("User enters valid username and password")
def enter_valid_credentials(context):

    context.login.enter_username(USERNAME)
    context.login.enter_password(PASSWORD)

@when("User enters invalid username and password")
def enter_invalid_credentials(context):

    context.login.enter_username(INVALID_USERNAME)
    context.login.enter_password(INVALID_PASSWORD)

@when("Clicks Login button")
def click_login(context):

    context.login.click_login()



@then("User should login successfully")
def verify_login(context):

    dashboard = DashboardPage(context.driver)

    dashboard.close_popup_if_present()

    WebDriverWait(context.driver, 20).until(
        EC.url_contains("dashboard")
    )

    assert "dashboard" in context.driver.current_url.lower()

@then("Error message should be displayed")
def verify_invalid_login(context):

    assert context.login.get_error_message() != "Invalid email!"

@then("Username field should be visible")
def username_visible(context):

    assert context.login.is_username_displayed()

@then("Password field should be visible")
def password_visible(context):

    assert context.login.is_password_displayed()

@then("Login button should be enabled")
def login_button_enabled(context):

    assert context.login.is_login_button_enabled()