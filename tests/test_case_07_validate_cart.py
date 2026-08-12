import pytest

from config.config import (
    URL,
    STANDARD_USER,
    PASSWORD
)

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utilities.logger import LogGenerator


logger = LogGenerator.get_logger()


@pytest.mark.tc7
@pytest.mark.cart
def test_validate_products_inside_cart(driver):
    """
    TC7:
    Validate product names and prices inside cart.

    Expected:
        Cart should contain exactly the same 4 products
        that were selected and added.
    """

    logger.info(
        "TC7 started - Cart product validation"
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

        selected_products = (
            products_page.add_random_products_to_cart(4)
        )

        assert len(selected_products) == 4

        assert products_page.get_cart_count() == 4

        products_page.open_cart()

        cart_page = CartPage(driver)

        actual_products = (
            cart_page.get_cart_details()
        )

        assert len(actual_products) == 4, (
            f"Expected 4 cart items, "
            f"got {len(actual_products)}."
        )

        expected_products = sorted(
            selected_products,
            key=lambda product: product["name"]
        )

        actual_products = sorted(
            actual_products,
            key=lambda product: product["name"]
        )

        assert actual_products == expected_products, (
            "Cart product details do not match.\n"
            f"Expected: {expected_products}\n"
            f"Actual: {actual_products}"
        )

        logger.info(
            "TC7 passed - Cart details validated"
        )

    except Exception as error:

        logger.error(
            f"TC7 failed - {error}"
        )

        raise