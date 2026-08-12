import pytest

from config.config import (
    URL,
    STANDARD_USER,
    PASSWORD,
    FIRST_NAME,
    LAST_NAME,
    ZIP
)

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utilities.logger import LogGenerator
from utilities.screenshot import Screenshot


logger = LogGenerator.get_logger()


@pytest.mark.tc8
@pytest.mark.checkout
def test_complete_checkout(driver):
    """
    TC8:
    Complete checkout and validate order summary.

    Expected:
        Order summary should contain the correct
        products and order confirmation should be displayed.
    """

    logger.info(
        "TC8 started - Checkout"
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

        actual_cart_products = (
            cart_page.get_cart_details()
        )

        expected_products = sorted(
            selected_products,
            key=lambda product: product["name"]
        )

        actual_cart_products = sorted(
            actual_cart_products,
            key=lambda product: product["name"]
        )

        assert actual_cart_products == expected_products, (
            "Cart data does not match selected products."
        )

        cart_page.proceed_to_checkout()

        checkout_page = CheckoutPage(driver)

        checkout_page.enter_checkout_information(
            FIRST_NAME,
            LAST_NAME,
            ZIP
        )

        summary_products = (
            checkout_page.get_summary_products()
        )

        assert len(summary_products) == 4, (
            f"Expected 4 summary products, "
            f"got {len(summary_products)}."
        )

        expected_summary = sorted(
            selected_products,
            key=lambda product: product["name"]
        )

        actual_summary = sorted(
            summary_products,
            key=lambda product: product["name"]
        )

        assert actual_summary == expected_summary, (
            "Order summary does not match selected products."
        )

        # Required screenshot
        screenshot_path = Screenshot.capture(
            driver,
            "TC8_Order_Summary"
        )

        logger.info(
            f"Order summary screenshot: {screenshot_path}"
        )

        checkout_page.finish_order()

        assert checkout_page.verify_order_completed(), (
            "Order confirmation was not displayed."
        )

        confirmation = (
            checkout_page.confirmation_message()
        )

        assert confirmation == "Thank you for your order!", (
            f"Unexpected confirmation: {confirmation}"
        )

        logger.info(
            "TC8 passed - Checkout completed"
        )

    except Exception as error:

        logger.error(
            f"TC8 failed - {error}"
        )

        raise