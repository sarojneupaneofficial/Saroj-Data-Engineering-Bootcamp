Keys in SQL

key-column(Combination of column) used to identify records uniquely, establish relationship between tables

A key helps us uniquely identify a row and connects tables together

Avoid duplicate data, maintain data accuracy, build relationship between tables, improves data retrieval

Primary Key- A primary key must be uniquely identifies each record in a table

cannot have null value

must be unique

Foreign key- a column that links one table to another

creates a relationship between the tables

ensures referential integrity

Candidate key- any column that can uniquely identifiy a record

Alternate key- keys that are not selected as primary key, null is not allowed, more than 1

Composite key- made up of 2 or more columns, null is not allowed, 1 per table

Unique key- ensures all values in a column are unique, more thaqn 1 in a table

difference between pk- can have 1 null value

can have multiple unique keys

Super key- is any set of columns that uniquely identifies a record

includes: primary key, candidate key, extra columns

e.g: {std_id}

{std_id, name}

Referential integrity error- ensures that the relationship between the tables remain consistent and valid enforced using FK

A FK value in 1 table must always match a valid PK value in another table

dept_id INT,

FOREIGN KEY(dept_id) REFERENCES dept(dept_id)

we are not allowed to delete parent table directly if it has child table.

In that case either we have to use cascade or we have to delete child and then parent

Drop vs Delete

Drop - Drop deletes the entire table structure plus the table's data permanently

Delete- it only deletes data(rows), table structures, it is DML command

this delete also removes the data table still exist, can use where condition as well

Delete means removing student from a classroom, but classroom still exist

But for drop means destroying the entire classroom and nothing remains

Test Question

When you will use drop instead of delete?

--> We use delete when you want to remove data but keep table and we will use drop when the table is no longer needed.

Create database test_db;

Used test_db;

CREATE TABLE emp(

id INT,

name VARCHAR(30),

salary INT

);

INSERT INTO emp VALUES (1, "Bipina", 2000), (2, "Shalini", 2000), (3, "Bipi", 2000)

#We are deleting specific rows

DELETE FROM emp WHERE id=2;

DELETE FROM emp; # Delete all rows

SELECT \* FROM emp; #can rollback as well

DROP- DDL Command, means it will delete the entire table and it also removes the data, structures, and indexes

DROP TABLE emp;

SELECT \* FROM emp; # it will give an error that table doesn't exist
