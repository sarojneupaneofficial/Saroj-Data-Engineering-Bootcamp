# Day 2 Practice Questions with Answers

# -----------------------------------
# 1. Encapsulation
# Create class Student with private marks
# -----------------------------------

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks

    def get_marks(self):
        return self.__marks


s1 = Student(70)
s1.set_marks(90)

print("Marks:", s1.get_marks())


# -----------------------------------
# 2. Inheritance
# Parent class Animal
# Child class Dog
# -----------------------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


d1 = Dog("Tommy", "Labrador")

print("Name:", d1.name)
print("Breed:", d1.breed)
d1.sound()


# -----------------------------------
# 3. Inheritance
# Parent class Vehicle
# Child class Bike
# -----------------------------------

class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


b1 = Bike("Yamaha", "R15")

print("Brand:", b1.brand)
print("Model:", b1.model)


# -----------------------------------
# 4. Polymorphism
# Same function with different inputs
# -----------------------------------

def multiply(a, b=1, c=1):
    return a * b * c


print(multiply(5))
print(multiply(5, 2))
print(multiply(5, 2, 3))


# -----------------------------------
# 5. *args Example
# Accept multiple values
# -----------------------------------

def total(*numbers):
    return sum(numbers)


print(total(10))
print(total(10, 20))
print(total(10, 20, 30))
