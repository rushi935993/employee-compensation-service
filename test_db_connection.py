from database.connection import test_connection


if __name__ == "__main__":
    result = test_connection()
    print(result)