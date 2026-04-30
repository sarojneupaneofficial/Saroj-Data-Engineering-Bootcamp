Week 4 – Day 3 — Apache Spark Notes
What is Apache Spark?

Apache Spark is a fast distributed data processing framework used for big data analytics, ETL pipelines, machine learning, and streaming.

It processes large datasets across clusters much faster than traditional systems like Hadoop MapReduce.

Why Spark is Important

Key advantages:

In-memory processing (faster than disk-based systems)
Distributed computing
Supports batch + streaming data
Works with Python, SQL, Scala, Java
Integrates with Hadoop ecosystem

Used heavily in data engineering pipelines 🚀

Spark Architecture

Main components:

1. Driver Program

Controls execution of Spark applications.

Responsibilities:

Creates SparkSession
Converts code into execution plan
Sends tasks to executors 2. Executors

Workers that:

Run computations
Store data in memory
Return results to driver 3. Cluster Manager

Manages resources across cluster nodes.

Examples:

YARN
Kubernetes
Standalone Spark Cluster
Spark Core Components
SparkSession

Entry point to Spark applications.

Example:

from pyspark.sql import SparkSession

spark = SparkSession.builder \
 .appName("Week4Day3Practice") \
 .getOrCreate()
RDD (Resilient Distributed Dataset)

Basic distributed data structure in Spark.

Properties:

Immutable
Fault tolerant
Distributed across cluster

Example:

rdd = spark.sparkContext.parallelize([1,2,3,4,5])
print(rdd.collect())
DataFrames

Structured data format (like tables).

Example:

data = [("Saroj", 22), ("Alex", 25)]

df = spark.createDataFrame(data, ["Name", "Age"])
df.show()

Advantages over RDD:

Faster execution
Optimized query engine
Supports SQL queries
Spark SQL

Run SQL queries on datasets.

Example:

df.createOrReplaceTempView("people")

spark.sql("SELECT \* FROM people").show()
Transformations vs Actions
Transformations (lazy execution)

Examples:

map()
filter()
select()

Example:

rdd.map(lambda x: x\*2)
Actions (trigger execution)

Examples:

collect()
show()
count()

Example:

rdd.collect()
Lazy Evaluation in Spark

Spark does not execute immediately.

Execution happens only when:

collect()
show()
count()

are called.

This improves performance ⚡

Example Workflow in Spark

Typical pipeline:

Create SparkSession
Load dataset
Apply transformations
Run actions
Save results

Example:

df = spark.read.csv("data.csv", header=True)

df_filtered = df.filter(df["Age"] > 20)

df_filtered.show()
Where Spark is Used (Real Projects)

Common data engineering use cases:

ETL pipelines
Big data analytics
Streaming pipelines
Machine learning preprocessing
Log analysis

Tools Spark works with:

Hadoop
Hive
Kafka
AWS S3
Databricks
