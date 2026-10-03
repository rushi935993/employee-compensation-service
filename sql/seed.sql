INSERT INTO Department
    (DepartmentID, DepartmentName, Location)
VALUES
    (1, 'Engineering', 'Pune'),
    (2, 'Human Resources', 'Mumbai'),
    (3, 'Finance', 'Pune'),
    (4, 'Operations', 'Mumbai'),
    (5, 'Sales', 'Pune');


INSERT INTO Employee
    (FirstName, LastName, DepartmentID, Salary, Bonus, HireDate)
VALUES
    ('Aarav', 'Sharma', 1, 800000.00, 100000.00, '2023-01-15'),
    ('Priya', 'Patil', 1, 700000.00, NULL,       '2023-04-10'),
    ('Rohan', 'Deshmukh', 1, 900000.00, 150000.00, '2022-08-20'),

    ('Neha', 'Joshi', 2, 600000.00, 30000.00, '2024-02-01'),
    ('Amit', 'Kulkarni', 2, 550000.00, NULL, '2024-06-15'),

    ('Sneha', 'More', 3, 1000000.00, 300000.00, '2021-11-05'),
    ('Vikram', 'Pawar', 3, 850000.00, 100000.00, '2022-03-18'),

    ('Pooja', 'Shinde', 4, 500000.00, NULL, '2023-09-12'),
    ('Kunal', 'Jadhav', 4, 450000.00, 50000.00, '2024-01-20'),
    ('Anjali', 'Patil', 4, 1200000.00, 10000.00, '2020-07-01'),

    ('Raj', 'Mehta', 5, 100000.00, 200000.00, '2025-01-10'),
    ('Kavya', 'Desai', 5, 120000.00, 150000.00, '2025-02-14');