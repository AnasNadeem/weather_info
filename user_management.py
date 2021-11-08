import sqlite3
import hashlib
print('Please login to the application.')
username = input('Username: ')
password = input('Password: ')

def check_user(username, password):
    pass_hash = hashlib.sha256(password.encode()).hexdigest()
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    try:
        cur.execute('SELECT * FROM user where username=? and password=?', (username, pass_hash))
        row_data = cur.fetchone()
        if row_data!=None:
            print('True')
        else:
            print('Incorrect details.')            
    except Exception as ex:
        print(f'Error due to {str(ex)}')

def create_new_user(username, password):
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

def update_user(username, password):
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

def del_user(username):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    try:
        cur.execute('DELETE FROM user WHERE username=?', username)
        con.commit()
        print(f'User {username} has been deleted.')
    except Exception as ex:
        print(f'Error due to {str(ex)}')
