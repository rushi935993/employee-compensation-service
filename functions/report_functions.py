import json

import azure.functions as func

from services.compensation_service import CompensationService


def get_total_bonus(req: func.HttpRequest) -> func.HttpResponse:
    try:
        service = CompensationService()
        total_bonus = service.get_total_bonus()

        return func.HttpResponse(
            json.dumps({
                "total_bonus": total_bonus
            }),
            status_code=200,
            mimetype="application/json",
        )

    except Exception:
        return func.HttpResponse(
            json.dumps({
                "error": "Internal server error."
            }),
            status_code=500,
            mimetype="application/json",
        )

def get_employees_without_bonus(
    req: func.HttpRequest,
) -> func.HttpResponse:
    try:
        service = CompensationService()
        employees = service.get_employees_without_bonus()

        return func.HttpResponse(
            json.dumps(employees),
            status_code=200,
            mimetype="application/json",
        )

    except Exception:
        return func.HttpResponse(
            json.dumps({
                "error": "Internal server error."
            }),
            status_code=500,
            mimetype="application/json",
        )

def get_bonus_percentage(
    req: func.HttpRequest,
) -> func.HttpResponse:
    try:
        service = CompensationService()
        employees = service.get_bonus_percentage()

        return func.HttpResponse(
            json.dumps(employees),
            status_code=200,
            mimetype="application/json",
        )

    except Exception:
        return func.HttpResponse(
            json.dumps({
                "error": "Internal server error."
            }),
            status_code=500,
            mimetype="application/json",
        )

def get_departments_bonus_above_average_salary(
    req: func.HttpRequest,
) -> func.HttpResponse:
    try:
        service = CompensationService()

        departments = (
            service.get_departments_bonus_above_average_salary()
        )

        return func.HttpResponse(
            json.dumps(departments),
            status_code=200,
            mimetype="application/json",
        )

    except Exception:
        return func.HttpResponse(
            json.dumps({
                "error": "Internal server error."
            }),
            status_code=500,
            mimetype="application/json",
        )

def get_bonus_ranking(
    req: func.HttpRequest,
) -> func.HttpResponse:
    try:
        service = CompensationService()
        employees = service.get_bonus_ranking()

        return func.HttpResponse(
            json.dumps(employees),
            status_code=200,
            mimetype="application/json",
        )

    except Exception:
        return func.HttpResponse(
            json.dumps({
                "error": "Internal server error."
            }),
            status_code=500,
            mimetype="application/json",
        )

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

        return func.HttpResponse(
            json.dumps({
                "highest_base_salary_employee": highest_salary,
                "highest_total_compensation_employee":
                    highest_total_compensation,
                "same_employee": same_employee,
            }),
            status_code=200,
            mimetype="application/json",
        )

    except Exception:
        return func.HttpResponse(
            json.dumps({
                "error": "Internal server error."
            }),
            status_code=500,
            mimetype="application/json",
        )