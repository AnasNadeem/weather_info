import sqlite3
import hashlib

class UserManagement:
  def __init__(self, username, password):
    self.username = username
    self.password = password

  def check_user(self):
    pass_hash = hashlib.sha256(self.password.encode()).hexdigest()
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    try:
        cur.execute('SELECT * FROM user where username=? and password=?', (self.username, pass_hash))
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
        print(all_data)
    except Exception as ex:
        print(f'Error due to {str(ex)}')

  def create_new_user(self):
    pass_hash = hashlib.sha256(self.password.encode()).hexdigest()
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    try:
        cur.execute('SELECT * FROM user where username=?', (self.username,))
        row_db = cur.fetchone()
        if row_db != None:
            print(f'Username is already in use.')
        else:
            cur.execute("""
            INSERT INTO user(username, password)
            VALUES (?,?)
            """, (self.username, pass_hash)
            )
            con.commit()
            print('User created.')
    except Exception as ex:
        print(f'Error due to {str(ex)}')

  def update_user(self):
    pass_hash = hashlib.sha256(self.password.encode()).hexdigest()
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    try:
        cur.execute('SELECT * FROM user where username=?', (self.username,))
        row_db = cur.fetchone()
        if row_db == None:
            print(f'Invalid Username.')
        else:
            cur.execute("""
            UPDATE user SET 
            password=?
            WHERE username=?
            """, (pass_hash,self.username)
            )
            con.commit()
            print(f'{self.username} user has been updated.')
    except Exception as ex:
        print(f'Error due to {str(ex)}')

  def del_user(self):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    try:
        cur.execute('DELETE FROM user WHERE username=?', self.username)
        con.commit()
        print(f'User {self.username} has been deleted.')
    except Exception as ex:
        print(f'Error due to {str(ex)}')
