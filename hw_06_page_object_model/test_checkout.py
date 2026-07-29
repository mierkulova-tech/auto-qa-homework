"""
HW 06 — Page Object Model: SauceDemo end-to-end checkout test.
"""
from selenium import webdriver
from imports import LoginPage, InventoryPage, CartPage, CheckoutInfoPage, CheckoutOverviewPage
from constants import USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, POSTAL_CODE, PRODUCTS, EXPECTED_TOTAL

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