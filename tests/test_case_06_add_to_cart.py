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


@pytest.mark.tc6
@pytest.mark.cart
def test_add_selected_products_to_cart(driver):
    """
    TC6:
    Add 4 randomly selected products to the cart.

    Expected:
        Cart badge should display 4.
    """

    logger.info(
        "TC6 started - Add products to cart"
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

        assert len(selected_products) == 4, (
            f"Expected 4 products, "
            f"got {len(selected_products)}."
        )

        cart_count = products_page.get_cart_count()

        assert cart_count == 4, (
            f"Expected cart count 4, "
            f"got {cart_count}."
        )

        for product in selected_products:

            logger.info(
                f'Added: {product["name"]} | '
                f'{product["price"]}'
            )

        logger.info(
            "TC6 passed - 4 products added"
        )

    except Exception as error:

        logger.error(
            f"TC6 failed - {error}"
        )

        raise