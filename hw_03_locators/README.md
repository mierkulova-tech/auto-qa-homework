# HW 03 — Advanced Locators and Navigation

<p align="center">
  <img src="assets/hw_03_preview.png" alt="Project Structure Preview" width="800">
</p>


Comprehensive automated testing of the IT Career Hub website, focusing on complex navigation, language switching, and interactive UI elements.

## Project structure

```
hw_03_locators/
├── test_callback_navigation.py  ← navigation and modal window validation
├── test_header_navigations.py   ← visibility check for all header links
├── test_switch_languages.py     ← language toggle logic (RU/DE)
└── README.md
```

## Run tests

```bash
# Run all tests in the directory
pytest hw_03_locators/ -v -s

# Run a specific test file
pytest test_callback_navigation.py -v
```

## What is tested

| Feature | Description |
| :--- | :--- |
| **Header Elements** | Presence check for Logo, Programs, About Us, Contacts, Reviews, and Blog links. |
| **Navigation** | Multi-step transition: Main Menu → "About Us" dropdown → "Contacts" page. |
| **Callback Form** | Interaction with the "CALLBACK" button using JavaScript to bypass element interception and verification of the modal window text. |
| **Localization** | Switching between Russian and German languages with validation of both the URL and the main `<h1>` header content. |

## Tech stack

- Python 3.x
- Pytest
- Selenium WebDriver
- Chrome WebDriver (Automated via Selenium Manager)
