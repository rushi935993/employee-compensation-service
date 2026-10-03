import json
from typing import Any

import azure.functions as func


def json_response(
    data: Any,
    status_code: int = 200,
) -> func.HttpResponse:
    return func.HttpResponse(
        body=json.dumps(data),
        status_code=status_code,
        mimetype="application/json",
    )


def error_response(
    message: str,
    status_code: int,
) -> func.HttpResponse:
    return json_response(
        {"error": message},
        status_code=status_code,
    )