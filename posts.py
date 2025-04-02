import sqlite3

DATABASE = 'personal_site.db'  # Use the same database name as in your Flask app

# Connect to the database (this will create the database file if it doesn't exist)
conn = sqlite3.connect(DATABASE)

# Create the posts table if it doesn't exist
conn.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database initialized and 'posts' table created.")
