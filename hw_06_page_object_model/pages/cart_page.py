"""
Cart Page — Page Object for the SauceDemo shopping cart page.
"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object representing the SauceDemo cart screen."""

    # --- Locators ---
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _CART_ITEMS      = (By.CLASS_NAME, "cart_item")

    # --- Actions ---
    def proceed_to_checkout(self) -> None:
        """Click the Checkout button to proceed to the checkout form."""
        self._click(self._CHECKOUT_BUTTON)

    # --- Queries ---
    def get_item_count(self) -> int:
        """Return the number of items currently in the cart."""
        return len(self._find_all(self._CART_ITEMS))
