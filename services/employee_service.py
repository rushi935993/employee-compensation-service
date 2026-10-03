from datetime import date
from typing import Any

from repositories.employee_repository import EmployeeRepository


class EmployeeService:
    """Business logic and validation for employee operations."""

    def __init__(self) -> None:
        self.repository = EmployeeRepository()

    def create_employee(
        self,
        first_name: str,
        last_name: str,
        department_id: int,
        salary: float,
        bonus: float | None,
        hire_date: str | None,
    ) -> int:

        self._validate_employee_data(
            first_name=first_name,
            last_name=last_name,
            department_id=department_id,
            salary=salary,
            bonus=bonus,
            hire_date=hire_date,
        )

        return self.repository.create_employee(
            first_name=first_name.strip(),
            last_name=last_name.strip(),
            department_id=department_id,
            salary=salary,
            bonus=bonus,
            hire_date=hire_date,
        )

    def get_employee(self, employee_id: int) -> dict[str, Any] | None:
        self._validate_employee_id(employee_id)

        return self.repository.get_employee(employee_id)

    def list_employees(
        self,
        department_id: int | None = None,
    ) -> list[dict[str, Any]]:

        if department_id is not None:
            self._validate_positive_integer(
                department_id,
                "department_id",
            )

        return self.repository.list_employees(department_id)

    def update_employee(
        self,
        employee_id: int,
        first_name: str,
        last_name: str,
        department_id: int,
        salary: float,
        bonus: float | None,
        hire_date: str | None,
    ) -> bool:

        self._validate_employee_id(employee_id)

        self._validate_employee_data(
            first_name=first_name,
            last_name=last_name,
            department_id=department_id,
            salary=salary,
            bonus=bonus,
            hire_date=hire_date,
        )

        return self.repository.update_employee(
            employee_id=employee_id,
            first_name=first_name.strip(),
            last_name=last_name.strip(),
            department_id=department_id,
            salary=salary,
            bonus=bonus,
            hire_date=hire_date,
        )

    def delete_employee(self, employee_id: int) -> bool:
        self._validate_employee_id(employee_id)

        return self.repository.delete_employee(employee_id)

    @staticmethod
    def _validate_employee_id(employee_id: int) -> None:
        if not isinstance(employee_id, int) or employee_id <= 0:
            raise ValueError("employee_id must be a positive integer.")

    @staticmethod
    def _validate_positive_integer(
        value: int,
        field_name: str,
    ) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError(
                f"{field_name} must be a positive integer."
            )

    @staticmethod
    def _validate_employee_data(
        first_name: str,
        last_name: str,
        department_id: int,
        salary: float,
        bonus: float | None,
        hire_date: str | None,
    ) -> None:

        if not first_name or not first_name.strip():
            raise ValueError("First name is required.")

        if not last_name or not last_name.strip():
            raise ValueError("Last name is required.")

        if len(first_name.strip()) > 50:
            raise ValueError(
                "First name must not exceed 50 characters."
            )

        if len(last_name.strip()) > 50:
            raise ValueError(
                "Last name must not exceed 50 characters."
            )

        EmployeeService._validate_positive_integer(
            department_id,
            "department_id",
        )

        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        if bonus is not None and bonus < 0:
            raise ValueError("Bonus cannot be negative.")

        if hire_date is not None:
            try:
                date.fromisoformat(hire_date)
            except ValueError as exc:
                raise ValueError(
                    "hire_date must use YYYY-MM-DD format."
                ) from exc