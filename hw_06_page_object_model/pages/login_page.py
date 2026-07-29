"""
Login Page — Page Object for https://www.saucedemo.com/
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object representing the SauceDemo login screen."""

    # --- Locators ---
    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON   = (By.ID, "login-button")

    # --- Actions ---
    def login(self, username: str, password: str) -> None:
        """Enter credentials and submit the login form."""
        self._type(self._USERNAME_INPUT, username)
        self._type(self._PASSWORD_INPUT, password)
        self._click(self._LOGIN_BUTTON)