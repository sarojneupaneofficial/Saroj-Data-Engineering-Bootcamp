SQL Notes (Window Functions, Filters, Dates, Joins, Aggregations)
1️⃣ Window Functions (Ranking)

Window functions assign rankings without collapsing rows.

ROW_NUMBER()
Assigns unique sequential numbers
No duplicates
Useful for pagination, removing duplicates, selecting top rows

Example:

SELECT \*,
ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
FROM employees;

Example ranking:

Salary ROW_NUMBER
100 1
100 2
80 3
70 4
RANK()
Same rank for ties
Skips next rank number

Example:

Salary RANK
100 1
100 1
80 3
70 4

Use case:
✔ Competition ranking
✔ Leaderboards with gaps allowed

DENSE_RANK()
Same rank for ties
No skipped numbers

Example:

Salary DENSE_RANK
100 1
100 1
80 2
70 3

Use case:
✔ Top N products
✔ Continuous ranking lists

2️⃣ Date Filtering (Recent Records)
Last 6 months
SELECT _
FROM coders
WHERE hire_date >= add_months(current_date(), -6);
Last 180 days
SELECT _
FROM coders
WHERE hire_date >= date_sub(current_date(), 180);
3️⃣ Pattern Matching (LIKE)

Used for searching text patterns.

Pattern Meaning
'A%' starts with A
'%a' ends with a
'%is%' contains "is"
'**\_**' exactly 5 characters

Examples:

SELECT _ FROM emp1 WHERE first_name LIKE 'A%';
SELECT _ FROM emp1 WHERE first_name LIKE '%a';
SELECT _ FROM emp1 WHERE first_name LIKE '%is%';
SELECT _ FROM emp1 WHERE first_name LIKE '**\_**';
4️⃣ Filtering with IN

Select multiple values easily:

SELECT \*
FROM emp1
WHERE emp_id IN (1,3,5);

Equivalent to:

emp_id = 1 OR emp_id = 3 OR emp_id = 5
5️⃣ Range Filtering (BETWEEN)
Salary range
SELECT _
FROM emp1
WHERE salary BETWEEN 50000 AND 70000;
Date range
SELECT _
FROM emp1
WHERE hire_date BETWEEN '2021-01-01' AND '2023-12-31';
6️⃣ Updating Data
Increase salary by 10%
UPDATE emp1
SET salary = salary \* 1.10
WHERE department = 'IT';
Change department
UPDATE emp1
SET department = 'admin'
WHERE emp_id = 2;
7️⃣ Aggregation with GROUP BY

Used to summarize grouped data.

Example:

SELECT department, COUNT(\*) AS num_employees
FROM emp1
GROUP BY department
HAVING num_employees > 2;

Explanation:

Clause Purpose
GROUP BY groups rows
COUNT(\*) counts employees
HAVING filters grouped results
8️⃣ Joins (RIGHT JOIN)

Used to combine data from multiple tables.

Tables:

employee

emp_id | emp_name | department_id

departments

department_id | department_name

Example:

SELECT d.department_name, e.emp_id, e.emp_name
FROM employee e
RIGHT JOIN departments d
ON e.department_id = d.department_id;

Meaning:

Returns all departments
Matches employees if available
Shows NULL if no employee exists in department
