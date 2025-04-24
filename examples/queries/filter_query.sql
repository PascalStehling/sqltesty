-- Filter query with join
SELECT 
    p.product_name,
    p.price,
    c.category_name
FROM products p
JOIN categories c ON p.product_category = c.id
WHERE p.price > 50
ORDER BY p.price DESC;