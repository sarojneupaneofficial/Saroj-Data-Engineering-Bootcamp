# Week 2 - Day 1: Python Functions, Map, Filter, OOP Basics

## Overview

Today we practiced Python fundamentals important for Data Engineering:

- Functions
- Lambda expressions
- Map and Filter
- Recursion
- Basic Object-Oriented Programming (OOP)

---

## 1. Functions

Functions help reuse code.

```python
def square(num):
    return num * num

print(square(5))
2. Even or Odd Function
def check_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

3. Working with Lists

We created a function to multiply list elements:

def multiply_list(numbers):
    result = []
    for i in numbers:
        result.append(i * 2)
    return result

4. Map Function

Map applies a function to all elements in a list.

def add_ten(x):
    return x + 10

result = map(add_ten, [1, 2, 3, 4, 5])
print(list(result))
5. Filter Function

Filter is used to select elements based on condition.

num = [1, 2, 3, 4, 5, 6]

result1 = list(filter(lambda x: x % 2 == 0, num))
print(result1)
6. Filtering Salary Data
s = [5000, 12000, 8000, 20000, 50000]

high_sal = filter(lambda x: x > 10000, s)
print(list(high_sal))
7. Fibonacci Series (Recursion)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(7):
    print(fib(i))
8. Object-Oriented Programming (OOP)

We created a class to understand objects.

class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year

p1 = Person("Kushal", 2026)

print(p1.name)
print(p1.year)


## Key Learnings
- Functions help organize logic
- Map applies function to all items
- Filter selects data based on condition
- Recursion solves problems using self-calling functions
- OOP helps model real-world objects
```
