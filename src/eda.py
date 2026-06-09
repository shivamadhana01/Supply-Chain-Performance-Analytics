import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
orders = pd.read_csv("orders.csv")

# Revenue Column
orders["revenue"] = (
    orders["quantity"] *
    orders["unit_price"]
)

print("=" * 50)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# Dataset Overview
print("\nDataset Shape")
print(orders.shape)

print("\nColumns")
print(orders.columns)

# Revenue Statistics
print("\nRevenue Statistics")
print(orders["revenue"].describe())

# Order Status Analysis
print("\nOrder Status Distribution")
print(
    orders["order_status"]
    .value_counts()
)

# Top Products
top_products = (
    orders.groupby("product_id")
    ["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products")
print(top_products)

# Top Suppliers
top_suppliers = (
    orders.groupby("supplier_id")
    ["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Suppliers")
print(top_suppliers)

# Top Warehouses
top_warehouses = (
    orders.groupby("warehouse_id")
    ["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nWarehouse Performance")
print(top_warehouses)

# Monthly Revenue
orders["order_date"] = pd.to_datetime(
    orders["order_date"]
)

orders["month"] = (
    orders["order_date"]
    .dt.to_period("M")
)

monthly_revenue = (
    orders.groupby("month")
    ["revenue"]
    .sum()
)

print("\nMonthly Revenue")
print(monthly_revenue)

# Revenue Trend Plot
monthly_revenue.plot(
    figsize=(12,6),
    title="Monthly Revenue Trend"
)

plt.tight_layout()
plt.savefig(
    "monthly_revenue.png"
)

print("\nEDA Completed Successfully")
