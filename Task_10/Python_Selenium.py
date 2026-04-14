from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()

try:
    # Open website
    driver.get("https://www.saucedemo.com/")

    # Fetch Title and URL
    title = driver.title
    current_url = driver.current_url

    print("Title:", title)
    print("URL:", current_url)

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Get page content
    body = driver.find_element(By.TAG_NAME, "body").text

    # Save to text file
    with open("Webpage_task_10.txt", "w", encoding="utf-8") as file:
        file.write(body)

    print("Webpage content saved successfully!")

finally:
    driver.quit()

    