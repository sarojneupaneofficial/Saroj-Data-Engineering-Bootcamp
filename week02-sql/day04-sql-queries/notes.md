-- =====================================================
-- SQL NOTES : AGGREGATE FUNCTIONS + JOINS
-- =====================================================

-- =====================================================
-- WEEK PRACTICE NOTES
-- SQL INSTALLATION + COMMON PROBLEMS
-- =====================================================

/\*
SQL INSTALLATION NOTES

1. Installed MySQL Server
   - Downloaded and installed MySQL Server.
   - MySQL Server is used to store and manage databases.

2. Installed MySQL Workbench
   - GUI tool used to write SQL queries.
   - Helps create databases, tables, and run commands.

3. Setup Connection
   - Created local connection using:
     Hostname: localhost
     Port: 3306
     Username: root
     Password: **\*\*\*\***

4. Tested Connection
   - Successfully connected to MySQL server.

\*/

/\*
COMMON PROBLEMS FACED DURING INSTALLATION
=====================================================

1. No Database Selected
   Error:
   SQL Error [1046] [3D000]: No database selected

Reason:
Database was not selected before creating table.

Solution:
USE dashboard_db;

2. Can't Create Database (Already Exists)
   Error:
   SQL Error [1007]: Can't create database; database exists

Reason:
Database already created before.

Solution:
USE dashboard_db;

OR

DROP DATABASE dashboard_db;
CREATE DATABASE dashboard_db;

3. Communications Link Failure

Reason:
MySQL server not running.

Solution:

- Start MySQL service
- Check localhost and port 3306
- Restart MySQL Workbench

4. Public Key Retrieval is not allowed

Reason:
Authentication issue in MySQL connection.

Solution:
Connection settings:
allowPublicKeyRetrieval=true
useSSL=false

5. Syntax Errors

Reason:
Missing semicolon (;)
Wrong spelling
Wrong table name

Solution:
Check query carefully.

\*/

/\*
WHAT I LEARNED THIS WEEK
=====================================================

- Installed MySQL Server and Workbench
- Connected database locally
- Created database and tables
- Inserted records
- Used SELECT, UPDATE, DELETE
- Practiced Aggregate Functions
- Learned SQL JOINS
- Solved installation errors

\*/

/_
EXAMPLE COMMANDS
=====================================================
_/

CREATE DATABASE dashboard_db;
USE dashboard_db;

CREATE TABLE Employee (
emp_id INT,
emp_name VARCHAR(50),
salary INT
);

SELECT \* FROM Employee;

-- =====================================================
-- AGGREGATE FUNCTIONS
-- =====================================================

-- AVG() = Finds average value
-- Example: Average order amount per city
SELECT City, AVG(Amount) AS Avg_Order
FROM Orders
GROUP BY City;

-- MAX() = Highest value
SELECT Customer_Name, MAX(Amount) AS Max_Order
FROM Orders
GROUP BY Customer_Name;

-- MIN() = Lowest value
SELECT Customer_Name, MIN(Amount) AS Min_Order
FROM Orders
GROUP BY Customer_Name;

-- SUM() = Total value
SELECT Customer_Name, SUM(Amount) AS Total_Sales
FROM Orders
GROUP BY Customer_Name;

-- COUNT() = Number of rows
SELECT City, COUNT(\*) AS Total_Orders
FROM Orders
GROUP BY City;

-- WHERE = Filter rows before grouping
SELECT Customer_Name, SUM(Amount)
FROM Orders
WHERE Amount > 4000
GROUP BY Customer_Name;

-- =====================================================
-- UPDATE COMMAND
-- =====================================================

-- Update single customer
UPDATE Orders
SET Amount = Amount + 1000
WHERE Customer_Name = 'Kusum';

-- Update city records
UPDATE Orders
SET Amount = Amount + 5000
WHERE City = 'NY';

-- =====================================================
-- JOINS NOTES
-- =====================================================

-- INNER JOIN
-- Returns matching records from both tables

SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;

-- LEFT JOIN
-- Returns all records from left table
-- Matching records from right table
-- No match = NULL

SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;

-- RIGHT JOIN
-- Returns all records from right table
-- Matching from left table
-- No match = NULL

SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;

-- FULL OUTER JOIN (MySQL workaround using UNION)
-- Returns all matched + unmatched rows

SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id

UNION

SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;

-- CROSS JOIN
-- Returns every combination of both tables
-- Cartesian Product

SELECT e.name, d.department_name
FROM employees e
CROSS JOIN departments d;

-- =====================================================
-- QUICK MEMORY TRICK
-- =====================================================

-- INNER = Common in both
-- LEFT = All Left
-- RIGHT = All Right
-- FULL = Everything
-- CROSS = All combinations
