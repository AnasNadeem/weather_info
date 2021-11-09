import sqlite3
import hashlib
def create_db():
  conn = sqlite3.connect(database='user.db')
  cur = conn.cursor()
  cur.execute("""
    CREATE TABLE IF NOT EXISTS user(
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
    )
  """)
  username = 'test'
  password = 'test'
  pass_hash = hashlib.sha256(password.encode()).hexdigest()
  cur.execute("""
    INSERT INTO user(username, password)
    VALUES (?,?)
    """, (username, pass_hash)
    )
  conn.commit()

create_db()