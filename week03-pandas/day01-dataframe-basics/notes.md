# Week 3 Day 1 - Pandas DataFrame Basics

## Introduction

Today’s topic focuses on **Pandas DataFrames**, one of the most important tools in Data Analytics, Data Science, and Data Engineering.

A **DataFrame** is a two-dimensional table-like data structure in Python provided by the **Pandas** library. It organizes data into rows and columns, similar to an Excel sheet or SQL table.

DataFrames are widely used for:

- Cleaning raw data
- Transforming datasets
- Handling missing values
- Performing calculations
- Filtering records
- Preparing data for dashboards and machine learning

Learning DataFrames is essential because most real-world business data is stored in tabular format.

---

## Why This Topic Matters

In modern companies such as Amazon, Google, Uber, and PayPal, millions of rows of sales, customer, and product data are processed daily.

DataFrames help professionals:

- Analyze business performance
- Detect data issues
- Calculate revenue and trends
- Build ETL pipelines
- Prepare reports

This is why Pandas is a core skill for Data Engineers and Analysts.

---

## Topics Covered Today

## 1. Creating a DataFrame

A DataFrame can be created using dictionaries, lists, CSV files, SQL tables, or APIs.

Example:

```python id="57b6rn"
import pandas as pd

data = {
    "Product": ["Laptop", "Phone"],
    "Price": [1200, 800]
}

df = pd.DataFrame(data)
```

This creates a structured table with rows and columns.

---

## 2. Adding New Columns

New columns can be created using calculations from existing columns.

Example:

```python id="6pwnjl"
df["Revenue"] = df["Price"] * df["Sales"]
```

Used in business analysis to calculate:

- Revenue
- Profit
- Tax
- Discounts

---

## 3. Basic DataFrame Operations

### View First Rows

```python id="uhx2f8"
df.head(3)
```

Shows the first 3 rows.

### Column Names

```python id="5zzupn"
df.columns
```

Returns all column names.

### Data Types

```python id="zudn13"
df.dtypes
```

Shows whether data is integer, float, string, etc.

This is important for cleaning incorrect data formats.

---

## 4. Adding New Records

Rows can be added using:

```python id="g5b4n9"
df.loc[len(df)] = ["Mouse", 50, 25]
```

Used when inserting new business records.

---

## 5. Missing Data Handling

Real datasets often contain blank or missing values.

Examples:

- Missing salary
- Unknown customer city
- Empty product price

### Detect Missing Values

```python id="n9gnpt"
df.isnull()
```

### Count Missing Values

```python id="u3kr5k"
df.isnull().sum()
```

### Fill Missing Values

```python id="5sj8cz"
df.fillna(0)
```

Missing value handling is one of the most important real-world data skills.

---

## 6. Filtering Data

Example:

```python id="6x72q7"
df[df["Sales"] < 10]
```

Used to find:

- Low-selling products
- High-risk customers
- Low inventory items

---

# SQL Interview Questions Covered Today

These questions are common in technical interviews:

1. Find duplicate records
2. Second highest salary
3. Employees without department
4. Total revenue per product
5. Top 3 highest-paid employees

These questions test SQL logic, aggregation, filtering, joins, and ranking.

---

# Real-World Applications

Pandas DataFrames are used in:

- Sales dashboards
- Finance reports
- Customer analytics
- Inventory management
- Machine learning pipelines
- ETL workflows

---

# Summary

Today introduced the foundation of tabular data processing using Pandas.

Key skills learned:

- Create DataFrames
- Add columns
- Read structure
- Insert rows
- Handle missing data
- Filter records

These are beginner skills that lead into advanced topics such as:

- GroupBy
- Merge / Join
- Pivot Tables
- Time Series
- Data Visualization

---

# Conclusion

Mastering DataFrames is the first major step toward becoming a strong Data Analyst or Data Engineer. Almost every real-world dataset you work with in the future will involve DataFrame operations.
