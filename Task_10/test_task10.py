import Python_Selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

#  Positive Test Case
def test_valid_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url


#  Negative Test Case
def test_invalid_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username and password do not match" in error


#  Title Check
def test_title(driver):
    assert driver.title == "Swag Labs"


#  URL Check (Homepage)
def test_homepage_url(driver):
    assert driver.current_url == "https://www.saucedemo.com/"


#  Dashboard URL after login
def test_dashboard_url(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url