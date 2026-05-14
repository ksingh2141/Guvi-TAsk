import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.guvi.in/")
time.sleep(5)

# Courses
courses = driver.find_element(By.XPATH, "//a[contains(text(),'Courses')]")

# LIVE Classes
live = driver.find_element(By.XPATH, "//a[contains(text(),'LIVE Classes')]")

# Practice
practice = driver.find_element(By.XPATH, "//a[contains(text(),'Practice')]")

# Resources
resources = driver.find_element(By.XPATH, "//a[contains(text(),'Resources')]")

# Our Products
Products = driver.find_element(By.XPATH, "(//*[contains(text(),'Our Products')])[1]")

# Login
login = driver.find_element(By.XPATH, "(//button[@id='login-btn'])[1]")

# Sign up
signup = driver.find_element(By.XPATH, "(//button[text()='Sign up'])[1]")


print("All elements found successfully")

time.sleep(3)

# Parent element
parent = driver.find_element(
    By.XPATH,
    "//a[text()='Courses']/parent::*"
)

print("Parent Element Found")

# First child
first_child = driver.find_element(
    By.XPATH,
    "//a[text()='Courses']/parent::*/*[1]"
)

print("First Child Found")
# Following siblings
siblings = driver.find_elements(
    By.XPATH,
    "//a[text()='Courses']/following-sibling::*"
)

print("Following Siblings Count:", len(siblings))

time.sleep(3)
driver.quit()