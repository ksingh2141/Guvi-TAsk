import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Fixture

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/droppable/")
    yield driver
    driver.quit()

def test_Drag_And_Drop_Positive(driver):
    frame = driver.find_element(By.CLASS_NAME, "demo-frame")
    driver.switch_to.frame(frame)

    source = driver.find_element(By.ID, 'draggable')
    target = driver.find_element(By.ID, 'droppable')

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    time.sleep(5)

    assert "Dropped!" in target.text
    print("Drag And Drop Successful")

def test_Drag_And_Drop_Negative(driver):
        frame = driver.find_element(By.CLASS_NAME, "demo-frame")
        driver.switch_to.frame(frame)

        source = driver.find_element(By.ID, "draggable")
        wrong_target = driver.find_elements(By.ID, "wrongid")

        # Validation
        assert len(wrong_target) == 0

        print("Negative Test Passed - Wrong target not found")