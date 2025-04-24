-- Simple count query
SELECT 
    product_category,
    COUNT(*) as product_count
FROM products
GROUP BY product_category
ORDER BY product_count DESC;