
-- Total Orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- Total Customers
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM orders;

-- Order Status Distribution
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;

-- Monthly Orders Trend
SELECT
    DATE_TRUNC('month', order_purchase_timestamp) AS order_month,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_month
ORDER BY order_month;

-- Delayed Deliveries
SELECT COUNT(*) AS delayed_orders
FROM orders
WHERE order_delivered_customer_date > order_estimated_delivery_date;