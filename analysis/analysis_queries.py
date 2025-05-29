import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")
total_sales = pd.read_sql("""
    SELECT Round(SUM(total_amount_gbp)) as total_sales
    FROM orders_enriched
""", conn)

print("Total Sales (GBP):")
print(total_sales)


top_products = pd.read_sql("""
    SELECT p.name, SUM(o.quantity) AS total_quantity, 
           ROUND(SUM(o.total_amount_gbp), 2) AS revenue_gbp
    FROM orders_enriched o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.name
    ORDER BY revenue_gbp DESC
    LIMIT 5
""", conn)

print("\nTop Products:")
print(top_products)
# %% 
sales_by_country = pd.read_sql(""" 
SELECT u.user_id, u.country, SUM(o.total_amount_gbp) AS total_spent, sum(o.quantity) AS quantity_purchased
FROM orders_enriched o
JOIN users u ON o.user_id = u.user_id
GROUP BY u.country
order by u.country desc
""", conn)
print("Top sales by countries")
print(sales_by_country)

left_join_check = pd.read_sql(""" Select o.order_id, o.user_id, u.country, o.total_amount_gbp
                              FROM orders_enriched o
                              LEFT JOIN users u on o.user_id = u.user_id
                              Order by o.order_id
                              """,conn)

