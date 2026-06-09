import pandas as pd

orders = pd.read_csv("orders.csv")

# Revenue
orders["revenue"] = (
    orders["quantity"] *
    orders["unit_price"]
)

# Delivery Time
orders["order_date"] = pd.to_datetime(
    orders["order_date"]
)

orders["delivery_date"] = pd.to_datetime(
    orders["delivery_date"]
)

orders["delivery_days"] = (
    orders["delivery_date"] -
    orders["order_date"]
).dt.days

# KPIs
total_revenue = orders["revenue"].sum()

total_orders = len(orders)

average_order_value = (
    total_revenue /
    total_orders
)

average_delivery_time = (
    orders["delivery_days"].mean()
)

total_shipping_cost = (
    orders["shipping_cost"].sum()
)

delivered_orders = (
    orders["order_status"]
    .eq("Delivered")
    .sum()
)

fulfillment_rate = (
    delivered_orders /
    total_orders
) * 100

print("=" * 50)
print("SUPPLY CHAIN KPI DASHBOARD")
print("=" * 50)

print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: {average_order_value:,.2f}")
print(f"Average Delivery Time: {average_delivery_time:.2f} Days")
print(f"Shipping Cost: {total_shipping_cost:,.2f}")
print(f"Fulfillment Rate: {fulfillment_rate:.2f}%")
