# HW 02 — Introduction to Selenium WebDriver

Automating browser interactions to capture specific UI components using Chrome.

## Project structure

```
hw_02_selenium_intro/
├── test_payment_section.py      ← automation script (Chrome + Pytest)
├── payment_methods_capture.png  ← generated artifact (screenshot)
└── README.md
```

## Run tests

```bash
pytest pytest test_payment_section.py -v -s
```

## What is tested

| Feature             | Description                                          |
|---------------------|------------------------------------------------------|
| Navigation          | Automated click on "Способы оплаты" link             |
| Element Isolation   | Locating the payment section using a unique ID       |
| Visual Verification | Capturing a screenshot of the isolated payment block |

## Tech stack

- Python 3.x
- Pytest
- Selenium WebDriver
- Google Chrome