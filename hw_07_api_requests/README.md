# HW 07 — API Testing with Requests

API tests for the Employee module of the course's X-Clients training server,
using an `EmployeeApi` helper class (Page-Object-style, same idea as the
`pages/` classes in hw_06).

## Project structure

```
hw_07_api_requests/
├── api/
│   ├── __init__.py
│   ├──employee_api.py     ← EmployeeApi helper class
│   └── constants.py
├── conftest.py
├── test_employee_api.py
├── mock_server.py
└── README.md
```

## Run tests

```bash
pytest hw_07_api_requests/test_employee_api.py -v
```

## What is tested

| Test | Description                                                                    |
| :--- |:-------------------------------------------------------------------------------|
| **test_create_employee_success** | `POST /employee/create` returns the new employee with matching fields.         |
| **test_create_employee_empty_body** | Negative test: empty JSON body returns `422` with `"Field required"`.          |
| **test_get_employee_info** | `GET /employee/info?id=` returns the same data the employee was created with.   |
| **test_update_employee** | `PATCH /employee/change` updates a field, and the change persists on re-fetch. |

## Tech stack

- Python 3.x
- Pytest
- Requests
- Flask