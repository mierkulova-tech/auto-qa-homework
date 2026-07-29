# HW 06 — Page Object Model

![Homework Preview](../assets/hw_06_preview.png)

End-to-end checkout test for [SauceDemo](https://www.saucedemo.com/) using the Page Object Model pattern.

## Project structure

```
hw_06_page_object_model/
├── pages/
│   ├── __init__.py
│   ├── base_page.py             ← shared WebDriver interaction methods
│   ├── login_page.py            ← login form
│   ├── inventory_page.py        ← product catalogue and cart actions
│   ├── cart_page.py             ← cart review and checkout navigation
│   ├── checkout_info_page.py    ← personal information form
│   └── checkout_overview_page.py ← order summary and total price
├── constants.py          
├── conftest.py          
├── imports.py 
├── test_checkout.py             ← end-to-end test
└── README.md
```

## Run tests

```bash
pytest test_checkout.py -v -s
```

## What is tested

| Step | Description |
| :--- | :--- |
| **Login** | Authenticate as `standard_user` on SauceDemo. |
| **Add to Cart** | Add Sauce Labs Backpack, Bolt T-Shirt, and Onesie. |
| **Cart Validation** | Assert 3 items are present before proceeding. |
| **Checkout Form** | Fill in first name, last name, and postal code. |
| **Total Assertion** | Read the summary total and verify it equals `$58.29`. |

## Tech stack

- Python 3.x
- Pytest
- Selenium WebDriver
- Chrome WebDriver (Automated via Selenium Manager)
