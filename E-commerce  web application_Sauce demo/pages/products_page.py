import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class ProductsPage(BasePage):
    """
    Page Object for the Products/Inventory page.
    """

    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    ADD_TO_CART = (By.XPATH, ".//button[contains(text(),'Add to cart')]")

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def get_all_products(self):
        """
        Returns all product cards.
        """
        return self.get_elements(self.INVENTORY_ITEMS)

    def select_random_products(self, count=4):
        """
        Randomly select products.
        """
        products = self.get_all_products()

        if count > len(products):
            raise ValueError("Requested product count exceeds inventory.")

        return random.sample(products, count)

    def add_random_products_to_cart(self, count=4):
        """
        Adds random products to cart and returns details.
        """
        selected_products = self.select_random_products(count)

        product_details = []

        for product in selected_products:

            name = product.find_element(
                By.CLASS_NAME,
                "inventory_item_name"
            ).text

            price = product.find_element(
                By.CLASS_NAME,
                "inventory_item_price"
            ).text

            button = product.find_element(
                By.TAG_NAME,
                "button"
            )

            button.click()

            product_details.append({
                "name": name,
                "price": price
            })

        return product_details

    def get_cart_count(self):
        """
        Returns cart badge count.
        """
        if self.is_displayed(self.CART_BADGE):
            return int(
                self.get_text(self.CART_BADGE)
            )
        return 0

    def open_cart(self):
        self.click(self.CART_ICON)

    def get_product_names(self):
        """
        Product names in current UI order.
        """
        names = []

        elements = self.driver.find_elements(
            By.CLASS_NAME,
            "inventory_item_name"
        )

        for element in elements:
            names.append(element.text)

        return names

    def get_product_prices(self):
        """
        Product prices as float values.
        """
        prices = []

        elements = self.driver.find_elements(
            By.CLASS_NAME,
            "inventory_item_price"
        )

        for element in elements:
            price = float(
                element.text.replace("$", "")
            )

            prices.append(price)

        return prices

    def sort_by_name_ascending(self):
        Select(
            self.get_element(self.SORT_DROPDOWN)
        ).select_by_visible_text(
            "Name (A to Z)"
        )

    def sort_by_name_descending(self):
        Select(
            self.get_element(self.SORT_DROPDOWN)
        ).select_by_visible_text(
            "Name (Z to A)"
        )

    def sort_by_price_low_to_high(self):
        Select(
            self.get_element(self.SORT_DROPDOWN)
        ).select_by_visible_text(
            "Price (low to high)"
        )

    def sort_by_price_high_to_low(self):
        Select(
            self.get_element(self.SORT_DROPDOWN)
        ).select_by_visible_text(
            "Price (high to low)"
        )

    def verify_name_ascending(self):
        names = self.get_product_names()
        return names == sorted(names)

    def verify_name_descending(self):
        names = self.get_product_names()
        return names == sorted(
            names,
            reverse=True
        )

    def verify_price_low_to_high(self):
        prices = self.get_product_prices()
        return prices == sorted(prices)

    def verify_price_high_to_low(self):
        prices = self.get_product_prices()
        return prices == sorted(
            prices,
            reverse=True
        )