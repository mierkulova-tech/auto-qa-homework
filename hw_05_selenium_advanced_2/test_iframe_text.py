"""
Module for testing iframe interaction and text validation
on the Selenium WebDriver Java demo page.
"""

from typing import Any, Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver() -> Generator[WebDriver, Any, None]:
    """
    Fixture to initialize, configure, and tear down the Chrome WebDriver instance.

    Yields:
        webdriver.Chrome: The configured Chrome WebDriver instance.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    yield driver
    driver.quit()


def test_iframe_text_is_displayed(driver: webdriver.Chrome) -> None:
    """
    Test Case: Verify that a specific text is present inside an iframe element.

    Steps:
        1. Navigate to the iframes demo page.
        2. Wait for the iframe to be present in the DOM and switch context into it.
        3. Locate all paragraph elements with class "lead" inside the iframe.
        4. Search for the expected text across all paragraphs.
        5. Assert that the expected text was found in at least one paragraph.
    """
    wait = WebDriverWait(driver, 10)

    # STEP 2: Locate the iframe by ID and switch WebDriver context into it
    iframe = wait.until(EC.presence_of_element_located((By.ID, "my-iframe")))
    driver.switch_to.frame(iframe)
    print("Switched into iframe context.")

    # STEP 3: Locate all lead paragraphs inside the iframe
    paragraphs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lead")))
    print(f"Found {len(paragraphs)} paragraph(s) inside iframe.")

    # STEP 4: Search for the expected text across all paragraphs
    expected_text = "semper posuere integer et senectus justo curabitur."
    found = any(expected_text in paragraph.text for paragraph in paragraphs)

    # STEP 5: Assert the text was found
    assert found, (
        f"Expected text not found inside iframe.\n"
        f"Expected: '{expected_text}'"
    )
    print(f"Validation successful. Text found: '{expected_text}'")