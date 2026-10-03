from services.compensation_service import CompensationService


def test_total_bonus():
    service = CompensationService()

    total_bonus = service.get_total_bonus()

    assert total_bonus == 1090000.0


def test_employees_without_bonus():
    service = CompensationService()

    employees = service.get_employees_without_bonus()

    assert isinstance(employees, list)
    assert len(employees) > 0

    for employee in employees:
        assert employee["bonus"] is None


def test_bonus_percentage():
    service = CompensationService()

    employees = service.get_bonus_percentage()

    assert isinstance(employees, list)
    assert len(employees) > 0

    aarav = next(
        employee
        for employee in employees
        if employee["employee_id"] == 1
    )

    assert aarav["bonus_percentage"] == 12.5


def test_departments_bonus_above_average_salary():
    service = CompensationService()

    departments = (
        service.get_departments_bonus_above_average_salary()
    )

    assert isinstance(departments, list)
    assert len(departments) > 0

    sales = next(
        department
        for department in departments
        if department["department_id"] == 5
    )

    assert sales["department_name"] == "Sales"
    assert sales["total_bonus"] == 350000.0
    assert sales["average_salary"] == 110000.0


def test_bonus_ranking():
    service = CompensationService()

    employees = service.get_bonus_ranking()

    assert isinstance(employees, list)
    assert len(employees) > 0

    non_null_bonuses = [
        employee["bonus"]
        for employee in employees
        if employee["bonus"] is not None
    ]

    assert non_null_bonuses == sorted(
        non_null_bonuses,
        reverse=True,
    )

    null_bonus_started = False

    for employee in employees:
        if employee["bonus"] is None:
            null_bonus_started = True
        else:
            assert not null_bonus_started


def test_highest_salary():
    service = CompensationService()

    employee = service.get_highest_salary()

    assert employee is not None
    assert employee["employee_id"] == 10
    assert employee["first_name"] == "Anjali"
    assert employee["salary"] == 1200000.0


def test_highest_total_compensation():
    service = CompensationService()

    employee = service.get_highest_total_compensation()

    assert employee is not None
    assert employee["employee_id"] == 6
    assert employee["first_name"] == "Sneha"
    assert employee["total_compensation"] == 1300000.0