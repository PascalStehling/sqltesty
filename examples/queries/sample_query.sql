SELECT 
    customers.name, 
    orders.product, 
    orders.quantity
FROM customers
JOIN orders ON customers.id = orders.customer_id
WHERE orders.quantity > 5
ORDER BY orders.quantity DESC;