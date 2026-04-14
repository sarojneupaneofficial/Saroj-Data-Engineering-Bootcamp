# Practice Question

# 1. Function to return square of a number
def square(num):
    return num * num


print(square(5))


# 2. Function to check even or odd
def check_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_number(7))


# 3. Function to multiply each value by 2
lst = [5, 10, 15]


def multiply_list(numbers):
    result = []
    for i in numbers:
        result.append(i * 2)
    return result


print(multiply_list(lst))


# Map functions

number = [1, 2, 3, 4, 5]


def add_ten(x):
    return x + 10


result = map(add_ten, number)

print(list(result))

# find only even number - use filter

num = [1, 2, 3, 4, 5, 6]

result1 = list(filter(lambda x: x % 2 == 0, num))

print(result1)

# get employees with salary > 10000


s = [5000, 12000, 8000, 20000, 50000]

high_sal = filter(lambda x: x > 10000, s)
print(list(high_sal))

# fibonacci Series


def fib(n):

    if n <= 1:

        return n

    return fib(n-1) + fib(n-2)

# print Series


n = 7

for i in range(n):

    print(fib(i))

# Factorial = 5! using recursion

# example


class Person:  # blueprint Created
    def __init__(self, name, year):  # runs automatically when object is created
        self.name = name  # Assigning values, Left side -> object variable , righside -> input value
        self.year = year


# object creation- internally - Person.__init__(p1, "Kushal", 2026)
p1 = Person("Kushal", 2026)

print(p1.name)  # Accessing Data
print(p1.year)
