"""
Module for testing UI element text changes on the UITestingPlayground website.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    """
    Fixture to initialize and configure the Chrome WebDriver instance.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://uitestingplayground.com/textinput')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_change_text_button(driver: webdriver.Chrome) -> None:
    """
    Test Case: Verify that the button's label updates to match the text
    entered into the input field.

    Steps:
        1. Navigate to the Text Input page.
        2. Enter the string "ITCH" into the designated input field.
        3. Click the blue action button.
        4. Assert that the button's displayed text has changed to "ITCH".
    """
    # STEP 2: Locate the input field and enter the text "ITCH"
    text_input = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
    target_text = "ITCH"
    text_input.send_keys(target_text)

    # STEP 3: Locate and click the button to trigger the update
    updating_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
    updating_button.click()

    # STEP 4: Retrieve the updated button text and verify it
    actual_text = updating_button.text

    assert actual_text == target_text, (
        f"Text mismatch! Expected '{target_text}', but got '{actual_text}'"
    )
    print(f"Success: Button text successfully changed to '{actual_text}'")