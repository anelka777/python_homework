import sqlite3
import pandas as pd

conn = sqlite3.connect('../db/lesson.db')

query = """
SELECT
    line_items.line_item_id,
    line_items.quantity,
    products.product_id,
    products.product_name,
    products.price
FROM line_items
JOIN products ON line_items.product_id = products.product_id
"""
df=pd.read_sql_query(query, conn)

print("First version")
print(df.head())

df['total'] = df['quantity'] * df['price']
print("\nSum (total):")
print(df.head())

summary = df.groupby('product_id').agg({
  'line_item_id': 'count',
  'total' : 'sum',
  'product_name' : 'first'
}).reset_index()

summary = summary.sort_values('product_name')
summary.to_csv('order_summary.csv', index=False)

print('\nSummary table')
print(summary.head())

conn.close()