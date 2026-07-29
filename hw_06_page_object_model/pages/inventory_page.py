"""
Inventory Page — Page Object for the SauceDemo product listing page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object representing the SauceDemo product catalogue."""

    # --- Locators ---
    _CART_BADGE  = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK   = (By.CLASS_NAME, "shopping_cart_link")

    def _add_to_cart_button(self, product_name: str) -> tuple:
        """
        Build a dynamic locator for the 'Add to cart' button
        of a specific product by its visible name.
        """
        safe_name = product_name.lower().replace(" ", "-")
        return (By.ID, f"add-to-cart-{safe_name}")

    # --- Actions ---
    def add_product(self, product_name: str) -> None:
        """Click the 'Add to cart' button for the given product name."""
        self._click(self._add_to_cart_button(product_name))

    def go_to_cart(self) -> None:
        """Click the shopping cart icon to navigate to the cart page."""
        self._click(self._CART_LINK)