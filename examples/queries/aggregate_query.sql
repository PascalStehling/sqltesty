SELECT 
    product,
    SUM(quantity) as total_quantity,
    COUNT(*) as order_count
FROM orders
GROUP BY product
HAVING SUM(quantity) > 5
ORDER BY total_quantity DESC;