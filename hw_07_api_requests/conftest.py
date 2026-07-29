import pytest

from hw_07_api_requests.api.constants import BASE_URL
from hw_07_api_requests.api.employee_api import EmployeeApi


@pytest.fixture
def api() -> EmployeeApi:
    """Provide a ready-to-use EmployeeApi client for tests.

    Returns:
        EmployeeApi: Client pointed at the course's base URL.
    """
    return EmployeeApi(BASE_URL)


@pytest.fixture
def created_employee(api: EmployeeApi) -> dict:
    """Create a throwaway employee and return the API's response.

    Several tests need an existing employee to read or update, so this
    fixture centralizes creation instead of repeating it per test.

    Args:
        api: The EmployeeApi client fixture.

    Returns:
        dict: The created employee's data, including its "id".
    """
    return api.create_employee(company_id=1, name="Test Employee", position="QA Engineer")