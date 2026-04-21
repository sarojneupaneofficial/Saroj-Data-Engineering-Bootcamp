# 📁 Day 5 – Functions + OOP Practice (`day05-functions-oop-practice/notes.md`)

# Day 5 - Functions and OOP Practice

## Functions Practice

```python
def square(n):
    return n * n

print(square(5))
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(10))
OOP Practice
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(self.brand, self.model)

car1 = Car("Toyota", "Corolla")
car1.info()
```
