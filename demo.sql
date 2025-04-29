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

-- Window Function Explanation
-- RANK() - Assigns a unique rank to rows within a partition, with gaps in the sequence when there are ties
-- PARTITION BY dept_id - Groups the data by department ID, creating separate "windows" for each department
-- ORDER BY salary DESC - Within each department, ranks employees from highest to lowest salary

SELECT name, dept_id, salary,
       RANK() OVER(PARTITION BY dept_id ORDER BY salary DESC) as dept_rank
FROM Employees;


-- Explanation
-- WITH RECURSIVE: Defines a recursive Common Table Expression named fib with two columns:

-- n: Position in the Fibonacci sequence
-- val: Value of the Fibonacci number at position n
-- Base case: SELECT 1, 1 provides the starting point where:

-- First "1" represents position (n=1)
-- Second "1" represents the value of F(1)=1
-- Recursive part:

-- SELECT n+1, val + (SELECT val FROM fib WHERE n = fib.n - 1)
-- For each row, generates the next row where:
-- n+1 increments the position counter
-- val + (SELECT val FROM fib WHERE n = fib.n - 1) adds the current Fibonacci value to the previous one
-- Termination condition: WHERE n < 10 stops the recursion when n reaches 10

-- Final query: SELECT * FROM fib returns all calculated Fibonacci numbers

WITH RECURSIVE fib(n, val) AS (
  SELECT 1, 1
  UNION ALL
  SELECT n+1, val + (SELECT val FROM fib WHERE n = fib.n - 1)
  FROM fib
  WHERE n < 10
)
SELECT * FROM fib;