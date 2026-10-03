import json
import os
from pathlib import Path
from typing import Any

import pyodbc


def _load_local_settings() -> None:
    """Load local.settings.json for local development."""

    project_root = Path(__file__).resolve().parent.parent
    settings_path = project_root / "local.settings.json"

    if not settings_path.exists():
        return

    with settings_path.open("r", encoding="utf-8") as file:
        settings = json.load(file)

    values = settings.get("Values", {})

    connection_string = values.get("SQL_CONNECTION_STRING")

    if connection_string:
        os.environ["SQL_CONNECTION_STRING"] = connection_string


def get_connection() -> pyodbc.Connection:
    """Create an Azure SQL connection."""

    _load_local_settings()

    connection_string = os.getenv("SQL_CONNECTION_STRING")

    if not connection_string:
        raise RuntimeError(
            "SQL_CONNECTION_STRING is not configured."
        )

    return pyodbc.connect(connection_string)


def test_connection() -> dict[str, Any]:
    """Test the database connection."""

    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1 AS result")
        row = cursor.fetchone()

        return {
            "connected": True,
            "result": row.result if row else None,
        }

    finally:
        connection.close()