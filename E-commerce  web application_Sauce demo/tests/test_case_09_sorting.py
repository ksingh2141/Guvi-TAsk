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


@pytest.mark.tc9
def test_sort_price_low_to_high(driver):
    """
    TC9:
    Validate Price (low to high) sorting.
    """

    logger.info(
        "TC9 started - Price low to high"
    )

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    try:

        # Open application
        login_page.open(URL)

        # Login
        login_page.login(
            STANDARD_USER,
            PASSWORD
        )

        assert login_page.is_login_successful(), (
            "Login failed."
        )

        # Get prices before sorting.
        original_prices = (
            products_page.get_product_prices()
        )

        logger.info(
            f"Original prices: {original_prices}"
        )

        # Select Price low -> high.
        products_page.sort_by_price_low_to_high()

        # Get prices after sorting.
        sorted_prices = (
            products_page.get_product_prices()
        )

        logger.info(
            f"Sorted prices: {sorted_prices}"
        )

        # ProductsPage returns float values.
        expected_prices = sorted(
            original_prices
        )

        assert sorted_prices == expected_prices, (
            "Products are not sorted correctly "
            "from low to high.\n"
            f"Expected: {expected_prices}\n"
            f"Actual: {sorted_prices}"
        )

        logger.info(
            "TC9 Price low-to-high passed"
        )

    except Exception as error:

        logger.error(
            f"TC9 price sorting failed: {error}"
        )

        raise


@pytest.mark.tc9
def test_sort_name_z_to_a(driver):
    """
    TC9:
    Validate Name (Z to A) sorting.
    """

    logger.info(
        "TC9 started - Name Z to A"
    )

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    try:

        # Open application
        login_page.open(URL)

        # Login
        login_page.login(
            STANDARD_USER,
            PASSWORD
        )

        assert login_page.is_login_successful(), (
            "Login failed."
        )

        # Get original names.
        original_names = (
            products_page.get_product_names()
        )

        logger.info(
            f"Original names: {original_names}"
        )

        # Select Name Z -> A.
        products_page.sort_by_name_descending()

        # Get sorted names.
        sorted_names = (
            products_page.get_product_names()
        )

        logger.info(
            f"Sorted names: {sorted_names}"
        )

        expected_names = sorted(
            original_names,
            reverse=True
        )

        assert sorted_names == expected_names, (
            "Products are not sorted correctly "
            "from Z to A.\n"
            f"Expected: {expected_names}\n"
            f"Actual: {sorted_names}"
        )

        logger.info(
            "TC9 Name Z-to-A passed"
        )

    except Exception as error:

        logger.error(
            f"TC9 name sorting failed: {error}"
        )

        raise