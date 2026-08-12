import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """
    Creates and manages a Chrome WebDriver instance for each test.

    The driver is automatically closed after the test completes.
    """

    options = Options()

    # Disable Chrome password manager notifications
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        }
    )

    # Disable password leak detection
    options.add_argument("--disable-features=PasswordLeakDetection")

    # Start browser maximized
    options.add_argument("--start-maximized")

    # Create Chrome WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        yield driver

    finally:
        # Always close browser, even if test fails
        driver.quit()