"""
Checkout Info Page — Page Object for the SauceDemo checkout step one (form).
"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutInfoPage(BasePage):
    """Page Object representing the SauceDemo checkout information form."""

    # --- Locators ---
    _FIRST_NAME_INPUT = (By.ID, "first-name")
    _LAST_NAME_INPUT  = (By.ID, "last-name")
    _POSTAL_CODE_INPUT = (By.ID, "postal-code")
    _CONTINUE_BUTTON  = (By.ID, "continue")

    # --- Actions ---
    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Fill in the checkout personal information form."""
        self._type(self._FIRST_NAME_INPUT, first_name)
        self._type(self._LAST_NAME_INPUT, last_name)
        self._type(self._POSTAL_CODE_INPUT, postal_code)
        print(f"Form filled: {first_name} {last_name}, ZIP: {postal_code}")

    def continue_to_overview(self) -> None:
        """Click Continue to proceed to the order overview page."""
        self._click(self._CONTINUE_BUTTON)
