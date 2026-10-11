import pandas as pd

# Load final dataset
df = pd.read_csv("Data/pharmacy_sales_inventory_final.csv")

# Convert date columns
df["Date"] = pd.to_datetime(df["Date"])
df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"])

# ------------------------------------
# 1. Expiring Soon Records
# ------------------------------------

expiring_soon = df[
    df["Expiry_Status"] == "Expiring Soon"
].copy()

print("\n--- Medicines Expiring Soon ---")

print(
    expiring_soon[
        [
            "Medicine_Name",
            "Category",
            "Stock_Available",
            "Expiry_Date",
            "Days_To_Expiry"
        ]
    ].sort_values("Days_To_Expiry").to_string(index=False)
)


# ------------------------------------
# 2. Number of Expiring Soon Records
# ------------------------------------

print("\n--- Expiring Soon Records ---")
print(len(expiring_soon))


# ------------------------------------
# 3. Expired Records
# ------------------------------------

expired = df[
    df["Expiry_Status"] == "Expired"
]

print("\n--- Expired Records ---")
print(len(expired))


# ------------------------------------
# 4. Expiry Status Summary
# ------------------------------------

print("\n--- Expiry Status Summary ---")

print(
    df["Expiry_Status"].value_counts()
)


# ------------------------------------
# 5. Total Stock in Expiring Soon Items
# ------------------------------------

expiring_stock = expiring_soon["Stock_Available"].sum()

print("\n--- Stock in Expiring Soon Items ---")
print(expiring_stock)