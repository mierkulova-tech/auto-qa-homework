"""
Module for testing Drag & Drop functionality on the GlobalSQA demo site.
"""

from typing import Any, Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
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
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    yield driver
    driver.quit()


def accept_cookie_popup(driver: WebDriver, wait: WebDriverWait) -> None:
    """
    Helper: Accept the cookie consent popup if it appears.

    Args:
        driver: The active Chrome WebDriver instance.
        wait: A configured WebDriverWait instance.
    """
    cookie_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-cta-consent")))
    cookie_button.click()


def test_drag_and_drop_image_to_trash(driver: webdriver.Chrome) -> None:
    """
    Test Case: Drag the first photo from the gallery into the Trash area
    and verify that the photo counts are updated correctly.

    Steps:
        1. Accept the cookie consent popup.
        2. Switch into the iframe containing the drag-and-drop widget.
        3. Wait for all gallery photos to be visible.
        4. Locate the first photo and the Trash drop target.
        5. Perform the drag-and-drop action using ActionChains.
        6. Assert that the Trash area contains exactly 1 photo.
        7. Assert that the gallery area contains exactly 3 photos remaining.
    """
    wait = WebDriverWait(driver, 10)

    # STEP 1: Dismiss the cookie consent banner
    accept_cookie_popup(driver, wait)

    # STEP 2: Switch into the iframe wrapping the drag-and-drop demo
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    driver.switch_to.frame(iframe)
    print("Switched into drag-and-drop iframe context.")

    # STEP 3: Wait for all gallery items to be visible
    gallery_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))
    first_photo = gallery_items[0]
    print(f"Gallery loaded. Total photos before drag: {len(gallery_items)}")

    # STEP 4: Locate the Trash drop target
    trash = wait.until(EC.visibility_of_element_located((By.ID, "trash")))
    print("Trash area located.")

    # STEP 5: Perform drag-and-drop using ActionChains
    actions = ActionChains(driver)
    actions.drag_and_drop(first_photo, trash).perform()
    print("Drag-and-drop action executed.")

    # STEP 6: Wait for the photo to appear in Trash, then assert count
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))
    trash_items = driver.find_elements(By.CSS_SELECTOR, "#trash li")
    assert len(trash_items) == 1, (
        f"Expected 1 photo in Trash, but found {len(trash_items)}."
    )
    print(f"Trash count verified: {len(trash_items)} photo(s) in trash.")

    # STEP 7: Assert that exactly 3 photos remain in the gallery
    gallery_items = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
    assert len(gallery_items) == 3, (
        f"Expected 3 photos remaining in gallery, but found {len(gallery_items)}."
    )
    print(f"Gallery count verified: {len(gallery_items)} photo(s) remaining.")