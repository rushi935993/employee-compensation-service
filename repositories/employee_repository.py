from typing import Any

from database.connection import get_connection


class EmployeeRepository:
    """Database operations for employees."""

    def create_employee(
        self,
        first_name: str,
        last_name: str,
        department_id: int,
        salary: float,
        bonus: float | None,
        hire_date: str | None,
    ) -> int:
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO Employee
                    (
                        FirstName,
                        LastName,
                        DepartmentID,
                        Salary,
                        Bonus,
                        HireDate
                    )
                OUTPUT INSERTED.EmployeeID
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    first_name,
                    last_name,
                    department_id,
                    salary,
                    bonus,
                    hire_date,
                ),
            )

            employee_id = cursor.fetchone()[0]
            connection.commit()

            return employee_id

        finally:
            connection.close()

    def get_employee(self, employee_id: int) -> dict[str, Any] | None:
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    EmployeeID,
                    FirstName,
                    LastName,
                    DepartmentID,
                    Salary,
                    Bonus,
                    HireDate
                FROM Employee
                WHERE EmployeeID = ?
                """,
                (employee_id,),
            )

            row = cursor.fetchone()

            if not row:
                return None

            return {
                "employee_id": row.EmployeeID,
                "first_name": row.FirstName,
                "last_name": row.LastName,
                "department_id": row.DepartmentID,
                "salary": float(row.Salary),
                "bonus": float(row.Bonus) if row.Bonus is not None else None,
                "hire_date": (
                    row.HireDate.isoformat()
                    if row.HireDate is not None
                    else None
                ),
            }

        finally:
            connection.close()

    def list_employees(
        self,
        department_id: int | None = None,
    ) -> list[dict[str, Any]]:
        connection = get_connection()

        try:
            cursor = connection.cursor()

            if department_id is not None:
                cursor.execute(
                    """
                    SELECT
                        EmployeeID,
                        FirstName,
                        LastName,
                        DepartmentID,
                        Salary,
                        Bonus,
                        HireDate
                    FROM Employee
                    WHERE DepartmentID = ?
                    ORDER BY EmployeeID
                    """,
                    (department_id,),
                )
            else:
                cursor.execute(
                    """
                    SELECT
                        EmployeeID,
                        FirstName,
                        LastName,
                        DepartmentID,
                        Salary,
                        Bonus,
                        HireDate
                    FROM Employee
                    ORDER BY EmployeeID
                    """
                )

            rows = cursor.fetchall()

            return [
                {
                    "employee_id": row.EmployeeID,
                    "first_name": row.FirstName,
                    "last_name": row.LastName,
                    "department_id": row.DepartmentID,
                    "salary": float(row.Salary),
                    "bonus": (
                        float(row.Bonus)
                        if row.Bonus is not None
                        else None
                    ),
                    "hire_date": (
                        row.HireDate.isoformat()
                        if row.HireDate is not None
                        else None
                    ),
                }
                for row in rows
            ]

        finally:
            connection.close()

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
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE Employee
                SET
                    FirstName = ?,
                    LastName = ?,
                    DepartmentID = ?,
                    Salary = ?,
                    Bonus = ?,
                    HireDate = ?
                WHERE EmployeeID = ?
                """,
                (
                    first_name,
                    last_name,
                    department_id,
                    salary,
                    bonus,
                    hire_date,
                    employee_id,
                ),
            )

            updated = cursor.rowcount > 0
            connection.commit()

            return updated

        finally:
            connection.close()

    def delete_employee(self, employee_id: int) -> bool:
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                DELETE FROM Employee
                WHERE EmployeeID = ?
                """,
                (employee_id,),
            )

            deleted = cursor.rowcount > 0
            connection.commit()

            return deleted

        finally:
            connection.close()

    def get_total_bonus(self) -> float:
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT COALESCE(SUM(Bonus), 0) AS TotalBonus
                FROM Employee
            """)

            row = cursor.fetchone()

            return float(row.TotalBonus) if row else 0.0

        finally:
            connection.close()


    def get_employees_without_bonus(self) -> list[dict]:
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT
                    EmployeeID,
                    FirstName,
                    LastName,
                    DepartmentID,
                    Salary,
                    Bonus,
                    HireDate
                FROM Employee
                WHERE Bonus IS NULL
                ORDER BY EmployeeID
            """)

            rows = cursor.fetchall()

            return [
                {
                    "employee_id": row.EmployeeID,
                    "first_name": row.FirstName,
                    "last_name": row.LastName,
                    "department_id": row.DepartmentID,
                    "salary": float(row.Salary),
                    "bonus": None,
                    "hire_date": (
                        row.HireDate.isoformat()
                        if row.HireDate is not None
                        else None
                    ),
                }
                for row in rows
            ]

        finally:
            connection.close()

    def get_bonus_percentage(self) -> list[dict]:
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT
                    EmployeeID,
                    FirstName,
                    LastName,
                    DepartmentID,
                    Salary,
                    Bonus,
                    ROUND(
                        COALESCE(Bonus, 0) * 100.0 / NULLIF(Salary, 0),
                        2
                    ) AS BonusPercentage
                FROM Employee
                ORDER BY EmployeeID
            """)

            rows = cursor.fetchall()

            return [
                {
                    "employee_id": row.EmployeeID,
                    "first_name": row.FirstName,
                    "last_name": row.LastName,
                    "department_id": row.DepartmentID,
                    "salary": float(row.Salary),
                    "bonus": (
                        float(row.Bonus)
                        if row.Bonus is not None
                        else None
                    ),
                    "bonus_percentage": (
                        float(row.BonusPercentage)
                        if row.BonusPercentage is not None
                        else 0.0
                    ),
                }
                for row in rows
            ]

        finally:
            connection.close()

    def get_departments_bonus_above_average_salary(self) -> list[dict]:
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT
                    d.DepartmentID,
                    d.DepartmentName,
                    SUM(COALESCE(e.Bonus, 0)) AS TotalBonus,
                    AVG(e.Salary) AS AverageSalary
                FROM Department d
                INNER JOIN Employee e
                    ON d.DepartmentID = e.DepartmentID
                GROUP BY
                    d.DepartmentID,
                    d.DepartmentName
                HAVING
                    SUM(COALESCE(e.Bonus, 0)) > AVG(e.Salary)
                ORDER BY d.DepartmentID
            """)

            rows = cursor.fetchall()

            return [
                {
                    "department_id": row.DepartmentID,
                    "department_name": row.DepartmentName,
                    "total_bonus": float(row.TotalBonus),
                    "average_salary": float(row.AverageSalary),
                }
                for row in rows
            ]

        finally:
            connection.close()

    def get_bonus_ranking(self) -> list[dict]:
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT
                    EmployeeID,
                    FirstName,
                    LastName,
                    DepartmentID,
                    Salary,
                    Bonus,
                    HireDate
                FROM Employee
                ORDER BY
                    CASE
                        WHEN Bonus IS NULL THEN 1
                        ELSE 0
                    END,
                    Bonus DESC
            """)

            rows = cursor.fetchall()

            return [
                {
                    "employee_id": row.EmployeeID,
                    "first_name": row.FirstName,
                    "last_name": row.LastName,
                    "department_id": row.DepartmentID,
                    "salary": float(row.Salary),
                    "bonus": (
                        float(row.Bonus)
                        if row.Bonus is not None
                        else None
                    ),
                    "hire_date": (
                        row.HireDate.isoformat()
                        if row.HireDate is not None
                        else None
                    ),
                }
                for row in rows
            ]

        finally:
            connection.close()

    def get_highest_salary(self) -> dict | None:
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT TOP 1
                    EmployeeID,
                    FirstName,
                    LastName,
                    DepartmentID,
                    Salary,
                    Bonus,
                    HireDate
                FROM Employee
                ORDER BY Salary DESC, EmployeeID
            """)

            row = cursor.fetchone()

            if not row:
                return None

            return {
                "employee_id": row.EmployeeID,
                "first_name": row.FirstName,
                "last_name": row.LastName,
                "department_id": row.DepartmentID,
                "salary": float(row.Salary),
                "bonus": (
                    float(row.Bonus)
                    if row.Bonus is not None
                    else None
                ),
                "hire_date": (
                    row.HireDate.isoformat()
                    if row.HireDate is not None
                    else None
                ),
            }

        finally:
            connection.close()

    def get_highest_total_compensation(self) -> dict | None:
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT TOP 1
                    EmployeeID,
                    FirstName,
                    LastName,
                    DepartmentID,
                    Salary,
                    Bonus,
                    HireDate,
                    Salary + COALESCE(Bonus, 0) AS TotalCompensation
                FROM Employee
                ORDER BY
                    Salary + COALESCE(Bonus, 0) DESC,
                    EmployeeID
            """)

            row = cursor.fetchone()

            if not row:
                return None

            return {
                "employee_id": row.EmployeeID,
                "first_name": row.FirstName,
                "last_name": row.LastName,
                "department_id": row.DepartmentID,
                "salary": float(row.Salary),
                "bonus": (
                    float(row.Bonus)
                    if row.Bonus is not None
                    else None
                ),
                "total_compensation": float(row.TotalCompensation),
                "hire_date": (
                    row.HireDate.isoformat()
                    if row.HireDate is not None
                    else None
                ),
            }

        finally:
            connection.close()