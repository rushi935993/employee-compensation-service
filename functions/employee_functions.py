import json

import azure.functions as func

from services.employee_service import EmployeeService


def create_employee(req: func.HttpRequest) -> func.HttpResponse:
    """Create a new employee."""

    try:
        body = req.get_json()

        required_fields = [
            "first_name",
            "last_name",
            "department_id",
            "salary",
        ]

        missing_fields = [
            field
            for field in required_fields
            if field not in body
        ]

        if missing_fields:
            return func.HttpResponse(
                json.dumps(
                    {
                        "error": "Missing required fields.",
                        "fields": missing_fields,
                    }
                ),
                status_code=400,
                mimetype="application/json",
            )

        service = EmployeeService()

        employee_id = service.create_employee(
            first_name=body["first_name"],
            last_name=body["last_name"],
            department_id=int(body["department_id"]),
            salary=float(body["salary"]),
            bonus=(
                float(body["bonus"])
                if body.get("bonus") is not None
                else None
            ),
            hire_date=body.get("hire_date"),
        )

        return func.HttpResponse(
            json.dumps(
                {
                    "message": "Employee created successfully.",
                    "employee_id": employee_id,
                }
            ),
            status_code=201,
            mimetype="application/json",
        )

    except ValueError as error:
        return func.HttpResponse(
            json.dumps({"error": str(error)}),
            status_code=400,
            mimetype="application/json",
        )

    except (TypeError, KeyError):
        return func.HttpResponse(
            json.dumps(
                {
                    "error": "Invalid request body."
                }
            ),
            status_code=400,
            mimetype="application/json",
        )

    except Exception:
        return func.HttpResponse(
            json.dumps(
                {
                    "error": "Internal server error."
                }
            ),
            status_code=500,
            mimetype="application/json",
        )   

def get_employee(req: func.HttpRequest) -> func.HttpResponse:
    try:
        employee_id = int(req.route_params.get("employee_id"))

        service = EmployeeService()
        employee = service.get_employee(employee_id)

        if employee is None:
            return func.HttpResponse(
                json.dumps({
                    "error": "Employee not found."
                }),
                status_code=404,
                mimetype="application/json",
            )

        return func.HttpResponse(
            json.dumps(employee),
            status_code=200,
            mimetype="application/json",
        )

    except ValueError as error:
        return func.HttpResponse(
            json.dumps({"error": str(error)}),
            status_code=400,
            mimetype="application/json",
        )

    except (TypeError, KeyError):
        return func.HttpResponse(
            json.dumps({"error": "Invalid employee ID."}),
            status_code=400,
            mimetype="application/json",
        )

    except Exception:
        return func.HttpResponse(
            json.dumps({"error": "Internal server error."}),
            status_code=500,
            mimetype="application/json",
        )

def list_employees(req: func.HttpRequest) -> func.HttpResponse:
    try:
        department_id = req.params.get("departmentId")

        if department_id is not None:
            department_id = int(department_id)

        service = EmployeeService()
        employees = service.list_employees(department_id)

        return func.HttpResponse(
            json.dumps(employees),
            status_code=200,
            mimetype="application/json",
        )

    except ValueError as error:
        return func.HttpResponse(
            json.dumps({"error": str(error)}),
            status_code=400,
            mimetype="application/json",
        )

    except (TypeError, KeyError):
        return func.HttpResponse(
            json.dumps({"error": "Invalid department ID."}),
            status_code=400,
            mimetype="application/json",
        )

    except Exception:
        return func.HttpResponse(
            json.dumps({"error": "Internal server error."}),
            status_code=500,
            mimetype="application/json",
        )

def update_employee(req: func.HttpRequest) -> func.HttpResponse:
    try:
        employee_id = int(req.route_params.get("employee_id"))
        body = req.get_json()

        required_fields = [
            "first_name",
            "last_name",
            "department_id",
            "salary",
        ]

        missing_fields = [
            field
            for field in required_fields
            if field not in body
        ]

        if missing_fields:
            return func.HttpResponse(
                json.dumps({
                    "error": "Missing required fields.",
                    "fields": missing_fields,
                }),
                status_code=400,
                mimetype="application/json",
            )

        service = EmployeeService()

        updated = service.update_employee(
            employee_id=employee_id,
            first_name=body["first_name"],
            last_name=body["last_name"],
            department_id=int(body["department_id"]),
            salary=float(body["salary"]),
            bonus=(
                float(body["bonus"])
                if body.get("bonus") is not None
                else None
            ),
            hire_date=body.get("hire_date"),
        )

        if not updated:
            return func.HttpResponse(
                json.dumps({
                    "error": "Employee not found."
                }),
                status_code=404,
                mimetype="application/json",
            )

        return func.HttpResponse(
            json.dumps({
                "message": "Employee updated successfully.",
                "employee_id": employee_id,
            }),
            status_code=200,
            mimetype="application/json",
        )

    except ValueError as error:
        return func.HttpResponse(
            json.dumps({"error": str(error)}),
            status_code=400,
            mimetype="application/json",
        )

    except (TypeError, KeyError):
        return func.HttpResponse(
            json.dumps({"error": "Invalid request body."}),
            status_code=400,
            mimetype="application/json",
        )

    except Exception:
        return func.HttpResponse(
            json.dumps({"error": "Internal server error."}),
            status_code=500,
            mimetype="application/json",
        )

def delete_employee(req: func.HttpRequest) -> func.HttpResponse:
    try:
        employee_id = int(req.route_params.get("employee_id"))

        service = EmployeeService()
        deleted = service.delete_employee(employee_id)

        if not deleted:
            return func.HttpResponse(
                json.dumps({
                    "error": "Employee not found."
                }),
                status_code=404,
                mimetype="application/json",
            )

        return func.HttpResponse(
            json.dumps({
                "message": "Employee deleted successfully.",
                "employee_id": employee_id,
            }),
            status_code=200,
            mimetype="application/json",
        )

    except ValueError as error:
        return func.HttpResponse(
            json.dumps({"error": str(error)}),
            status_code=400,
            mimetype="application/json",
        )

    except (TypeError, KeyError):
        return func.HttpResponse(
            json.dumps({"error": "Invalid employee ID."}),
            status_code=400,
            mimetype="application/json",
        )

    except Exception:
        return func.HttpResponse(
            json.dumps({"error": "Internal server error."}),
            status_code=500,
            mimetype="application/json",
        )