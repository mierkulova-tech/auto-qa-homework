"""
HW 06 — Page Object Model: SauceDemo end-to-end checkout test.
"""

from typing import Any, Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage


# --- Constants ---
BASE_URL      = "https://www.saucedemo.com/"
USERNAME      = "standard_user"
PASSWORD      = "secret_sauce"
FIRST_NAME    = "Olena"
LAST_NAME     = "Mierkulova"
POSTAL_CODE   = "20095"
PRODUCTS      = [
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Onesie",
]
EXPECTED_TOTAL = "Total: $58.29"


# --- Fixture ---
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


# --- Test ---
def test_checkout_total(driver: webdriver.Chrome) -> None:
    """
    Test Case: Complete an end-to-end checkout flow and verify the order total.

    Steps:
        1. Log in as standard_user.
        2. Add Sauce Labs Backpack, Bolt T-Shirt, and Onesie to the cart.
        3. Navigate to the cart and verify item count.
        4. Proceed to checkout and fill in the personal information form.
        5. Wait for the overview page to load.
        6. Read the total price from the order summary page.
        7. Assert the total equals $58.29.
    """
    # STEP 1: Log in
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)
    print(f"Logged in as '{USERNAME}'.")

    # STEP 2: Add products to cart
    inventory_page = InventoryPage(driver)
    for product in PRODUCTS:
        inventory_page.add_product(product)

    # STEP 3: Go to cart and verify item count
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 3, "Expected 3 items in cart before checkout."
    assert "cart" in driver.current_url

    # STEP 4: Proceed to checkout and fill form
    cart_page.proceed_to_checkout()
    assert "checkout-step-one" in driver.current_url

    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.fill_form(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout_info_page.continue_to_overview()

    # STEP 5: Wait for overview page
    overview_page = CheckoutOverviewPage(driver)
    overview_page.wait_for_overview_page()

    # STEP 6–7: Read total and assert
    actual_total = overview_page.get_total()
    assert actual_total == EXPECTED_TOTAL, (
        f"Total mismatch!\n"
        f"Expected: '{EXPECTED_TOTAL}'\n"
        f"Actual:   '{actual_total}'"
    )
    print(f"Test passed. Order total verified: '{actual_total}'")