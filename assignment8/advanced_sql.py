# TASK 1
import sqlite3

conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

print("\nTask 1:")
query = """
SELECT
  o.order_id,
  SUM(p.price * li.quantity) AS total_price
FROM
  orders o
JOIN
  line_items li ON o.order_id = li.order_id
JOIN
  products p ON li.product_id = p.product_id
GROUP BY
  o.order_id
ORDER BY
  o.order_id
LIMIT 5;
"""
cursor.execute(query)
for row in cursor.fetchall():
    print(f"Order ID: {row[0]}, Total Price: {row[1]}")


#TASK2
print("\nTask 2:")
query = """
SELECT
  c.customer_name,
  AVG(order_totals.total_price) AS average_total_price
FROM
  customers c
LEFT JOIN (
  SELECT
    o.customer_id AS customer_id_b,
    SUM(p.price * li.quantity) AS total_price
  FROM
    orders o
  JOIN line_items li ON o.order_id = li.order_id
  JOIN products p ON li.product_id = p.product_id
  GROUP BY o.order_id
) AS order_totals
ON c.customer_id = order_totals.customer_id_b
GROUP BY c.customer_id;

"""

cursor.execute(query)
for row in cursor.fetchall():
    customer = row[0]
    avg_price = row[1]
    if avg_price is not None:
        print(f"Customer: {customer}, Average Order Price: {avg_price:.2f}")
    else:
        print(f"Customer: {customer}, Average Order Price: No orders")


# TASK 3
print("\nTask 3:")
cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
customer_row = cursor.fetchone()
if customer_row is None:
    print("Customer 'Perez and Sons' not found.")
else:
    customer_id = customer_row[0]

cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
employee_row = cursor.fetchone()
if employee_row is None:
    print("Employee Miranda Harris not found.")
else:
    employee_id = employee_row[0]

    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    product_ids = [row[0] for row in cursor.fetchall()]

    if len(product_ids) < 5:
        print("Not enough products in the base to create the order.")
    else:
        try:
            cursor.execute("""
                INSERT INTO orders (customer_id, employee_id, date)
                VALUES (?, ?, DATE('now'))
                RETURNING order_id
            """, (customer_id, employee_id))
            order_id = cursor.fetchone()[0]
        except sqlite3.OperationalError:
            cursor.execute("""
                INSERT INTO orders (customer_id, employee_id, date)
                VALUES (?, ?, DATE('now'))
            """, (customer_id, employee_id))
            order_id = cursor.lastrowid
        
        for product_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, 10)
            """, (order_id, product_id))
        conn.commit()

        cursor.execute("""
            SELECT li.line_item_id, li.quantity, p.product_name
            FROM line_items li
            JOIN products p ON li.product_id = p.product_id
            WHERE li.order_id = ?
        """, (order_id,))

        for row in cursor.fetchall():
            print(f"LineItem ID: {row[0]}, Quantity: {row[1]}, Product: {row[2]}")

#TASK 4
print("\nTask 4:")
query = """
SELECT
  e.employee_id,
  e.first_name,
  e.last_name,
  COUNT(o.order_id) AS order_count
FROM
  employees e
JOIN
  orders o ON e.employee_id = o.employee_id
GROUP BY
  e.employee_id, e.first_name, e.last_name
HAVING
  COUNT(o.order_id) > 5;
"""

cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(f"Employee ID: {row[0]}, Name: {row[1]} {row[2]}, Orders: {row[3]}")

cursor.close()
conn.close()