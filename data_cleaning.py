import pandas as pd

# Load dataset
df = pd.read_csv("Data/pharmacy_sales_inventory.csv")

print("Original Data:")
print(df.head())

# Convert Date columns to datetime
df["Date"] = pd.to_datetime(df["Date"])
df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"])

# Check data types after conversion
print("\nData Types After Date Conversion:")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records if any
df = df.drop_duplicates()

# Sort data by Date
df = df.sort_values("Date")

# Save cleaned dataset
df.to_csv(
    "Data/pharmacy_sales_inventory_cleaned.csv",
    index=False
)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved successfully.")