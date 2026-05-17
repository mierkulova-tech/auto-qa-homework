# HW 01 — Unit Testing with Pytest

Writing unit tests for a `SimpleMath` class using Pytest.

## Project structure

```
hw_01_unit_testing/
├── simple_math.py       ← source class SimpleMath
├── test_simple_math.py  ← unit tests
└── README.md
```

## Run tests

```bash
pytest test_simple_math.py -v
```

## What is tested

| Method      | Test cases                                                    |
|-------------|---------------------------------------------------------------|
| `square(x)` | positive, negative, zero, one, large number                   |
| `cube(x)`   | positive, negative (sign preserved!), zero, one, large number |

## Tech stack

- Python 3.x
- Pytest
