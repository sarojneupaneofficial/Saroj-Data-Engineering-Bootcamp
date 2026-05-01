Topics Covered

1. Spark DataFrame Basics
   Creating DataFrames
   Viewing schema using:
   df.printSchema()
   Displaying data:
   df.show()
2. Selecting Columns

Extract specific columns from datasets:

df.select("column_name").show()

Selecting multiple columns:

df.select("col1", "col2").show() 3. Filtering Data

Filtering rows based on conditions:

df.filter(df.age > 25).show()

Using SQL-style condition:

df.filter("age > 25").show() 4. Group By Operations

Aggregation using groupBy:

df.groupBy("department").count().show()

Example with average:

df.groupBy("department").avg("salary").show() 5. Sorting Data

Sort dataset in ascending order:

df.orderBy("salary").show()

Descending order:

df.orderBy(df.salary.desc()).show() 6. Handling Missing Values

Drop null values:

df.dropna().show()

Fill missing values:

df.fillna(0).show() 7. Creating Temporary SQL Views

Register DataFrame as SQL table:

df.createOrReplaceTempView("table_name")

Query using Spark SQL:

spark.sql("SELECT \* FROM table_name").show() 8. Aggregation Functions Used

Common aggregations practiced:

count()
sum()
avg()
max()
min()

Example:

df.selectExpr("avg(salary)").show()
