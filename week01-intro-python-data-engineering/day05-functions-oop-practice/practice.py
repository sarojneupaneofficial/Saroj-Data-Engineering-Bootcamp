# Exercise 1: Function Practice

# Function
def square(n):
    return n * n


print("Square:", square(5))

# Even or Odd


def check(n):
    return "Even" if n % 2 == 0 else "Odd"


print("Check:", check(10))

# OOP


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)


emp1 = Employee("Saroj", 50000)
emp1.display()
