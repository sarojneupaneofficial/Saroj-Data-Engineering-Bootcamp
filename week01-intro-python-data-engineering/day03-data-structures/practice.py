# Exercise 1: List Manipulation
# Create a list of 5 numbers
nums = [10, 20, 30, 40, 50]

# Add a new number
nums.append(60)

# Remove one number
nums.remove(20)

# Print updated list
print("Updated List:", nums)

# Exercise 2: Remove Duplicates using Set

# List with duplicates
data = [1, 2, 2, 3, 4, 4, 5]

# Convert to set to remove duplicates
unique_data = set(data)

print("Unique Values:", unique_data)

# Exercise 3: Dictionary Practice


# Create student dictionary
student = {
    "name": "Saroj",
    "age": 24,
    "course": "Data Engineering"
}

# Access values
print("Name:", student["name"])
print("Age:", student["age"])

# Exercise 4: Update Dictionary

# Add new key-value
student = {
    "name": "Saroj",
    "age": 24
}

student["city"] = "Toronto"

print("Updated Student:", student)
