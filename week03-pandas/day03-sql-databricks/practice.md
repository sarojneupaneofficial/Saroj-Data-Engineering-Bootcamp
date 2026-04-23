# Week 3 Day 3 - 5 Practice Questions with Answers with the databricks

## Q1. Display All Employee Records

```sql
SELECT *
FROM employees;

## Q2. Show Employees in IT Department
SELECT *
FROM employees
WHERE department = 'IT';


## Q3. Find Employees with Salary Greater Than 70000
SELECT name, salary
FROM employees
WHERE salary > 70000;

## Q4. Count Employees Hired After 2022-01-01
SELECT COUNT(*) AS total_employees
FROM employees
WHERE hire_date > '2022-01-01';

## Q5. Top 3 Highest Paid Employees in Each Department
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER(
               PARTITION BY department
               ORDER BY salary DESC
           ) AS rank
    FROM employees
) temp
WHERE rank <= 3;
```
