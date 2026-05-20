"""
Module for testing language switching functionality between Russian and German
on the IT Career Hub website.
"""

import time
from typing import Any, Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver() -> Generator[WebDriver, Any, None]:
    """
    Fixture to initialize, configure, and tear down the Chrome WebDriver instance.

    Yields:
        webdriver.Chrome: The configured Chrome WebDriver instance.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://itcareerhub.de/ru')
    yield driver
    driver.quit()


def test_switch_languages_button(driver: webdriver.Chrome) -> None:
    """
    Test Case: Verify seamless language switching from Russian to German and back.

    Steps:
        1. Accept cookie policy to clear the viewport.
        2. Click the German language toggle button (DE).
        3. Verify the German URL and validate the presence of the German H1 heading.
        4. Click the Russian language toggle button (RU) on the German page.
        5. Verify the Russian URL and validate the presence of the Russian H1 heading.
    """
    wait = WebDriverWait(driver, 10)

    # STEP 1: Handle cookie consent banner
    cookie_btn = driver.find_element(By.CSS_SELECTOR, ".t972__accept-btn")
    cookie_btn.click()
    time.sleep(1)

    # STEP 2: Locate and click the German language switch button (DE)
    de_button = driver.find_element(By.CSS_SELECTOR, '.tn-elem__19217104631710153064158 a')
    de_button.click()

    # Wait until the URL changes to the German home page
    wait.until(EC.url_to_be("https://itcareerhub.de/"))

    # STEP 3: Verify German URL and main heading content
    assert driver.current_url == "https://itcareerhub.de/", (
        f"Expected URL to be 'https://itcareerhub.de/', but got '{driver.current_url}'"
    )

    heading_de = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
    expected_de_text = "Erwerben Sie einen gefragten IT-Beruf und starten Sie Ihre Karriere in Deutschland"

    assert expected_de_text in heading_de.text, (
        f"Expected German heading text not found. Actual: '{heading_de.text}'"
    )
    print("Successfully switched to German: Heading and URL are verified.")
    time.sleep(2)

    # STEP 4: Switch back to Russian
    ru_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="/ru"]'))
    )
    driver.execute_script("arguments[0].click();", ru_button)

    # Wait until the URL changes back to the Russian version
    wait.until(EC.url_contains("/ru"))

    # STEP 5: Verify Russian URL and final main heading content
    current_url_stripped = driver.current_url.strip()
    assert "itcareerhub.de/ru" in current_url_stripped, (
        f"Expected 'itcareerhub.de/ru' to be in URL, but got '{current_url_stripped}'"
    )

    heading_final = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))

    # FIXED: Updated the expected string to match the live website content
    expected_ru_text = "Освойте актуальные цифровые профессии в Германии"
    assert expected_ru_text in heading_final.text, (
        f"Expected Russian heading text not found. Actual: '{heading_final.text}'"
    )
    print("Successfully switched back to Russian: Heading and URL are verified.")