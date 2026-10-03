import azure.functions as func

from functions.employee_functions import (
    create_employee,
    get_employee,
    list_employees,
    update_employee,
    delete_employee,
)
from functions.report_functions import (
    get_total_bonus,
    get_employees_without_bonus,
    get_bonus_percentage,
    get_departments_bonus_above_average_salary,
    get_bonus_ranking,
    get_highest_salary,
)
app = func.FunctionApp()


@app.route(
    route="health",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def health(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        body='{"status":"ok","service":"employee-compensation-service"}',
        status_code=200,
        mimetype="application/json",
    )


@app.route(
    route="employees",
    methods=["POST"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def create_employee_function(req: func.HttpRequest) -> func.HttpResponse:
    return create_employee(req)


@app.route(
    route="employees/{employee_id}",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def get_employee_function(req: func.HttpRequest) -> func.HttpResponse:
    return get_employee(req)

@app.route(
    route="employees",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def list_employees_function(req: func.HttpRequest) -> func.HttpResponse:
    return list_employees(req)

@app.route(
    route="employees/{employee_id}",
    methods=["PUT"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def update_employee_function(req: func.HttpRequest) -> func.HttpResponse:
    return update_employee(req)

@app.route(
    route="employees/{employee_id}",
    methods=["DELETE"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def delete_employee_function(req: func.HttpRequest) -> func.HttpResponse:
    return delete_employee(req)

@app.route(
    route="reports/total-bonus",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def total_bonus_function(req: func.HttpRequest) -> func.HttpResponse:
    return get_total_bonus(req)

@app.route(
    route="reports/no-bonus",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def no_bonus_function(req: func.HttpRequest) -> func.HttpResponse:
    return get_employees_without_bonus(req)

@app.route(
    route="reports/bonus-percentage",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def bonus_percentage_function(
    req: func.HttpRequest,
) -> func.HttpResponse:
    return get_bonus_percentage(req)

@app.route(
    route="reports/departments-bonus-above-average-salary",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def departments_bonus_above_average_salary_function(
    req: func.HttpRequest,
) -> func.HttpResponse:
    return get_departments_bonus_above_average_salary(req)

@app.route(
    route="reports/bonus-ranking",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def bonus_ranking_function(req: func.HttpRequest) -> func.HttpResponse:
    return get_bonus_ranking(req)

@app.route(
    route="reports/highest-salary",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def highest_salary_function(req: func.HttpRequest) -> func.HttpResponse:
    return get_highest_salary(req)