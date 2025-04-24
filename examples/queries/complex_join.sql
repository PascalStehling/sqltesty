-- Complex join query with multiple tables
WITH recent_orders AS (
    SELECT 
        customer_id,
        product_id,
        order_date,
        quantity
    FROM orders
    WHERE order_date >= '2023-01-01'
)

SELECT 
    c.customer_name,
    c.customer_segment,
    p.product_name,
    p.category_name,
    ro.order_date,
    ro.quantity,
    p.price,
    (ro.quantity * p.price) AS total_amount,
    s.store_name,
    s.region
FROM recent_orders ro
JOIN customers c ON ro.customer_id = c.customer_id
JOIN products p ON ro.product_id = p.product_id
JOIN stores s ON c.preferred_store_id = s.store_id
WHERE 
    c.customer_segment = 'Premium' AND
    p.category_name IN ('Electronics', 'Home Appliances')
ORDER BY 
    total_amount DESC,
    ro.order_date DESC;