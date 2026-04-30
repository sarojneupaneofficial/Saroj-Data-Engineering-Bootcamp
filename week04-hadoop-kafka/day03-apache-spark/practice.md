## Practice Tasks

Try these:

## Task 1

Create SparkSession and print version

print(spark.version)

# Task 2

Create DataFrame manually

data = [("A",10),("B",20)]
df = spark.createDataFrame(data, ["Name","Score"])
df.show()

# Task 3

Filter dataset

df.filter(df["Score"] > 10).show()

# Task 4

Run SQL query

df.createOrReplaceTempView("students")

spark.sql("SELECT \* FROM students").show()
