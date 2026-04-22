import pandas as pd

# Create DataFrame
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Price": [1200, 800, 500, 300, 100],
    "Quantity": [5, 15, 8, 12, 20]
}

df = pd.DataFrame(data)

# Add Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

# Add Price per Quantity
df["Price_per_Quantity"] = df["Price"] / df["Quantity"]

# Filter Price > 250 and sort by Revenue ascending
filtered_df = df[df["Price"] > 250].sort_values(by="Revenue", ascending=True)

print("Filtered Data:")
print(filtered_df)

# Update Laptop price by 10%
df.loc[df["Product"] == "Laptop", "Price"] *= 1.10

# Remove duplicate products
df = df.drop_duplicates("Product")

# Remove invalid data (Quantity = 0)
df = df[df["Quantity"] != 0]

# GroupBy Product and sum Revenue
grouped_df = df.groupby("Product")["Revenue"].sum()

print("\nFinal Data:")
print(df)

print("\nGrouped Revenue:")
print(grouped_df)
