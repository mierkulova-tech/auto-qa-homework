"""
Module for testing the main navigation and callback functionality
on the IT Career Hub website.
"""

import time
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
    Fixture to initialize and configure the WebDriver instance before each test,
    and safely close it after the test execution is completed.

    Yields:
        webdriver.Chrome: The configured Chrome WebDriver instance.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://itcareerhub.de/ru')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_navigation_about_to_contacts(driver: webdriver.Chrome) -> None:
    """
    Test Case: Verify navigation from 'About Us' to 'Contacts' page
    and validate the functionality of the Callback Popup.

    Steps:
        1. Accept cookie policy.
        2. Click on 'About Us' section to open the submenu.
        3. Click on 'Contacts' link in the submenu.
        4. Verify that the URL changed to the contacts page.
        5. Scroll down to the 'CALLBACK' button.
        6. Click the 'CALLBACK' button via JavaScript to avoid element interception.
        7. Verify that the modal window opens and contains the expected text.
    """
    wait = WebDriverWait(driver, 10)

    # STEP 1: Accept cookies to clear the overlay
    cookie_btn = driver.find_element(By.CSS_SELECTOR, ".t972__accept-btn")
    cookie_btn.click()
    time.sleep(1)

    # STEP 2: Click on the "About Us" section to trigger the dropdown menu
    about_us_menu = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='#submenu:more2']")
    about_us_menu.click()
    time.sleep(2)

    # STEP 3: Click on the "Contacts" link inside the dropdown menu
    contacts_link = driver.find_element(By.CSS_SELECTOR, "div.t794__content a[href*='contact-us']")
    contacts_link.click()
    time.sleep(2)

    # ASSERTION 1: Verify successful navigation to the Contacts page
    assert "/contact-us" in driver.current_url, (
        f"Expected '/contact-us' to be in the URL, but got '{driver.current_url}'"
    )
    print("Successfully navigated to the Contacts page.")
    time.sleep(3)

    # STEP 4: Locate the "CALLBACK" button and scroll it into view
    callback_btn = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'ОБРАТНЫЙ ЗВОНОК')))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", callback_btn)
    time.sleep(1)
    print("Scrolled down to the Callback button.")

    # STEP 5: Click the "CALLBACK" button using JavaScript to bypass overlapping layers
    driver.execute_script("arguments[0].click();", callback_btn)
    print("Successfully clicked the Callback button.")
    time.sleep(2)

    # STEP 6: Verify the modal window content
    expected_text = "Запишитесь на бесплатную карьерную консультацию"
    text_message_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[field='tn_text_175871291756015470']"))
    )

    # ASSERTION 2: Verify the text element is visible and contains the expected message
    assert text_message_element.is_displayed(), "The callback modal text is not displayed."
    assert expected_text in text_message_element.text, (
        f"Expected text '{expected_text}' not found in the modal. Actual text: '{text_message_element.text}'"
    )
    print(f"Validation successful. Text found: '{text_message_element.text}'")