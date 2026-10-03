from repositories.employee_repository import EmployeeRepository


class CompensationService:

    def __init__(self) -> None:
        self.repository = EmployeeRepository()

    def get_total_bonus(self) -> float:
        return self.repository.get_total_bonus()

    def get_employees_without_bonus(self) -> list[dict]:
        return self.repository.get_employees_without_bonus()

    def get_bonus_percentage(self) -> list[dict]:
        return self.repository.get_bonus_percentage()

    def get_departments_bonus_above_average_salary(self) -> list[dict]:
        return self.repository.get_departments_bonus_above_average_salary()

    def get_bonus_ranking(self) -> list[dict]:
        return self.repository.get_bonus_ranking()

    def get_highest_salary(self) -> dict | None:
        return self.repository.get_highest_salary()


    def get_highest_total_compensation(self) -> dict | None:
        return self.repository.get_highest_total_compensation()