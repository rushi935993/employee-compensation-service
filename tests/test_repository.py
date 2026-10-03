from repositories.employee_repository import EmployeeRepository


def main() -> None:
    repository = EmployeeRepository()

    print("\n--- GET EMPLOYEE ---")
    employee = repository.get_employee(1)
    print(employee)

    print("\n--- LIST EMPLOYEES ---")
    employees = repository.list_employees()
    print(f"Total employees: {len(employees)}")

    for employee in employees[:3]:
        print(employee)

    print("\n--- FILTER BY DEPARTMENT ---")
    engineering = repository.list_employees(department_id=1)
    print(f"Engineering employees: {len(engineering)}")

    for employee in engineering:
        print(employee)


if __name__ == "__main__":
    main()