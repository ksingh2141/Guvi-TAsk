import pytest

from config.config import (
    URL,
    STANDARD_USER,
    PASSWORD
)

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.menu_page import MenuPage
from pages.cart_page import CartPage

from utilities.logger import LogGenerator


logger = LogGenerator.get_logger()


@pytest.mark.tc10
def test_reset_app_state(driver):
    """
    TC10:
    Validate Reset App State functionality.

    Expected:
        All cart items should be cleared and the
        application should return to its default state.
    """

    logger.info(
        "TC10 started - Reset App State"
    )

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    menu_page = MenuPage(driver)

    try:
        login_page.open(URL)

        login_page.login(
            STANDARD_USER,
            PASSWORD
        )

        assert login_page.is_login_successful(), (
            "Login failed."
        )

        selected_products = (
            products_page.add_random_products_to_cart(4)
        )

        assert len(selected_products) == 4

        assert products_page.get_cart_count() == 4, (
            "Expected cart count 4 before reset."
        )

        menu_page.open_menu()

        menu_page.reset_app_state()

        cart_count = (
            products_page.get_cart_count()
        )

        assert cart_count == 0, (
            f"Expected cart count 0 after reset, "
            f"got {cart_count}."
        )

        products_page.open_cart()

        cart_page = CartPage(driver)

        cart_items = cart_page.get_cart_items()

        assert len(cart_items) == 0, (
            f"Expected empty cart, "
            f"found {len(cart_items)} items."
        )

        logger.info(
            "TC10 passed - Reset App State validated"
        )

    except Exception as error:

        logger.error(
            f"TC10 failed - {error}"
        )

        raise