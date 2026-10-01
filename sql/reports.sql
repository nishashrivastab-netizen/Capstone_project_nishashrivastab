(a)  SELECT 
    COUNT(*) AS total_orders,
    ROUND(SUM(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100)), 2) AS total_revenue,
    ROUND(AVG(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100)), 2) AS avg_order_value
FROM orders o
JOIN products p ON o.product_id = p.product_id;

(b)  SELECT 
    COUNT(*) AS total_rows,
    COUNT(rating) AS rated_rows,
    (COUNT(*) - COUNT(rating)) AS difference
FROM orders;

(c)  SELECT c.customer_id, c.name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) = 0;

SELECT customer_id, name
FROM customers
WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id 
    FROM orders 
    WHERE customer_id IS NOT NULL
);

(d)  SELECT 
    c.city,
    COUNT(o.order_id) AS total_orders,
    SUM(o.returned) AS returned_orders,
    ROUND((SUM(o.returned) / COUNT(o.order_id)) * 100, 1) AS return_rate_pct
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.city
HAVING return_rate_pct > 20.0
ORDER BY return_rate_pct DESC;

(e)  SELECT 
    c.customer_id,
    c.name,
    ROUND(SUM(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100)), 2) AS total_spend
FROM orders o
JOIN products p ON o.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spend DESC, c.customer_id ASC
LIMIT 5;

SELECT 
    c.customer_id,
    c.name,
    ROUND(SUM(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100)), 2) AS total_spend
FROM orders o
JOIN products p ON o.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spend DESC, c.customer_id ASC
LIMIT 3 OFFSET 2;

(f)  SELECT 
    p.category,
    COUNT(o.order_id) AS order_count,
    ROUND(SUM(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100)), 2) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY p.category
ORDER BY revenue DESC;


(g)  SELECT COUNT(*) AS customers_starting_with_A
FROM customers
WHERE name LIKE 'A%';

(h)  SELECT DISTINCT acquisition_source
FROM customers;

(i)  SET SQL_SAFE_UPDATES = 0;
ALTER TABLE customers ADD COLUMN loyalty_tier VARCHAR(10);
UPDATE customers 
SET loyalty_tier = CASE 
    WHEN city_tier = 1 THEN 'Gold' 
    ELSE 'Silver' 
END;
SET SQL_SAFE_UPDATES = 1;
SELECT loyalty_tier, COUNT(*) AS count
FROM customers
GROUP BY loyalty_tier;

