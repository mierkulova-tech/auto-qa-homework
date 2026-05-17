"""
Module for testing image loading and attribute validation 
on the Selenium WebDriver playground.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    """Fixture to initialize and close the Chrome WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
    yield driver
    driver.quit()


def test_image_download_change(driver: webdriver.Chrome) -> None:
    """
    Test Case: Verify that all images are loaded and the 3rd image 
    possesses the correct 'alt' attribute.

    Steps:
        1. Navigate to the loading images page.
        2. Wait until the delayed images are present in the DOM.
        3. Locate the specific 'award' image element.
        4. Verify that the 'alt' attribute value is "award".
    """
    wait = WebDriverWait(driver, 15)

    # STEP 2: Wait for the last image to be present (indicates loading is finished)
    # Using 'landscape' ID as the completion signal
    wait.until(EC.presence_of_element_located((By.ID, 'landscape')))
    print("All images are successfully loaded.")

    # STEP 3: Locate the target image by its ID
    award_image = driver.find_element(By.ID, 'award')

    # STEP 4: Extract and verify the 'alt' attribute
    alt_text = award_image.get_attribute("alt")

    assert alt_text == "award", f"Expected 'award', but got '{alt_text}'"
    print(f"Success: The third image 'alt' attribute is '{alt_text}'.")