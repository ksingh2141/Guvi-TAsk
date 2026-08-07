from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """
    Page Object for Checkout flow.
    """

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    CANCEL = (By.ID, "cancel")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    SUMMARY_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def enter_checkout_information(
        self,
        first_name,
        last_name,
        postal_code
    ):
        """
        Fill checkout information and continue
        to the order overview page.
        """

        self.type(
            self.FIRST_NAME,
            first_name
        )

        self.type(
            self.LAST_NAME,
            last_name
        )

        self.type(
            self.POSTAL_CODE,
            postal_code
        )

        self.click(
            self.CONTINUE
        )

    def get_summary_products(self):
        """
        Return product names and prices from
        the checkout overview page.
        """

        products = []

        # Wait until at least one summary item is visible.
        self.wait.until(
            EC.visibility_of_element_located(
                self.SUMMARY_ITEMS
            )
        )

        items = self.driver.find_elements(
            *self.SUMMARY_ITEMS
        )

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

    def capture_order_summary(self):
        """
        Save screenshot of the checkout overview.
        """

        self.take_screenshot(
            "screenshots/order_summary.png"
        )

    def finish_order(self):
        """
        Click Finish button.
        """

        self.wait.until(
            EC.element_to_be_clickable(
                self.FINISH
            )
        ).click()

    def confirmation_message(self):
        """
        Return final confirmation text.
        """

        return self.get_text(
            self.COMPLETE_HEADER
        )

    def verify_order_completed(self):
        """
        Return True when order completion
        message is displayed.
        """

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.COMPLETE_HEADER
                )
            )

            return (
                self.confirmation_message()
                == "Thank you for your order!"
            )

        except Exception:
            return False

    def cancel_checkout(self):
        """
        Cancel checkout.
        """

        self.click(
            self.CANCEL
        )