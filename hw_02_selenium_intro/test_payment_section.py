"""
Module for visual testing and capturing specific element screenshots
on the IT Career Hub website.
"""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver() -> webdriver.Chrome:
    """
    Fixture to initialize, configure, and tear down the Chrome WebDriver instance.

    Yields:
        webdriver.Chrome: The configured Chrome WebDriver instance.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()


def test_payment_section_screenshot(driver: webdriver.Chrome) -> None:
    """
    Test Case: Navigate to the Payment Methods section and capture a
    targeted element-level screenshot.

    Steps:
        1. Locate and click the 'Payment Methods' navigation link.
        2. Wait for the payment section block to be fully visible.
        3. Capture a targeted screenshot of the payment block.
        4. Save the screenshot directly to the current module directory.
    """
    wait = WebDriverWait(driver, 10)

    # STEP 1: Locate and click the "Payment Methods" link by text
    # Keeping the original text as required for site interaction
    payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_link.click()

    # STEP 2: Use explicit wait instead of sleep to ensure the element is ready
    payment_section_id = "rec1921734713"
    payment_section = wait.until(
        EC.visibility_of_element_located((By.ID, payment_section_id))
    )

    # STEP 3: Define the output directory and file path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    screenshot_path = os.path.join(current_dir, "payment_methods_capture.png")

    # STEP 4: Capture and save the screenshot of the targeted block
    payment_section.screenshot(screenshot_path)

    print(f"\n[INFO] Chrome element screenshot successfully saved to: {screenshot_path}")