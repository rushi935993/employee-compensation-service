import pytest

from services.employee_service import EmployeeService


def test_get_employee():
    service = EmployeeService()

    employee = service.get_employee(1)

    assert employee is not None
    assert employee["employee_id"] == 1
    assert employee["first_name"] == "Aarav"
    assert employee["last_name"] == "Sharma"


def test_get_nonexistent_employee():
    service = EmployeeService()

    employee = service.get_employee(999999)

    assert employee is None


def test_list_all_employees():
    service = EmployeeService()

    employees = service.list_employees()

    assert isinstance(employees, list)
    assert len(employees) >= 12


def test_department_filter():
    service = EmployeeService()

    employees = service.list_employees(department_id=1)

    assert isinstance(employees, list)

    for employee in employees:
        assert employee["department_id"] == 1


def test_invalid_employee_id():
    service = EmployeeService()

    with pytest.raises(ValueError):
        service.get_employee(0)


def test_negative_salary():
    service = EmployeeService()

    with pytest.raises(ValueError):
        service.create_employee(
            first_name="Test",
            last_name="User",
            department_id=1,
            salary=-100,
            bonus=None,
            hire_date=None,
        )


def test_missing_first_name():
    service = EmployeeService()

    with pytest.raises(ValueError):
        service.create_employee(
            first_name="",
            last_name="User",
            department_id=1,
            salary=500000,
            bonus=None,
            hire_date=None,
        )