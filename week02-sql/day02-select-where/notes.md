# Day 2 - OOP Concepts in Python

# Topics:

# 1. Encapsulation

# 2. Inheritance

# 3. Polymorphism

# -----------------------------------

# 1. Encapsulation

# Hiding private data using methods

# -----------------------------------

class Employee:
def **init**(self, salary):
self.\_\_salary = salary # private variable

    # Setter Method = update private data safely
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary

    # Getter Method = access private data safely
    def get_salary(self):
        return self.__salary

emp = Employee(10000)

emp.set_salary(20000)

print("Updated Salary:", emp.get_salary())

# -----------------------------------

# 2. Inheritance

# Child class gets properties/methods

# from parent class

# -----------------------------------

class Person:
def **init**(self, name):
self.name = name

    def show_name(self):
        print("Name:", self.name)

class Employee(Person):
def **init**(self, name, salary):
super().**init**(name) # call parent constructor
self.salary = salary

emp1 = Employee("Arbin", 40000)

emp1.show_name()

print("Salary:", emp1.salary)

# -----------------------------------

# Example of Inheritance

# -----------------------------------

class Vehicle:
def **init**(self, speed):
self.speed = speed

class Car(Vehicle):
def **init**(self, speed, fuel_type):
super().**init**(speed)
self.fuel_type = fuel_type

c1 = Car(180, "Petrol")

print("Speed:", c1.speed)
print("Fuel Type:", c1.fuel_type)

# -----------------------------------

# 3. Polymorphism

# Same function works differently

# based on inputs

# -----------------------------------

def add(a, b=0, c=0):
return a + b + c

print(add(10))
print(add(10, 20))
print(add(10, 20, 30))

# Using \*args = multiple values

def add(\*numbers):
return sum(numbers)

print(add(10))
print(add(10, 20))
print(add(10, 20, 30))
