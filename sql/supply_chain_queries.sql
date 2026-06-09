/* =========================================
SUPPLY CHAIN PERFORMANCE ANALYTICS
SQL BUSINESS QUERIES
========================================= */

-- 1 Total Orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- 2 Total Revenue
SELECT
SUM(quantity * unit_price) AS total_revenue
FROM orders;

-- 3 Average Order Value
SELECT
AVG(quantity * unit_price) AS avg_order_value
FROM orders;

-- 4 Total Shipping Cost
SELECT
SUM(shipping_cost) AS total_shipping_cost
FROM orders;

-- 5 Revenue by Product
SELECT
product_id,
SUM(quantity * unit_price) AS revenue
FROM orders
GROUP BY product_id
ORDER BY revenue DESC;

-- 6 Top 10 Products
SELECT
product_id,
SUM(quantity * unit_price) AS revenue
FROM orders
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;

-- 7 Lowest Performing Products
SELECT
product_id,
SUM(quantity * unit_price) AS revenue
FROM orders
GROUP BY product_id
ORDER BY revenue ASC
LIMIT 10;

-- 8 Revenue by Supplier
SELECT
supplier_id,
SUM(quantity * unit_price) AS revenue
FROM orders
GROUP BY supplier_id
ORDER BY revenue DESC;

-- 9 Top Suppliers
SELECT
supplier_id,
SUM(quantity * unit_price) AS revenue
FROM orders
GROUP BY supplier_id
ORDER BY revenue DESC
LIMIT 10;

-- 10 Warehouse Revenue
SELECT
warehouse_id,
SUM(quantity * unit_price) AS revenue
FROM orders
GROUP BY warehouse_id
ORDER BY revenue DESC;

-- 11 Warehouse Order Count
SELECT
warehouse_id,
COUNT(*) AS total_orders
FROM orders
GROUP BY warehouse_id
ORDER BY total_orders DESC;

-- 12 Delivered Orders
SELECT
COUNT(*) AS delivered_orders
FROM orders
WHERE order_status='Delivered';

-- 13 Pending Orders
SELECT
COUNT(*) AS pending_orders
FROM orders
WHERE order_status='Pending';

-- 14 Cancelled Orders
SELECT
COUNT(*) AS cancelled_orders
FROM orders
WHERE order_status='Cancelled';

-- 15 Order Status Distribution
SELECT
order_status,
COUNT(*) AS total_orders
FROM orders
GROUP BY order_status;

-- 16 Fulfillment Rate
SELECT
ROUND(
COUNT(*) * 100.0 /
(SELECT COUNT(*) FROM orders),2
) AS fulfillment_rate
FROM orders
WHERE order_status='Delivered';

-- 17 Monthly Revenue
SELECT
DATE_FORMAT(order_date,'%Y-%m') AS month,
SUM(quantity * unit_price) AS revenue
FROM orders
GROUP BY month
ORDER BY month;

-- 18 Monthly Order Count
SELECT
DATE_FORMAT(order_date,'%Y-%m') AS month,
COUNT(*) AS total_orders
FROM orders
GROUP BY month
ORDER BY month;

-- 19 Monthly Shipping Cost
SELECT
DATE_FORMAT(order_date,'%Y-%m') AS month,
SUM(shipping_cost) AS shipping_cost
FROM orders
GROUP BY month
ORDER BY month;

-- 20 Average Quantity per Order
SELECT
AVG(quantity) AS avg_quantity
FROM orders;

-- 21 Maximum Order Value
SELECT
MAX(quantity * unit_price) AS max_order_value
FROM orders;

-- 22 Minimum Order Value
SELECT
MIN(quantity * unit_price) AS min_order_value
FROM orders;

-- 23 Average Shipping Cost
SELECT
AVG(shipping_cost) AS avg_shipping_cost
FROM orders;

-- 24 Top Revenue Generating Warehouse
SELECT
warehouse_id,
SUM(quantity * unit_price) AS revenue
FROM orders
GROUP BY warehouse_id
ORDER BY revenue DESC
LIMIT 1;

-- 25 Revenue Contribution %
SELECT
product_id,
ROUND(
SUM(quantity * unit_price) *100 /
(
SELECT SUM(quantity * unit_price)
FROM orders
),2
) AS contribution_pct
FROM orders
GROUP BY product_id
ORDER BY contribution_pct DESC;

-- 26 Average Revenue by Supplier
SELECT
supplier_id,
AVG(quantity * unit_price) AS avg_revenue
FROM orders
GROUP BY supplier_id;

-- 27 Revenue by Order Status
SELECT
order_status,
SUM(quantity * unit_price) AS revenue
FROM orders
GROUP BY order_status;

-- 28 Top Shipping Cost Orders
SELECT
order_id,
shipping_cost
FROM orders
ORDER BY shipping_cost DESC
LIMIT 20;

-- 29 Revenue per Warehouse
SELECT
warehouse_id,
ROUND(
SUM(quantity * unit_price),2
) AS revenue
FROM orders
GROUP BY warehouse_id;

-- 30 Business Summary Dashboard Query
SELECT
COUNT(*) AS total_orders,
SUM(quantity * unit_price) AS revenue,
AVG(quantity * unit_price) AS avg_order_value,
SUM(shipping_cost) AS shipping_cost
FROM orders;
