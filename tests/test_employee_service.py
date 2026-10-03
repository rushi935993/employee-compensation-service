from services.employee_service import EmployeeService


def main() -> None:
    service = EmployeeService()

    print("\n--- GET EMPLOYEE ---")
    employee = service.get_employee(1)
    print(employee)

    print("\n--- LIST EMPLOYEES ---")
    employees = service.list_employees()
    print(f"Total employees: {len(employees)}")

    print("\n--- DEPARTMENT FILTER ---")
    employees = service.list_employees(department_id=1)
    print(f"Engineering employees: {len(employees)}")

    print("\n--- VALIDATION TEST ---")

    try:
        service.get_employee(0)
    except ValueError as error:
        print(f"Validation caught: {error}")

    try:
        service.create_employee(
            first_name="",
            last_name="Test",
            department_id=1,
            salary=500000,
            bonus=None,
            hire_date="2026-01-01",
        )
    except ValueError as error:
        print(f"Validation caught: {error}")

    try:
        service.create_employee(
            first_name="Test",
            last_name="Employee",
            department_id=1,
            salary=-100,
            bonus=None,
            hire_date="2026-01-01",
        )
    except ValueError as error:
        print(f"Validation caught: {error}")


if __name__ == "__main__":
    main()