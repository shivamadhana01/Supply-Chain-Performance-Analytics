import pandas as pd
import numpy as np

print("=" * 50)
print("SUPPLY CHAIN DATA CLEANING PIPELINE")
print("=" * 50)

# Load datasets
orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")
inventory = pd.read_csv("inventory.csv")
suppliers = pd.read_csv("suppliers.csv")
warehouses = pd.read_csv("warehouses.csv")

print("\nDataset Shapes")
print("Orders:", orders.shape)
print("Products:", products.shape)
print("Inventory:", inventory.shape)
print("Suppliers:", suppliers.shape)
print("Warehouses:", warehouses.shape)

# Standardize column names
orders.columns = orders.columns.str.lower().str.strip()
products.columns = products.columns.str.lower().str.strip()
inventory.columns = inventory.columns.str.lower().str.strip()
suppliers.columns = suppliers.columns.str.lower().str.strip()
warehouses.columns = warehouses.columns.str.lower().str.strip()

print("\nChecking Missing Values")
print(orders.isnull().sum())

print("\nChecking Duplicate Records")
print("Before:", len(orders))

orders.drop_duplicates(inplace=True)

print("After:", len(orders))

# Convert date columns if present
date_cols = ["order_date", "delivery_date"]

for col in date_cols:
    if col in orders.columns:
        orders[col] = pd.to_datetime(
            orders[col],
            errors="coerce"
        )

# Delivery Days Calculation
if (
    "order_date" in orders.columns and
    "delivery_date" in orders.columns
):
    orders["delivery_days"] = (
        orders["delivery_date"] -
        orders["order_date"]
    ).dt.days

# Revenue Calculation
if (
    "quantity" in orders.columns and
    "unit_price" in orders.columns
):
    orders["revenue"] = (
        orders["quantity"] *
        orders["unit_price"]
    )

# Profit Estimation
if "revenue" in orders.columns:
    orders["estimated_cost"] = (
        orders["revenue"] * 0.75
    )

    orders["profit"] = (
        orders["revenue"] -
        orders["estimated_cost"]
    )

# Save cleaned data
orders.to_csv(
    "cleaned_orders.csv",
    index=False
)

print("\nCleaning Completed Successfully")
print("Cleaned file saved as cleaned_orders.csv")
