import sqlite3
import hashlib

class UserManagement:
  def check_user(self, username, password):
    pass_hash = hashlib.sha256(password.encode()).hexdigest()
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    try:
      cur.execute('SELECT * FROM user where username=? and password=?', (username, pass_hash))
      row_data = cur.fetchone()
      if row_data!=None:
          return True
      else:
          return False          
    except Exception as ex:
      print(f'Error due to {str(ex)}')

  def list_user(self):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    try:
      cur.execute('SELECT * FROM user')
      all_data = cur.fetchall()
      for data in all_data:
        print(f"{data[0]}")
    except Exception as ex:
      print(f'Error due to {str(ex)}')

  def create_new_user(self, username, password):
    pass_hash = hashlib.sha256(password.encode()).hexdigest()
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    try:
      cur.execute('SELECT * FROM user where username=?', (username,))
      row_db = cur.fetchone()
      if row_db != None:
        print(f'Username is already in use.')
      else:
        cur.execute("""
        INSERT INTO user(username, password)
        VALUES (?,?)
        """, (username, pass_hash)
        )
        con.commit()
        print('User created.')
    except Exception as ex:
      print(f'Error due to {str(ex)}')

  def update_user(self, username, password):
    pass_hash = hashlib.sha256(password.encode()).hexdigest()
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    try:
      cur.execute('SELECT * FROM user where username=?', (username,))
      row_db = cur.fetchone()
      if row_db == None:
        print(f'Invalid Username.')
      else:
        cur.execute("""
        UPDATE user SET 
        password=?
        WHERE username=?
        """, (pass_hash,username)
        )
        con.commit()
        print(f'{username} user has been updated.')
    except Exception as ex:
      print(f'Error due to {str(ex)}')

  def del_user(self, username):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    try:
      cur.execute('DELETE FROM user WHERE username=?', (username, ))
      con.commit()
      print(f'User {username} has been deleted.')
    except Exception as ex:
      print(f'Error due to {str(ex)}')
