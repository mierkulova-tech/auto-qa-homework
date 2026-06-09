# HW 05 — Advanced Selenium II: iFrames & Drag and Drop

![Homework Preview](../assets/hw_05_preview.png)
Testing advanced browser interactions: switching into iframe contexts and performing drag-and-drop operations.

## Project structure

```
hw_05_selenium_advanced_2/
├── test_iframe_text.py    ← iframe context switch and text validation
├── test_drag_and_drop.py  ← drag photo to trash and verify counts
└── README.md
```

## Run tests

```bash
# Run all tests in the directory
pytest hw_05_selenium_advanced_2/ -v -s

# Run a specific test file
pytest test_iframe_text.py -v -s
pytest test_drag_and_drop.py -v -s
```

## What is tested

| Feature | Description |
| :--- | :--- |
| **iFrame Switch** | Locating an iframe, switching WebDriver context into it, and validating the presence of specific paragraph text. |
| **Drag & Drop** | Grabbing the first photo in a gallery and dragging it to a Trash area via JavaScript event simulation. |
| **Count Validation** | Verifying that after the drop: Trash contains 1 photo and the gallery retains exactly 3 photos. |

## Tech stack

- Python 3.x
- Pytest
- Selenium WebDriver
- Chrome WebDriver (Automated via Selenium Manager)
