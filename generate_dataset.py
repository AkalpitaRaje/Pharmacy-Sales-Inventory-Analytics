import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Reproducible results
np.random.seed(42)

# Number of records
num_records = 1200

# Medicine details
medicines = [
    "Paracetamol",
    "Amoxicillin",
    "Cetirizine",
    "Azithromycin",
    "Ibuprofen",
    "Pantoprazole",
    "Metformin",
    "Amlodipine",
    "Cough Syrup",
    "Vitamin C",
    "ORS",
    "Antacid",
    "Diclofenac",
    "Levocetirizine",
    "Calcium Tablets"
]

categories = [
    "Tablet",
    "Capsule",
    "Syrup",
    "Tablet",
    "Tablet",
    "Tablet",
    "Tablet",
    "Tablet",
    "Syrup",
    "Tablet",
    "Sachet",
    "Tablet",
    "Tablet",
    "Tablet",
    "Tablet"
]

suppliers = [
    "ABC Pharma",
    "MediCare Ltd",
    "HealthPlus Distributors",
    "Sunrise Pharma",
    "Wellness Drugs"
]

# Create medicine-category mapping
medicine_category = dict(zip(medicines, categories))

# Generate dates
start_date = datetime(2026, 1, 1)

dates = [
    start_date + timedelta(days=np.random.randint(0, 212))
    for _ in range(num_records)
]

# Random medicine selection
medicine_names = np.random.choice(medicines, num_records)

# Category based on medicine
category_values = [
    medicine_category[medicine]
    for medicine in medicine_names
]

# Supplier selection
supplier_values = np.random.choice(
    suppliers,
    num_records
)

# Quantity sold
quantity_sold = np.random.randint(1, 50, num_records)

# Unit price
unit_prices = np.round(
    np.random.uniform(2, 150, num_records),
    2
)

# Stock available
stock_available = np.random.randint(5, 250, num_records)

# Expiry dates
expiry_dates = [
    datetime(2026, 8, 1) + timedelta(days=np.random.randint(30, 900))
    for _ in range(num_records)
]

# Create DataFrame
df = pd.DataFrame({
    "Transaction_ID": range(10001, 10001 + num_records),
    "Date": dates,
    "Medicine_Name": medicine_names,
    "Category": category_values,
    "Supplier": supplier_values,
    "Quantity_Sold": quantity_sold,
    "Unit_Price": unit_prices,
    "Stock_Available": stock_available,
    "Expiry_Date": expiry_dates
})

# Sort by date
df = df.sort_values("Date")

# Save CSV file
df.to_csv(
    "Data/pharmacy_sales_inventory.csv",
    index=False
)

print("Dataset created successfully!")
print(f"Total records: {len(df)}")
print("File saved in Data folder.")