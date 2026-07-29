import requests


from hw_07_api_requests.api.constants import CREATE_URL
from hw_07_api_requests.api.employee_api import EmployeeApi


def test_create_employee_success(api: EmployeeApi) -> None:
    """Creating an employee with valid data should return the new record."""
    name = "Harry Potter"
    position = "Junior QA Engineer"

    employee = api.create_employee(company_id=1, name=name, position=position)

    assert employee["name"] == name
    assert employee["position"] == position
    assert "id" in employee


def test_create_employee_empty_body() -> None:
    """Sending an empty body to /employee/create should be rejected with 422."""
    resp = requests.post(CREATE_URL, json={})
    assert resp.status_code == 422
    detail = resp.json()["detail"]
    assert detail[0]["msg"] == "Field required"


def test_get_employee_info(api: EmployeeApi, created_employee: dict) -> None:
    """Fetching an employee by id should return the data it was created with."""
    employee_id = created_employee["id"]
    fetched = api.get_employee(employee_id)
    assert fetched["id"] == employee_id
    assert fetched["name"] == created_employee["name"]
    assert fetched["position"] == created_employee["position"]


def test_update_employee(api: EmployeeApi, created_employee: dict) -> None:
    """Updating an employee's position should be reflected when read back."""
    employee_id = created_employee["id"]
    new_position = "Senior QA Engineer"

    updated = api.update_employee(employee_id, position=new_position)
    assert updated["position"] == new_position

    fetched = api.get_employee(employee_id)
    assert fetched["position"] == new_position