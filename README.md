# Saroj Data Engineering Bootcamp

A structured hands-on bootcamp where I practice Python, SQL, Pandas, Hadoop, and Data Engineering concepts day by day.

---

# Week 1 - Python Foundations

## Day 1 - Orientation

- Introduction to Data Engineering
- Bootcamp roadmap
- Tools setup
- Python environment basics

## Day 2 - Python Collections

- Lists
- Tuples
- Sets
- Dictionaries
- Indexing and slicing

## Day 3 - Data Structures

- Stack
- Queue
- Linked concepts
- Searching basics
- Sorting basics

## Day 4 - Functions & OOP

- Functions
- Parameters
- Return values
- Classes
- Objects
- Methods
- Constructors

## Day 5 - Functions & OOP Practice

- Real practice questions
- Class creation
- Methods implementation
- Problem solving

---

# Week 2 - SQL Fundamentals

## Day 1 - SQL Introduction

- Database basics
- SQL commands
- CREATE DATABASE
- CREATE TABLE
- INSERT INTO
- SELECT basics

## Day 2 - SELECT & WHERE

- Filtering data
- WHERE clause
- AND / OR
- ORDER BY
- LIMIT
- Conditions

## Day 3 - Keys

- Primary Key
- Foreign Key
- Candidate Key
- Alternate Key
- Composite Key
- Unique Key
- Super Key
- Referential Integrity
- DELETE vs DROP

## Day 4 - SQL Queries

- Interview style SQL questions
- Duplicate records
- Second highest salary
- Employees without department
- Revenue calculations
- Top paid employees

---

# Week 3 - Pandas & Big Data

## Day 1 - DataFrame Basics

- Creating DataFrames
- Columns and rows
- Data types
- Adding new columns
- Revenue calculations
- Filtering rows
- Sorting values
- Missing values
- fillna()
- loc[]
- drop_duplicates()
- groupby()

## Day 2 - Hadoop Fundamentals

- What is Hadoop
- Why Hadoop is needed?
- Big Data concepts
- HDFS
- NameNode
- DataNode
- Blocks
- Replication
- YARN
- MapReduce
- Hadoop cluster architecture
- Hadoop commands
- Real-world use cases

  ## Day 3 - SQL Queries and Databricks Workspace

- SQL aggregation using COUNT and filtering
- Table creation and bulk data insertion in Databricks
- Window functions (ROW_NUMBER, PARTITION BY)
- Extracting top-N records per group

## Day 04: SQL, Hadoop & Data Querying Practice

- SQL table creation
- Inserting employee records
- Filtering using `WHERE`
- Pattern matching using `LIKE`
- Filtering multiple values using `IN`
- Range filtering using `BETWEEN`
- Date filtering using `CURRENT_DATE`, `ADD_MONTHS`, and `DATE_SUB`
- Updating records using `UPDATE`
- Aggregating data using `GROUP BY`
- Filtering grouped results using `HAVING`
- Joining tables using `RIGHT JOIN`
- Ranking records using window functions

## Window Functions

I practiced three important ranking functions:

### ROW_NUMBER()

`ROW_NUMBER()` gives a unique number to every row.

---

# Week 4 — Day 1

## Topics Covered

- SQL JOIN (facebook_posts + facebook_reactions)
- Filtering records using WHERE clause
- Finding posts with heart reactions
- Python string sorting using `sorted()`
- ASCII value ordering (A–Z, a–z)
- Removing duplicates from lists using `set()`
- Introduction to Hadoop (HDFS, MapReduce, YARN)
- Introduction to Kafka (Producer, Consumer, Topic, Broker)

# Week 4 Day 02 – Hadoop, Hive & Docker

- Introduction to Apache Hadoop
- HDFS (Hadoop Distributed File System)
- Uploading and reading files from HDFS
- Introduction to Apache Hive
- Running SQL-like queries on big data using Hive
- Basic Docker commands and container management

## Practice Performed

- Loaded CSV dataset into HDFS
- Verified file storage using HDFS commands
- Queried data using Hive tables
- Executed SELECT queries on Hive datasets
- Practiced essential Docker commands
- Managed containers and checked running services

# Week 4 Day 3 – Apache Spark

Learned Apache Spark basics including:

- Spark Architecture (Driver & Executors)
- SparkSession setup
- RDD vs DataFrame
- Transformations vs Actions
- Lazy Evaluation
- Spark SQL queries

Practiced creating DataFrames and running distributed data operations using PySpark.

## Key Practice

**SQL**

```sql
SELECT p.*
FROM facebook_posts p
JOIN facebook_reactions r
ON p.post_id = r.post_id
WHERE r.reaction = 'heart';


## Week 4 Day 4 – Apache Spark Exercises

Today’s session focused on hands-on Apache Spark practice using DataFrames and Spark SQL.

Topics covered:
- Creating and exploring DataFrames
- Selecting and filtering data
- GroupBy and aggregation functions
- Sorting datasets
- Handling missing values
- Creating temporary SQL views
- Running Spark SQL queries



## Author

Saroj Neupane
```
