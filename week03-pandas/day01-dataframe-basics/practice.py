import pandas as pd

# -----------------------------------
# Q1 Create DataFrame
# -----------------------------------
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Price": [1200, 800, 500, 300, 100],
    "Sales": [5, 15, 8, 12, 20]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

# -----------------------------------
# Q2 Add Revenue Column
# -----------------------------------
df["Revenue"] = df["Price"] * df["Sales"]

print("\nWith Revenue:\n")
print(df)

# -----------------------------------
# Q3 Basic Operations
# -----------------------------------
print("\nFirst 3 Rows:")
print(df.head(3))

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# -----------------------------------
# Q4 Add New Record using loc
# -----------------------------------
df.loc[len(df)] = ["Mouse", 50, 25, 1250]

print("\nAfter Adding New Row:\n")
print(df)

# -----------------------------------
# Q5 Missing Data Handling
# -----------------------------------
df.loc[2, "Price"] = None
df.loc[4, "Sales"] = None

print("\nMissing Values Added:\n")
print(df)

print("\nDetect Missing:")
print(df.isnull())

print("\nCount Missing:")
print(df.isnull().sum())

df.fillna(0, inplace=True)

print("\nAfter fillna(0):\n")
print(df)

# -----------------------------------
# Q6 Low Sales Alert
# -----------------------------------
print("\nProducts with Sales < 10:\n")
print(df[df["Sales"] < 10])


# Output:
