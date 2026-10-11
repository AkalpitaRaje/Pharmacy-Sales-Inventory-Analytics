import pandas as pd

# Load cleaned dataset
df = pd.read_csv("Data/pharmacy_sales_inventory_cleaned.csv")

# Convert date columns
df["Date"] = pd.to_datetime(df["Date"])
df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"])

# 1. Calculate Revenue
df["Revenue"] = df["Quantity_Sold"] * df["Unit_Price"]

# 2. Create Stock Status
def get_stock_status(stock):
    if stock <= 20:
        return "Low Stock"
    elif stock <= 80:
        return "Medium Stock"
    else:
        return "Sufficient Stock"

df["Stock_Status"] = df["Stock_Available"].apply(get_stock_status)

# 3. Calculate days remaining until expiry
df["Days_To_Expiry"] = (
    df["Expiry_Date"] - df["Date"]
).dt.days

# 4. Create Expiry Status
def get_expiry_status(days):
    if days < 0:
        return "Expired"
    elif days <= 90:
        return "Expiring Soon"
    else:
        return "Valid"

df["Expiry_Status"] = df["Days_To_Expiry"].apply(get_expiry_status)

# 5. Create Month column
df["Month"] = df["Date"].dt.month_name()

# 6. Create Month Number
df["Month_Number"] = df["Date"].dt.month

# Display first 5 rows
print("\n--- Updated Dataset ---")
print(df.head())

# Display new columns
print("\n--- New Columns ---")
print(
    df[
        [
            "Revenue",
            "Stock_Status",
            "Days_To_Expiry",
            "Expiry_Status",
            "Month"
        ]
    ].head()
)

# Revenue summary
print("\n--- Total Revenue ---")
print(round(df["Revenue"].sum(), 2))

# Stock status summary
print("\n--- Stock Status ---")
print(df["Stock_Status"].value_counts())

# Expiry status summary
print("\n--- Expiry Status ---")
print(df["Expiry_Status"].value_counts())

# Save final analytical dataset
df.to_csv(
    "Data/pharmacy_sales_inventory_final.csv",
    index=False
)

print("\nFeature engineering completed successfully!")
print("Final dataset saved successfully.")