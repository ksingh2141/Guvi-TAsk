import pytest

from config.config import (
    URL,
    STANDARD_USER,
    PASSWORD
)

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.logger import LogGenerator


logger = LogGenerator.get_logger()


@pytest.mark.tc4
@pytest.mark.cart
def test_cart_icon_visibility(driver):
    """
    TC4:
    Verify cart icon visibility after login.

    Expected:
        Cart icon should be visible and accessible.
    """

    logger.info(
        "TC4 started - Cart icon visibility"
    )

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    try:
        login_page.open(URL)

        login_page.login(
            STANDARD_USER,
            PASSWORD
        )

        assert login_page.is_login_successful(), (
            "Login failed."
        )

        assert products_page.is_displayed(
            products_page.CART_ICON
        ), (
            "Cart icon is not visible."
        )

        cart_element = products_page.get_element(
            products_page.CART_ICON
        )

        assert cart_element.is_enabled(), (
            "Cart icon is not enabled."
        )

        logger.info(
            "TC4 passed - Cart icon validated"
        )

    except Exception as error:

        logger.error(
            f"TC4 failed - {error}"
        )

        raise