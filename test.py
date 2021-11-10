from user_management import UserManagement
import hashlib
import sqlite3
import unittest

class TestUserManagement(unittest.TestCase):
  def setUp(self):
    self.user = UserManagement()
    self.username = 'testing' 
    self.password = 'testing'
  
  def test_create_new_user(self):
    pass_hash = hashlib.sha256(self.password.encode()).hexdigest()
    self.user.create_new_user(username=self.username, password=self.password)
    try:
      conn = sqlite3.connect(database='user.db')
      cur = conn.cursor()
      cur.execute("SELECT * FROM user where username=?", (self.username,))
      row = cur.fetchone()
      conn.commit()
      # assert pass_hash==row[1], "Hashed pass should be same."
      self.assertEqual(pass_hash, row[1])
    except Exception as ex:
      print(f'Error due to {str(ex)}')

  def test_check_user_with_correct_data(self):
    username = 'test'
    password = 'test'
    result = self.user.check_user(username=username, password=password)
    # assert result==True , "Result should be True"
    self.assertTrue(result)

  def test_del_user(self):
    self.user.del_user(username=self.username)
    try:
      conn = sqlite3.connect(database='user.db')
      cur = conn.cursor()
      cur.execute("SELECT * FROM user where username=?", (self.username,))
      row = cur.fetchall()
      # assert row==[], "Db should be empty."
      self.assertListEqual(row, [])
    except Exception as ex:
      print(f'Error due to {str(ex)}')

  def test_check_user_with_incorrect_data(self):
    username = 'kuchbhi'
    password = 'kuchbhi'
    result = self.user.check_user(username=username, password=password)
    # assert result==False , "Result should be False"
    self.assertFalse(result)

if __name__=="__main__":
  unittest.main()