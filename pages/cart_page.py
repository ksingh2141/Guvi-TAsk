from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Page Object for SauceDemo Cart page.
    """

    CART_ITEMS = (
        By.CLASS_NAME,
        "cart_item"
    )

    ITEM_NAME = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    ITEM_PRICE = (
        By.CLASS_NAME,
        "inventory_item_price"
    )

    CHECKOUT = (
        By.ID,
        "checkout"
    )

    CONTINUE_SHOPPING = (
        By.ID,
        "continue-shopping"
    )

    def get_cart_items(self):
        """
        Return all products currently in the cart.

        Important:
        An empty cart is a valid state, especially after
        Reset App State. Therefore, this method must not
        wait for at least one cart item.
        """

        return self.driver.find_elements(
            *self.CART_ITEMS
        )

    def get_cart_details(self):
        """
        Return product names and prices from the cart.
        """

        items = self.driver.find_elements(
            *self.CART_ITEMS
        )

        products = []

        for item in items:

            name = item.find_element(
                *self.ITEM_NAME
            ).text.strip()

            price = item.find_element(
                *self.ITEM_PRICE
            ).text.strip()

            products.append(
                {
                    "name": name,
                    "price": price
                }
            )

        return products

    def proceed_to_checkout(self):
        """
        Click Checkout button.
        """

        self.wait.until(
            EC.element_to_be_clickable(
                self.CHECKOUT
            )
        ).click()

    def continue_shopping(self):
        """
        Continue shopping from cart.
        """

        self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_SHOPPING
            )
        ).click()