import pandas as pd
import matplotlib.pyplot as plt

# Load final dataset
df = pd.read_csv("Data/pharmacy_sales_inventory_final.csv")

# ------------------------------------
# 1. Low Stock Records
# ------------------------------------

low_stock = df[df["Stock_Status"] == "Low Stock"]

print("\n--- Low Stock Records ---")
print(low_stock[
    [
        "Medicine_Name",
        "Stock_Available",
        "Stock_Status"
    ]
].to_string(index=False))


# ------------------------------------
# 2. Number of Low Stock Records
# ------------------------------------

print("\n--- Number of Low Stock Records ---")
print(len(low_stock))


# ------------------------------------
# 3. Stock Status Distribution
# ------------------------------------

stock_distribution = (
    df["Stock_Status"]
    .value_counts()
)

print("\n--- Stock Status Distribution ---")
print(stock_distribution)


# ------------------------------------
# 4. Average Stock by Medicine
# ------------------------------------

average_stock = (
    df.groupby("Medicine_Name")["Stock_Available"]
    .mean()
    .sort_values()
)

print("\n--- Average Stock by Medicine ---")
print(average_stock)


# ------------------------------------
# 5. Low Stock Visualization
# ------------------------------------

plt.figure(figsize=(8, 5))

stock_distribution.plot(
    kind="bar"
)

plt.title("Inventory Stock Status Distribution")
plt.xlabel("Stock Status")
plt.ylabel("Number of Records")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()