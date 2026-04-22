# Week 3 Day 2 - Introduction to Hadoop

## What is Hadoop?

Hadoop is an open-source framework used to store and process very large amounts of data across many computers.

It is mainly used in Data Engineering and Big Data environments where normal databases cannot handle massive data efficiently.

Hadoop allows distributed storage and distributed processing.

---

## Why Hadoop is Needed

Traditional systems have limitations:

- Storage becomes expensive
- Slow processing on single machine
- Difficult to handle terabytes/petabytes of data
- Failure of one server can stop operations

Hadoop solves these by:

- Using many machines together
- Splitting data across systems
- Parallel processing
- Fault tolerance

---

## Main Components of Hadoop

## 1. HDFS (Hadoop Distributed File System)

Used for storing large files across multiple machines.

Features:

- Splits files into blocks
- Stores blocks on different nodes
- Replication for safety
- High fault tolerance

Example:

A 1GB file may be divided into multiple blocks and stored across many computers.

---

## 2. YARN (Yet Another Resource Negotiator)

Used for managing cluster resources.

Responsibilities:

- CPU allocation
- Memory management
- Job scheduling
- Resource sharing

---

## 3. MapReduce

Programming model used to process huge datasets.

Two phases:

### Map Phase

Breaks data into key-value pairs.

### Reduce Phase

Combines and summarizes final result.

Example:

Counting words in millions of files.

---

## 4. Hadoop Common

Libraries and utilities required for Hadoop to run.

---

## Hadoop Cluster Architecture

### Master Node

Controls cluster.

Includes:

- NameNode
- ResourceManager

### Worker Nodes

Do actual storage and processing.

Includes:

- DataNode
- NodeManager

---

## HDFS Important Terms

## NameNode

Master server that stores metadata:

- file names
- permissions
- block locations

## DataNode

Stores actual data blocks.

## Block

Small part of file stored separately.

Default block sizes may vary (128MB common).

## Replication Factor

Number of copies of each block.

Example:

Replication factor = 3 means 3 copies of every block.

---

## Advantages of Hadoop

- Handles huge data
- Scalable
- Fault tolerant
- Low cost storage
- Open source
- Parallel processing
- Flexible (structured + unstructured data)

---

## Disadvantages of Hadoop

- Complex setup
- Slower than memory-based systems
- Requires many machines
- Not ideal for real-time analytics

---

## Hadoop vs Traditional Database

| Feature   | Hadoop         | Traditional DB        |
| --------- | -------------- | --------------------- |
| Data Size | Huge           | Medium                |
| Cost      | Lower          | Higher                |
| Speed     | Good for batch | Good for transactions |
| Schema    | Flexible       | Fixed                 |
| Scaling   | Horizontal     | Vertical              |

---

## Real World Use Cases

- Log processing
- Social media analytics
- Recommendation systems
- Fraud detection
- Search engines
- Data lakes

---

## Common Hadoop Commands

```bash
hdfs dfs -ls /
hdfs dfs -mkdir /data
hdfs dfs -put file.csv /data
hdfs dfs -cat /data/file.csv
```
