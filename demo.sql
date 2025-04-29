-- Create Departments table
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
);

-- Create Employees table with foreign key reference to Departments
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

-- Insert data into Departments table
INSERT INTO Departments (dept_id, dept_name) VALUES
(1, 'Engineering'),
(2, 'Marketing'),
(3, 'Human Resources'),
(4, 'Finance'),
(5, 'Sales');

-- Insert data into Employees table
INSERT INTO Employees (emp_id, name, salary, dept_id) VALUES
(101, 'John Smith', 75000.00, 1),
(102, 'Jane Doe', 80000.00, 1),
(103, 'David Jones', 65000.00, 2),
(104, 'Sarah Brown', 90000.00, 4),
(105, 'Michael Lee', 72000.00, 3),
(106, 'Emily Chen', 85000.00, 1),
(107, 'Robert Wilson', 68000.00, 5),
(108, 'Lisa Anderson', 79000.00, 2),
(109, 'Thomas Miller', 95000.00, 4),
(110, 'Jennifer Taylor', 70000.00, 3);

CREATE PROCEDURE demo(
    IN ownerId Number,
    OUT is_demo 
)
AS
BEGIN

END

SELECT name, dept_id, salary,
       RANK() OVER(PARTITION BY dept_id ORDER BY salary DESC) as dept_rank
FROM Employees;