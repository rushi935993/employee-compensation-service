import json

import azure.functions as func

from services.compensation_service import CompensationService
from utils.http_response import error_response, json_response

def get_total_bonus(req: func.HttpRequest) -> func.HttpResponse:
    try:
        service = CompensationService()
        total_bonus = service.get_total_bonus()

        return json_response(
            {
                "total_bonus": total_bonus
            }
        )

    except Exception:
        return error_response("Internal server error.", 500)

def get_employees_without_bonus(
    req: func.HttpRequest,
) -> func.HttpResponse:
    try:
        service = CompensationService()
        employees = service.get_employees_without_bonus()

        return json_response(employees)

    except Exception:
        return error_response("Internal server error.", 500)

def get_bonus_percentage(
    req: func.HttpRequest,
) -> func.HttpResponse:
    try:
        service = CompensationService()
        employees = service.get_bonus_percentage()

        return json_response(employees)

    except Exception:
        return error_response("Internal server error.", 500)

def get_departments_bonus_above_average_salary(
    req: func.HttpRequest,
) -> func.HttpResponse:
    try:
        service = CompensationService()

        departments = (
            service.get_departments_bonus_above_average_salary()
        )

        return json_response(departments)

    except Exception:
        return error_response("Internal server error.", 500)

def get_bonus_ranking(
    req: func.HttpRequest,
) -> func.HttpResponse:
    try:
        service = CompensationService()
        employees = service.get_bonus_ranking()

        return json_response(employees)

    except Exception:
        return error_response("Internal server error.", 500)

def get_highest_salary(
    req: func.HttpRequest,
) -> func.HttpResponse:
    try:
        service = CompensationService()

        highest_salary = service.get_highest_salary()
        highest_total_compensation = (
            service.get_highest_total_compensation()
        )

        same_employee = (
            highest_salary is not None
            and highest_total_compensation is not None
            and highest_salary["employee_id"]
            == highest_total_compensation["employee_id"]
        )

        return json_response(
            {
                "highest_base_salary_employee": highest_salary,
                "highest_total_compensation_employee":
                    highest_total_compensation,
                "same_employee": same_employee,
            }
        )

    except Exception:
        return error_response("Internal server error.", 500)