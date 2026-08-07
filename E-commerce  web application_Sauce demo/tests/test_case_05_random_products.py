import pytest

from config.config import (
    URL,
    STANDARD_USER,
    PASSWORD
)

from pages.login_page import LoginPage
from pages.products_page import ProductsPage

from utilities.random_products import RandomProducts
from utilities.logger import LogGenerator


logger = LogGenerator.get_logger()


@pytest.mark.tc5
def test_random_product_selection(driver):
    """
    TC5:
    Randomly select 4 out of 6 products and extract
    their names and prices.

    Expected:
        Exactly 4 unique products should be selected.
    """

    logger.info(
        "TC5 started - Random product selection"
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

        all_products = products_page.get_all_products()

        assert len(all_products) == 6, (
            f"Expected 6 products, "
            f"found {len(all_products)}."
        )

        product_data = []

        for product in all_products:

            name = product.find_element(
                *products_page.PRODUCT_NAME
            ).text.strip()

            price = product.find_element(
                *products_page.PRODUCT_PRICE
            ).text.strip()

            assert name, "Product name is empty."

            assert price.startswith("$"), (
                f"Invalid price: {price}"
            )

            product_data.append({
                "name": name,
                "price": price
            })

        selected_products = RandomProducts.choose(
            product_data,
            4
        )

        assert len(selected_products) == 4

        selected_names = [
            product["name"]
            for product in selected_products
        ]

        assert len(selected_names) == len(
            set(selected_names)
        ), (
            "Duplicate products selected."
        )

        for product in selected_products:

            logger.info(
                f'Selected: {product["name"]} | '
                f'{product["price"]}'
            )

        logger.info(
            "TC5 passed - 4 products selected"
        )

    except Exception as error:

        logger.error(
            f"TC5 failed - {error}"
        )

        raise