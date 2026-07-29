"""
Base Page module — parent class for all Page Objects.
Contains shared WebDriver interaction methods.
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Base class inherited by all Page Object classes."""

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def _find(self, locator: tuple) -> WebElement:
        """Wait for element to be visible and return it."""
        return self._wait.until(EC.visibility_of_element_located(locator))

    def _find_all(self, locator: tuple) -> list[WebElement]:
        """Wait for all elements to be visible and return the list."""
        return self._wait.until(EC.visibility_of_all_elements_located(locator))

    def _click(self, locator: tuple) -> None:
        """Wait for element to be clickable and click it."""
        self._wait.until(EC.element_to_be_clickable(locator)).click()

    def _type(self, locator: tuple, text: str) -> None:
        """Clear the field and type the given text."""
        field = self._find(locator)
        field.clear()
        field.send_keys(text)

    def _get_text(self, locator: tuple) -> str:
        """Return the visible text of an element."""
        return self._find(locator).text