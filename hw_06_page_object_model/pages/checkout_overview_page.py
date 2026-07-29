"""
Checkout Overview Page — Page Object for the SauceDemo order summary page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    """Page Object representing the SauceDemo checkout summary screen."""

    # --- Locators ---
    _TOTAL_LABEL = (By.CSS_SELECTOR, "[data-test='total-label']")

    # --- Actions ---
    def wait_for_overview_page(self) -> None:
        """Wait until the URL confirms we are on the order overview page."""
        self._wait.until(EC.url_contains("checkout-step-two"))

    # --- Queries ---
    def get_total(self) -> str:
        """
        Read and return the total price string from the summary label.

        Returns:
            str: e.g. 'Total: $58.29'
        """
        total_text = self._get_text(self._TOTAL_LABEL)
        return total_text