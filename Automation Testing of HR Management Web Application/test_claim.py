from pages.login_page import LoginPage
from pages.claim_page import ClaimPage
from config.config import *


def test_create_claim(driver):

    driver.get(URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    claim = ClaimPage(driver)

    claim.open_claim()

    claim.click_assign_claim()

    claim.create_claim(
        employee="Ranga Akunuri",
        event="Accommodation",
        currency="Indian Rupee",
        remark="Automation Claim Test"
    )

    assert claim.claim_created()