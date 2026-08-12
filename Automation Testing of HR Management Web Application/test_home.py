from config.config import URL


def test_home_page(driver):

    driver.get(URL)

    assert "orangehrm" in driver.current_url.lower()