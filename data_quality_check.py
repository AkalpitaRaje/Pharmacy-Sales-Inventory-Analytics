import pandas as pd

# Load dataset
df = pd.read_csv("Data/pharmacy_sales_inventory.csv")

# Display first 5 rows
print("\n--- First 5 Rows ---")
print(df.head())

# Dataset shape
print("\n--- Dataset Shape ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Column names
print("\n--- Column Names ---")
print(df.columns.tolist())

# Data types
print("\n--- Data Types ---")
print(df.dtypes)

# Missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Duplicate rows
print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

# Statistical summary
print("\n--- Statistical Summary ---")
print(df.describe())