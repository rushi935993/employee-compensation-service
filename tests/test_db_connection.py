from database.connection import test_connection


def test_database_connection():
    result = test_connection()

    assert result["connected"] is True
    assert result["result"] == 1