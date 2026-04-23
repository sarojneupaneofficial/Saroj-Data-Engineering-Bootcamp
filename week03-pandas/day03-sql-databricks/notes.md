# Week 3 Day 3 - Databricks SQL & Window Functions

## Introduction

Today I learned SQL analytics using Databricks workspace.  
Databricks is a cloud-based data platform used for Data Engineering, Data Analytics, and Big Data processing.

It combines:

- Apache Spark
- SQL
- Python
- Machine Learning
- Data Warehousing

---

# What is Databricks?

Databricks is used to process large-scale data efficiently.

It provides:

- SQL workspace
- Notebook environment
- Spark clusters
- Data pipelines
- Lakehouse architecture

---

# Creating Table in Databricks

```sql
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT,
    name STRING,
    salary INT,
    department STRING,
    hire_date DATE
);
```

Insert Data
INSERT OVERWRITE employees VALUES
(1, 'Shalani', 50000, 'IT', '2026-01-10'),
(2, 'Nisha', 60000, 'HR', '2025-05-15');
INSERT OVERWRITE

Replaces existing table data with new data.

Aggregate Functions
Count Employees Hired After Date
SELECT COUNT(_) AS date_count
FROM employees
WHERE hire_date > '2022-01-01';
Explanation
COUNT(_) counts rows
WHERE filters records
returns employees hired after given date
Window Functions
Top 3 Highest Paid Employees in Each Department
SELECT _
FROM (
SELECT _,
ROW_NUMBER() OVER(
PARTITION BY department
ORDER BY salary DESC
) AS rank
FROM employees
) temp
WHERE rank <= 3;
Explanation
ROW_NUMBER()

Assigns unique ranking number.

PARTITION BY department

Creates separate ranking inside each department.

Example:

IT department ranking starts from 1
HR ranking starts from 1
Finance ranking starts from 1
ORDER BY salary DESC

Highest salary gets rank 1.

Outer Query

Filters only top 3 rows.

Example Output
Department Name Salary Rank
IT Kusum 95000 1
IT Bipina 90000 2
IT Avishek 80000 3
Why Window Functions Matter

Used heavily in Data Engineering and Analytics:

Ranking
Top N records
Running totals
Lead/Lag analysis
Deduplication
Department-wise comparisons
Databricks SQL Advantages
Fast big data processing
Works with Spark
Handles millions of rows
Great for ETL pipelines
Cloud scalable
Interview Questions
What is ROW_NUMBER()?

Used to assign unique sequential numbers to rows.

Difference between RANK() and ROW_NUMBER()?
ROW_NUMBER() gives unique numbers
RANK() can repeat ranks in ties
Why use PARTITION BY?

To divide data into groups for separate calculations.

What is Databricks?

Cloud platform built on Apache Spark
