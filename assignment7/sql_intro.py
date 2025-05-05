import sqlite3

def create_tables():
    try:
        conn = sqlite3.connect("../db/magazines.db")
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
        );
        """)

        conn.commit()
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error:", e)
    finally:
        conn.close()

# Task 3
def add_publisher(conn, name):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM publishers WHERE name = ?", (name,))
        if cursor.fetchone():
            print(f"Publisher '{name}' already exists.")
            return
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except Exception as e:
        print(f"Error adding publisher: {e}")

def add_magazine(conn, name, publisher_id):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM magazines WHERE name = ?", (name,))
        if cursor.fetchone():
            print(f"Magazine '{name}' already exists.")
            return
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
    except Exception as e:
        print(f"Error adding magazine: {e}")

def add_subscriber(conn, name, address):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone():
            print(f"Subscriber '{name}' at '{address}' already exists.")
            return
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    except Exception as e:
        print(f"Error adding subscriber: {e}")

def add_subscription(conn, subscriber_id, magazine_id, expiration_date):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 1 FROM subscriptions 
            WHERE subscriber_id = ? AND magazine_id = ? AND expiration_date = ?
        """, (subscriber_id, magazine_id, expiration_date))
        if cursor.fetchone():
            print("Subscription already exists.")
            return
        cursor.execute("""
            INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
        """, (subscriber_id, magazine_id, expiration_date))
    except Exception as e:
        print(f"Error adding subscription: {e}")

# Task 4
def get_all_subscribers(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM subscribers")
        rows = cursor.fetchall()
        print("\nAll Subscribers:")
        for row in rows:
            print(row)
    except Exception as e:
        print("Error retrieving subscribers:", e)

def get_all_magazines_sorted(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines ORDER BY name ASC")
        rows = cursor.fetchall()
        print("\nAll Magazines (sorted by name):")
        for row in rows:
            print(row)
    except Exception as e:
        print("Error retrieving magazines:", e)

def get_magazines_by_publisher(conn, publisher_name):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT magazines.magazine_id, magazines.name 
            FROM magazines
            JOIN publishers ON magazines.publisher_id = publishers.publisher_id
            WHERE publishers.name = ?
        """, (publisher_name,))
        rows = cursor.fetchall()
        print(f"\nMagazines by publisher '{publisher_name}':")
        for row in rows:
            print(row)
    except Exception as e:
        print("Error retrieving magazines by publisher:", e)


if __name__ == "__main__":
    create_tables()

    # Task 3
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")

    add_publisher(conn, "Penguin")
    add_publisher(conn, "National Geographic")
    add_publisher(conn, "Time Inc")

    add_magazine(conn, "Nature", 1)
    add_magazine(conn, "Science Weekly", 2)
    add_magazine(conn, "Time", 3)

    add_subscriber(conn, "Alice Smith", "123 Maple St")
    add_subscriber(conn, "Bob Jones", "456 Oak St")
    add_subscriber(conn, "Alice Smith", "789 Pine St")

    add_subscription(conn, 1, 1, "2025-12-31")
    add_subscription(conn, 1, 2, "2025-10-15")
    add_subscription(conn, 2, 3, "2025-08-01")

    conn.commit()
    conn.close()

    # Task 4
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")

    get_all_subscribers(conn)
    get_all_magazines_sorted(conn)
    get_magazines_by_publisher(conn, "Penguin")

    conn.close()

