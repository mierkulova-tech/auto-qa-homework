from typing import Any, Generator
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from constants import BASE_URL


@pytest.fixture
def driver() -> Generator[WebDriver, Any, None]:
    """
    Fixture to initialize, configure, and tear down the Chrome WebDriver instance.
    ChromeOptions suppress the 'Save password?' popup to prevent UI interference.

    Yields:
        webdriver.Chrome: The configured Chrome WebDriver instance.
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()