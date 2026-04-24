-- Row_number - Unique rank(no duplicates)
-- Rank() - skips rank() - 1,2,2,4
-- DENSE_RANK() - No skipping - no skipping (1,2,2,3)

 

 
-- R-- Row_number - Unique rank(no duplicates)
-- Rank() - skips rank() - 1,2,2,4
-- DENSE_RANK() - No skipping - no skipping (1,2,2,3)

 

 
-- Row_number() - unique, consective, numbering (pagination)
-- rank() - to rank items where ties skip intermediate rank (1,2,2,4)
-- dense_rank() - for ranking without gaps (1,2,2,3)
 ow_number() - unique, consective, numbering (pagination)
-- rank() - to rank items where ties skip intermediate rank (1,2,2,4)

-- dense_rank() - for ranking without gaps (1,2,2,3) -
-- assign the same rank to ties without gaps (1,2,2,3)
-- Leaderboards -> where ranking must be contiguous, identifying top N products

 

 
e.g.,
     rn
100  1  1  1
100  2  1  1
80   3  3  2
70   4  4  3

%sql
SELECT \*
from coders
WHERE hire_date >= add_months(current_date(), -6);

 
-- last 180 days -

 
--SELECT \*
--from coders
--WHERE hire_date >= date_sub(current_date(), 180);

 

 

CREATE TABLE IF NOT EXISTS emp1 (
emp_id INT,
first_name STRING,
last_name STRING,
department STRING,
salary INT,
hire_date DATE
);
INSERT OVERWRITE emp1 VALUES
(1, 'Nirajan', 'kc', 'IT', 60000, '2022-01-15'),
(2, 'Keshab','Rai','HR', 45000, '2021-03-10'),
(3, 'Shalani','Shah','IT', 70000, '2020-06-01'),
(4,'Nisha','Adhikari','Finance', 50000, '2019-11-12'),
(5,'Matrika','Subedi','HR', 48000, '2022-06-01'),
(6,'Arbin','Budhathoki','IT', 55000, '2023-02-18'),
(7,'Avishek','Bhandari','Finance', 65000, '2021-09-30'),
(8,'Saroj','Neupane','IT', 72000,'2020-12-25');

SELECT \*
from emp1
where first_name LIKE 'A%';

SELECT \*
from emp1
where first_name LIKE '%a';

SELECT \*
from emp1
where first_name like '%is%';

SELECT \*
from emp1
where first_name like '**\_**';

SELECT \*
from emp1
where emp_id IN (1,3,5);

SELECT \*
FROM emp1
WHERE salary BETWEEN 50000 AND 70000;

SELECT \*
FROM emp1
WHERE hire_date BETWEEN '2021-01-01' AND '2023-12-31';

UPDATE emp1 SET salary = salary \* 1.10
WHERE department = 'IT';

UPDATE emp1
SET department = 'admin '
WHERE emp_id = 2;

SELECT department, COUNT(\*) AS num_employees
FROM emp1
GROUP BY department
HAVING num_employees > 2;
CREATE TABLE IF NOT EXISTS employee (
emp_id INT,
emp_name STRING,
department_id INT
);

-- Department Tables

CREATE TABLE IF NOT EXISTS departments (
department_id INT,
department_name STRING
);

insert overwrite employee values
(1,'Kusum', 101),
(2,'Sujana', 102),
(3,'Ishwor', 103),
(4,'Bipina', NULL),
(5,'Keshab', 101);

SELECT d.department_name, e.emp_id, e.emp_name
from employee e
RIGHT JOIN departments d
ON e.department_id = d.department_id;
