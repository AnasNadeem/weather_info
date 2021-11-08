import sqlite3

def create_db():
    conn = sqlite3.connect(database='user.db')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user(
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    conn.commit()

create_db()