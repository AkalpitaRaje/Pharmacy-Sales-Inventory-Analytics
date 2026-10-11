import pandas as pd
import matplotlib.pyplot as plt

# Load final dataset
df = pd.read_csv("Data/pharmacy_sales_inventory_final.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])


# ==========================================
# 1. Top 10 Selling Medicines
# ==========================================

top_medicines = (
    df.groupby("Medicine_Name")["Quantity_Sold"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

top_medicines.sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Selling Medicines")
plt.xlabel("Quantity Sold")
plt.ylabel("Medicine")

plt.tight_layout()
plt.show()


# ==========================================
# 2. Revenue by Category
# ==========================================

category_revenue = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

category_revenue.plot(
    kind="bar"
)

plt.title("Revenue by Medicine Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ==========================================
# 3. Monthly Revenue Trend
# ==========================================

monthly_revenue = (
    df.groupby(df["Date"].dt.month)["Revenue"]
    .sum()
)

plt.figure(figsize=(10, 5))

monthly_revenue.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(
    monthly_revenue.index
)

plt.grid(True)

plt.tight_layout()
plt.show()


# ==========================================
# 4. Supplier-wise Revenue
# ==========================================

supplier_revenue = (
    df.groupby("Supplier")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))

supplier_revenue.plot(
    kind="bar"
)

plt.title("Supplier-wise Revenue")
plt.xlabel("Supplier")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()