## Week 4 – Day 2 Notes — Hadoop, Hive & Docker

## Hadoop

Hadoop is an open-source framework used for distributed storage and processing of big data across clusters of machines.

## Core Components

## HDFS (Hadoop Distributed File System)

Stores large datasets
Splits files into blocks
Distributes blocks across DataNodes
Provides fault tolerance using replication

## NameNode

Stores metadata
Tracks file locations
Controls access to files

## DataNode

Stores actual data blocks
Executes read/write operations

## YARN

Manages cluster resources
Schedules jobs

## MapReduce

Processes large datasets in parallel
Uses Map → Shuffle → Reduce workflow
Hive

Hive is a data warehouse tool built on Hadoop that allows querying large datasets using SQL-like syntax called HiveQL.

# Example:

SELECT \* FROM employees;

Hive converts queries into MapReduce jobs internally.

## Features of Hive

SQL-like query language (HiveQL)
Runs on top of HDFS
Used for batch processing
Suitable for structured data
Not designed for real-time analytics
Hive vs Traditional SQL
Feature Hive SQL Databases
Processing Batch Real-time
Storage HDFS Local Disk
Speed Slower Faster
Use Case Big Data Analytics Transactions

## Docker Basics

Docker is used to create lightweight containers for running applications consistently across environments.

## Common Docker Commands

## Check version:

docker --version

## Pull image:

docker pull image_name

## List running containers:

docker ps

## List all containers:

docker ps -a

# Start container:

docker start container_id

# Stop container:

docker stop container_id

# Remove container:

docker rm container_id

# Remove image:

docker rmi image_name

# Run container interactively:

docker run -it image_name bash

## What I Learned Today

Hadoop architecture basics
HDFS working (NameNode & DataNode)
Role of YARN and MapReduce
Hive and HiveQL queries
Difference between Hive and SQL databases
Essential Docker commands for containers
