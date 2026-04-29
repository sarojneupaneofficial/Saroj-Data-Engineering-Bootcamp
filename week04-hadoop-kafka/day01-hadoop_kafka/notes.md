# Week 4 Day 1 Notes

## Topics Covered

- SQL joins
- Filtering data using `WHERE`
- Facebook posts and reactions question
- Python list practice
- Alphabetizing strings
- ASCII values
- Hadoop basics
- Kafka basics

---

# 1. SQL Practice

## Question

Find all posts which were reacted to with a heart.

For such posts, output all columns from the `facebook_posts` table.

## Logic

1. Find rows where reaction is `'heart'`
2. Match those reactions with posts using `post_id`
3. Return all post details from `facebook_posts`

## SQL Query

```sql
SELECT p.*
FROM facebook_posts p
JOIN facebook_reactions r
ON p.post_id = r.post_id
WHERE r.reaction = 'heart';
```

## Explanation

facebook_posts p means we are giving the table an alias called p
facebook_reactions r means we are giving the reactions table an alias called r
JOIN combines both tables
ON p.post_id = r.post_id matches posts with their reactions
WHERE r.reaction = 'heart' filters only heart reactions
SELECT p.\* returns all columns from the posts table 2. Python List Practice
Given List
emp_ids = [101, 1012, 104, 104, 101, 102, 1012]
Find Unique Employee IDs
emp_ids = [101, 1012, 104, 104, 101, 102, 1012]

unique_ids = list(set(emp_ids))

print(unique_ids)
Count How Many Times Each ID Appears
emp_ids = [101, 1012, 104, 104, 101, 102, 1012]

for emp in set(emp_ids):
print(emp, "appears", emp_ids.count(emp), "times")
Output
101 appears 2 times
102 appears 1 times
104 appears 2 times
1012 appears 2 times 3. Alphabetize Strings
Question

Sort a given string alphabetically.

## Example

string = "PythonRocks"
Output
PRchknoosty
Code
string = "PythonRocks"

result = ''.join(sorted(string))

print(result)

## Explanation

sorted(string) sorts every character
Capital letters come before lowercase letters because of ASCII values
''.join() joins the sorted characters back into a string 4. ASCII Values

ASCII gives each character a numeric value.

Important values:

A = 65
Z = 90
a = 97
z = 122

That is why uppercase letters come before lowercase letters when sorting.

Example
print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))
Output
65
90
97
122 5. More String Practice
Example 1
string = 'axbyacd'

result = ''.join(sorted(string))

print(result)
Output
aabcdxy
Example 2
s = "escapevelocity"

result = ''.join(sorted(s))

print(result)
Output
acceeeilopstvy 6. Hadoop Basics
What is Hadoop?

Hadoop is a framework used to store and process very large amounts of data.

It is mainly used for Big Data.

Main Parts of Hadoop

1. HDFS

HDFS stands for Hadoop Distributed File System.

It stores large files across multiple machines.

2. MapReduce

MapReduce is used to process large datasets.

It works in two steps:

Map
Reduce 3. YARN

YARN manages resources and jobs in Hadoop.

Simple Hadoop Flow
Large Data
↓
Stored in HDFS
↓
Processed by MapReduce
↓
Final Output 7. Kafka Basics
What is Kafka?

Kafka is a distributed streaming platform.

It is used to send, store, and process real-time data.

Main Kafka Terms
Producer

A producer sends data to Kafka.

Consumer

A consumer reads data from Kafka.

Topic

A topic is like a category where messages are stored.

Broker

A broker is a Kafka server.

Message

A message is one piece of data sent through Kafka.

Simple Kafka Flow
Producer
↓
Kafka Topic
↓
Consumer
Example
Website clicks → Kafka → Data pipeline → Dashboard 8. Practice Questions
SQL Practice
Find all posts that received a heart reaction.
Find all posts that received a like reaction.
Find all reactions for each post.
Count how many reactions each post received.
Find posts that have no reactions.
