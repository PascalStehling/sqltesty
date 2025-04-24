-- Analytics query with aggregations across multiple dimensions
WITH monthly_sales AS (
    SELECT 
        SUBSTR(o.order_date, 1, 7) AS month,
        p.category_name,
        s.region,
        c.customer_segment,
        SUM(o.quantity * p.price) AS revenue,
        COUNT(DISTINCT o.order_id) AS order_count,
        COUNT(DISTINCT o.customer_id) AS customer_count
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN stores s ON c.preferred_store_id = s.store_id
    GROUP BY 
        SUBSTR(o.order_date, 1, 7),
        p.category_name,
        s.region,
        c.customer_segment
)

SELECT 
    month,
    category_name,
    region,
    customer_segment,
    revenue,
    order_count,
    customer_count,
    revenue / NULLIF(customer_count, 0) AS avg_revenue_per_customer,
    RANK() OVER (PARTITION BY month, region ORDER BY revenue DESC) AS category_rank_in_region
FROM monthly_sales
WHERE revenue > 1000
ORDER BY
    month,
    revenue DESC,
    region,
    category_name,
    customer_segment;