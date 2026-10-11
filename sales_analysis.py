import pandas as pd

# Load final dataset
df = pd.read_csv("Data/pharmacy_sales_inventory_final.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# 1. Total Revenue
# -----------------------------

total_revenue = df["Revenue"].sum()

print("\n--- Total Revenue ---")
print(f"₹{total_revenue:,.2f}")


# -----------------------------
# 2. Total Quantity Sold
# -----------------------------

total_quantity = df["Quantity_Sold"].sum()

print("\n--- Total Quantity Sold ---")
print(total_quantity)


# -----------------------------
# 3. Top 10 Selling Medicines
# -----------------------------

top_medicines = (
    df.groupby("Medicine_Name")["Quantity_Sold"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- Top 10 Selling Medicines ---")
print(top_medicines)


# -----------------------------
# 4. Revenue by Medicine
# -----------------------------

medicine_revenue = (
    df.groupby("Medicine_Name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- Top 10 Medicines by Revenue ---")
print(medicine_revenue)


# -----------------------------
# 5. Revenue by Category
# -----------------------------

category_revenue = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Revenue by Category ---")
print(category_revenue)


# -----------------------------
# 6. Quantity Sold by Category
# -----------------------------

category_quantity = (
    df.groupby("Category")["Quantity_Sold"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Quantity Sold by Category ---")
print(category_quantity)


# -----------------------------
# 7. Monthly Revenue
# -----------------------------

monthly_revenue = (
    df.groupby(df["Date"].dt.month)["Revenue"]
    .sum()
)

print("\n--- Monthly Revenue ---")
print(monthly_revenue)


# -----------------------------
# 8. Supplier-wise Revenue
# -----------------------------

supplier_revenue = (
    df.groupby("Supplier")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Supplier-wise Revenue ---")
print(supplier_revenue)