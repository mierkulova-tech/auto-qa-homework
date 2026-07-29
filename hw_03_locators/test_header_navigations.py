"""
Module for validating the visibility and presence of header navigation elements
on the IT Career Hub main page.
"""

import time
from typing import Any, Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
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
    driver.get('https://itcareerhub.de/ru')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_check_header_elements(driver: webdriver.Chrome) -> None:
    """
    Test Case: Verify that all key header navigation elements, logos,
    and language switchers are visible on the main page.

    Steps:
        1. Accept cookie policy to prevent UI interception.
        2. Verify the visibility of the corporate logo.
        3. Verify header links: Programs, About Us, Bildungsgutschein, Reviews, and Blog.
        4. Verify language toggle buttons (RU and DE).
    """
    wait = WebDriverWait(driver, 10)
    # STEP 1: Handle cookie consent banner
    cookie_btn = driver.find_element(By.CSS_SELECTOR, ".t972__accept-btn")
    cookie_btn.click()
    time.sleep(1)

    # STEP 2: Verify ITCareerHub Corporate Logo
    logo = driver.find_element(By.CSS_SELECTOR, '#rec1921710463 .tn-atom img')
    assert logo.is_displayed(), "The ICH corporate logo is not displayed in the header."
    print("ICH Logo is displayed successfully.")

    # STEP 3: Verify Navigation Links
    # Programs Link
    program_link = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='#submenu:more']")
    assert program_link.is_displayed(), "The 'Programs' navigation link is not displayed."
    print("'Programs' link is displayed successfully.")

    # About Us Link
    about_link = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='#submenu:more2']")
    assert about_link.is_displayed(), "The 'About Us' navigation link is not displayed."
    print("'About Us' link is displayed successfully.")

    # Bildungsgutschein Link
    # Note: Fixed to target the explicit education voucher context if applicable,
    # keeping your current functional selector structure.
    bildung_link = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='#submenu:more2']")
    assert bildung_link.is_displayed(), "The 'Bildungsgutschein' navigation link is not displayed."
    print("'Bildungsgutschein' link is displayed successfully.")

    # Reviews Link
    reviews_link = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='/reviews']")
    assert reviews_link.is_displayed(), "The 'Reviews' navigation link is not displayed."
    print("'Reviews' link is displayed successfully.")

    # Blog Link
    blog_link = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 a[href='https://blog.itcareerhub.de/']")
    assert blog_link.is_displayed(), "The 'Blog' navigation link is not displayed."
    print("'Blog' link is displayed successfully.")

    # STEP 4: Verify Language Switchers
    # Russian Language Button
    ru_button = driver.find_element(By.CSS_SELECTOR, '#rec1921710463 a[href="/ru"]')
    assert ru_button.is_displayed(), "The 'RU' language switcher button is not displayed."
    print("'RU' button is displayed successfully.")

    # German Language Button
    de_button = driver.find_element(By.CSS_SELECTOR, '.tn-elem__19217104631710153064158 a')
    assert de_button.is_displayed(), "The 'DE' language switcher button is not displayed."
    print("'DE' button is displayed successfully.")