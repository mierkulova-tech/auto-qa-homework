"""Employee API module - helper class wrapping the Employee Management API.

Mirrors the CompanyApi pattern from the course lesson: one method
per endpoint, each method asserts the expected status code and returns the
parsed JSON body, so tests stay short and readable.
"""

from typing import Any

import requests

from .constants import (
    ADMIN_PASSWORD,
    ADMIN_USERNAME,
    CHANGE_URL,
    CREATE_URL,
    INFO_URL,
    LOGIN_URL,
)


class EmployeeApi:
    """Helper class for interacting with the Employee Management API."""

    def __init__(self, url: str) -> None:
        """Initialize the client with the API's base URL.

        Args:
            url: Base URL of the API, e.g. "http://5.101.50.27:8000".
        """
        self.url = url

    def get_token(
            self, username: str = ADMIN_USERNAME, password: str = ADMIN_PASSWORD
    ) -> str:
        """Authenticate and return a client token.

        Args:
            username: Login username. Defaults to the course admin account.
            password: Login password. Defaults to the course admin account.

        Returns:
            The ``user_token`` string returned by ``POST /auth/login``.
        """
        creds = {"username": username, "password": password}
        resp = requests.post(LOGIN_URL, json=creds)
        assert resp.status_code == 200, (
            f"Login failed: expected 200, got {resp.status_code} ({resp.text})"
        )
        return resp.json()["user_token"]

    def create_employee(
            self, company_id: int, name: str, position: str
    ) -> dict[str, Any]:
        """Create a new employee.

        Args:
            company_id: ID of the company the employee belongs to.
                ASSUMPTION: employees are scoped to a company, mirroring how
                the lesson describes "get the list of a company's employees".
                Confirm this field name once /docs is reachable.
            name: Employee's full name.
            position: Employee's job title.

        Returns:
            The created employee as returned by the API (expected to include
            its new "id").
        """
        payload = {"company_id": company_id, "name": name, "position": position}
        resp = requests.post(CREATE_URL, json=payload)
        assert resp.status_code == 201, (
            f"Expected 201, got {resp.status_code} ({resp.text})"
        )
        return resp.json()

    def get_employee(self, employee_id: int) -> dict[str, Any]:
        """Retrieve information about an employee by ID.

        Args:
            employee_id: The ID of the employee to look up.
                ASSUMPTION: passed as a query parameter (?id=...), since the
                homework's URL has no {id} path segment, unlike /company/{id}.

        Returns:
            The employee's data as returned by the API.
        """
        resp = requests.get(INFO_URL, params={"id": employee_id})
        assert resp.status_code == 200, (
            f"Expected 200, got {resp.status_code} ({resp.text})"
        )
        return resp.json()

    def update_employee(self, employee_id: int, **fields: Any) -> dict[str, Any]:
        """Update an existing employee's data.

        Args:
            employee_id: The ID of the employee to update.
            **fields: Fields to update (e.g. name="...", position="...").
                ASSUMPTION: like /company/update/{id}, this endpoint likely
                requires a client_token query param to identify who is
                making the change.

        Returns:
            The updated employee as returned by the API.
        """
        client_token = self.get_token()
        resp = requests.patch(
            CHANGE_URL,
            params={"id": employee_id, "client_token": client_token},
            json=fields,
        )
        assert resp.status_code == 200, (
            f"Expected 200, got {resp.status_code} ({resp.text})"
        )
        return resp.json()