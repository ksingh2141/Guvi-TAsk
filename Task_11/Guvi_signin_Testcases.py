import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in")
    driver.maximize_window()
    yield driver
    driver.quit()

#1 validate the URL

def test_login_url_positive(driver):
    driver.find_element(By.XPATH, "//button[@id='login-btn']").click()
    time.sleep(3)

    assert "https://www.guvi.in/sign-in/" in driver.current_url

def test_login_url_negative(driver):
    driver.find_element(By.XPATH, "//button[@id='login-btn']").click()
    time.sleep(3)

    assert driver.current_url != "https://www.guvi.in/login/"

# 2. Validate Username & Password input boxes is visible and enabled

def test_input_fields_positive(driver):
    driver.find_element(By.XPATH, "//button[@id='login-btn']").click()
    time.sleep(3)

    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "password")

    assert email.is_displayed()
    assert email.is_enabled()

    assert password.is_displayed()
    assert password.is_enabled()

def test_input_fields_negative(driver):
    driver.find_element(By.XPATH, "//button[@id='login-btn']").click()
    time.sleep(3)

    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "password")

    # Negative checks (fields should NOT be disabled)
    assert not email.get_attribute("disabled")
    assert not password.get_attribute("disabled")

#3. Validate Submit Button

def test_submit_button_positive(driver):
    driver.find_element(By.XPATH, "//button[@id='login-btn']").click()
    time.sleep(3)

    driver.find_element(By.ID, "email").send_keys("kundansingh2141@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Arcpk@8929")

    driver.find_element(By.ID, "login-btn").click()
    time.sleep(5)

    assert "sign-in" not in driver.current_url

def test_submit_button_negative(driver):
    driver.find_element(By.XPATH, "//button[@id='login-btn']").click()
    time.sleep(3)

    driver.find_element(By.ID, "email").send_keys("kundansingh2141@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Arc8929")

    driver.find_element(By.ID, "login-btn").click()
    time.sleep(5)

    assert "sign-in"  in driver.current_url

