from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.guvi.in")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID,"login-btn").click()
time.sleep(2)

driver.find_element(By.ID,"email").send_keys("kundansingh2141@gmail.com")
driver.find_element(By.ID,"password").send_keys("Arcpk@8929")
driver.find_element(By.ID,"login-btn").click()
time.sleep(5)