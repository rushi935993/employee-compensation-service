# Employee Compensation Service

A production-minded backend service for managing employee and department records and generating compensation-related reports.

The service is implemented using **Python Azure Functions** with **Azure SQL Database** as the persistence layer. All database operations are performed through the backend service layer; clients do not access the database directly.

---

## 1. Features

### Employee Management

- Create an employee
- Retrieve an employee by ID
- List all employees
- Filter employees by department
- Update an employee
- Delete an employee

### Compensation Reports

- Total company bonus
- Employees who have never received a bonus
- Bonus percentage relative to salary
- Departments where total bonus exceeds average salary
- Employee bonus ranking
- Highest base salary
- Highest total compensation
- Check whether the highest-base-salary employee is also the highest-total-compensation employee

---

## 2. Architecture

```text
Client
   |
   | HTTPS
   v
Azure Functions HTTP Layer
   |
   v
Service Layer
   |
   v
Repository / Database Layer
   |
   v
Azure SQL Database

Responsibilities

Functions Layer

Handles HTTP requests and responses
Parses request parameters and JSON bodies
Returns appropriate HTTP status codes

Service Layer

Handles business validation
Coordinates application logic
Keeps HTTP concerns separate from database operations

Repository Layer

Executes SQL queries
Performs CRUD operations
Executes compensation reporting queries

Database Layer

Manages the SQL connection
Reads configuration from environment variables/local settings
3. Technology Stack
Python 3.11
Azure Functions
Azure SQL Database
pyodbc
ODBC Driver 18 for SQL Server
pytest
Git / GitHub
Postman or cURL
4. Project Structure
employee-compensation-service/
│
├── database/
│   ├── __init__.py
│   └── connection.py
│
├── functions/
│   ├── __init__.py
│   ├── employee_functions.py
│   └── report_functions.py
│
├── models/
│   ├── __init__.py
│   └── employee.py
│
├── repositories/
│   ├── __init__.py
│   ├── employee_repository.py
│   └── department_repository.py
│
├── services/
│   ├── __init__.py
│   ├── employee_service.py
│   └── compensation_service.py
│
├── utils/
│   ├── __init__.py
│   └── http_response.py
│
├── sql/
│   ├── schema.sql
│   └── seed.sql
│
├── tests/
│   ├── __init__.py
│   ├── test_db_connection.py
│   ├── test_employees.py
│   └── test_reports.py
│
├── function_app.py
├── host.json
├── requirements.txt
├── local.settings.json.example
├── .gitignore
└── README.md
5. Database Schema
Department
Column	Type	Description
DepartmentID	INT	Primary key
DepartmentName	VARCHAR(100)	Department name
Location	VARCHAR(100)	Department location
Employee
Column	Type	Description
EmployeeID	INT IDENTITY	Primary key
FirstName	VARCHAR(50)	Employee first name
LastName	VARCHAR(50)	Employee last name
DepartmentID	INT	Foreign key to Department
Salary	DECIMAL(12,2)	Base salary
Bonus	DECIMAL(12,2)	Optional bonus
HireDate	DATE	Employee hire date

Bonus = NULL represents an employee who has never received a bonus.

6. Prerequisites

Install:

Python 3.11
Azure Functions Core Tools
Microsoft ODBC Driver 18 for SQL Server
Access to an Azure SQL Database

Verify Python:

python --version

Verify Azure Functions Core Tools:

func --version

Verify the SQL Server ODBC driver:

python -c "import pyodbc; print(pyodbc.drivers())"

The output should include:

ODBC Driver 18 for SQL Server
7. Local Setup

Clone the repository and move into the project directory:

cd employee-compensation-service

Create a Python virtual environment:

py -3.11 -m venv .venv

Activate it:

.venv\Scripts\activate

Install dependencies:

python -m pip install -r requirements.txt
8. Database Setup

Create the database schema using:

sql/schema.sql

Then insert the sample data using:

sql/seed.sql

The seed data contains:

5 departments
12 employees

The data intentionally includes employees with NULL bonuses so that the reporting requirements can be tested.

9. Configuration

Create a local settings file from the example:

copy local.settings.json.example local.settings.json

Configure:

{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "python",
        "SQL_CONNECTION_STRING": "YOUR_AZURE_SQL_CONNECTION_STRING"
    }
}

Do not commit local.settings.json.

It is excluded through .gitignore.

For Azure deployment, configure SQL_CONNECTION_STRING as an application setting instead of storing credentials in source code.

10. Run the Application

Activate the virtual environment:

.venv\Scripts\activate

Start Azure Functions:

func start

The API will be available at:

http://localhost:7071
11. API Endpoints
Health
GET /api/health

Example:

curl http://localhost:7071/api/health
Create Employee
POST /api/employees

Example:

curl -X POST http://localhost:7071/api/employees ^
-H "Content-Type: application/json" ^
-d "{\"first_name\":\"Test\",\"last_name\":\"Employee\",\"department_id\":1,\"salary\":650000,\"bonus\":50000,\"hire_date\":\"2026-10-03\"}"
Get Employee
GET /api/employees/{employee_id}

Example:

curl http://localhost:7071/api/employees/1
List Employees
GET /api/employees

Example:

curl http://localhost:7071/api/employees
Filter by Department
GET /api/employees?departmentId={department_id}

Example:

curl "http://localhost:7071/api/employees?departmentId=1"
Update Employee
PUT /api/employees/{employee_id}

Example:

curl -X PUT http://localhost:7071/api/employees/13 ^
-H "Content-Type: application/json" ^
-d "{\"first_name\":\"Test\",\"last_name\":\"Updated\",\"department_id\":1,\"salary\":700000,\"bonus\":75000,\"hire_date\":\"2026-10-03\"}"
Delete Employee
DELETE /api/employees/{employee_id}

Example:

curl -X DELETE http://localhost:7071/api/employees/13
12. Compensation Reports
Total Company Bonus
GET /api/reports/total-bonus

Example:

curl http://localhost:7071/api/reports/total-bonus

The seeded dataset produces:

1,090,000

NULL bonuses are treated as zero using COALESCE.

Employees Without Bonus
GET /api/reports/no-bonus

Example:

curl http://localhost:7071/api/reports/no-bonus

Employees are identified using:

WHERE Bonus IS NULL
Bonus Percentage
GET /api/reports/bonus-percentage

Calculation:

Bonus Percentage = (Bonus / Salary) × 100

The result is rounded to two decimal places.

Departments Where Total Bonus Exceeds Average Salary
GET /api/reports/departments-bonus-above-average-salary

The query uses:

GROUP BY
SUM
AVG
HAVING
COALESCE
Bonus Ranking
GET /api/reports/bonus-ranking

Employees are ordered by bonus from highest to lowest.

Employees with NULL bonuses are placed after employees with bonuses.

Highest Salary
GET /api/reports/highest-salary

The response identifies:

Employee with the highest base salary
Employee with the highest total compensation
Whether they are the same employee

Total compensation is calculated as:

Salary + Bonus

with NULL bonus treated as zero.

13. Error Handling

The API uses standard HTTP status codes.

Status	Meaning
200	Successful request
201	Resource created
400	Invalid request or validation error
404	Employee not found
500	Internal server error

JSON responses are centralized through:

utils/http_response.py
14. Validation

The service layer validates:

Employee ID
Department ID
First name
Last name
Salary
Bonus
Hire date

Examples of invalid input include:

Non-positive employee ID
Missing first name
Negative salary
Negative bonus
Invalid hire date
15. Testing

Run the complete test suite:

python -m pytest -v

The project currently contains tests covering:

Database connectivity
Employee retrieval
Missing employees
Employee listing
Department filtering
Employee validation
Total company bonus
Employees without bonus
Bonus percentage
Department compensation analysis
Bonus ranking
Highest salary
Highest total compensation

Expected result:

16 passed
16. Design Decisions
Layered Architecture

The application separates HTTP handling, business logic, database access, and configuration.

This makes the code easier to test and maintain.

SQL Access Through Backend

Clients never access Azure SQL directly.

All database reads and writes go through the Azure Functions backend.

NULL Bonus Handling

NULL bonus means no bonus has been received.

Reporting calculations use:

COALESCE(Bonus, 0)

when a numeric zero is required.

Secrets

Database credentials are supplied through configuration rather than hardcoded in source code.

local.settings.json is excluded from Git.

Optional Default Bonus

The assignment allows an optional default bonus behavior.

This implementation does not automatically assign a default bonus when the bonus is omitted. The database preserves NULL so that the reporting requirement for employees who have never received a bonus remains meaningful.

17. Production Considerations

For a production deployment, the application can be extended with:

Azure Function App deployment
Azure Application Settings for secrets
Azure Key Vault integration
Application Insights monitoring
Authentication and authorization
Structured logging
CI/CD pipeline
Separate unit and integration test environments
API documentation/OpenAPI
Connection pooling and performance tuning
18. Summary

The Employee Compensation Service provides an HTTP-based backend for employee management and compensation reporting using:

Python
   +
Azure Functions
   +
Azure SQL
   +
pyodbc
   +
Layered Service/Repository Architecture

The implementation includes complete employee CRUD functionality, compensation reporting queries, validation, configuration-based secrets, error handling, SQL scripts, and automated tests.


### Step 26B — Save and verify

After saving `README.md`, run:

```cmd
git status

You should not see:

local.settings.json

Then run:

python -m pytest -v

Expected:

16 passed

