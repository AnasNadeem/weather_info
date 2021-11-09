from user_management import UserManagement
from weather import weather_data

print('Please login to continue to the application.')
username = input('Username: ')
password = input('Password: ')
user = UserManagement()
if user.check_user(username=username, password=password):
  print('Welcome to the application.')
  check_command = input("Enter the command:\n U to enter in UMS\n W to know the Weather data\n H to know all the commands.\n")
  if check_command=='U':
    print("""Welcome to the user management.
      Following are the commands: 
      create (to create a new user)
      list (to list all users)
      delete (to delete a user)
      update (to update a user username or password)
      """)
    user_cmnd = input()
    if user_cmnd=='create':
      new_username = input("Username: ")
      new_pass = input("Password: ")
      new_user = UserManagement()
      new_user.create_new_user(username=new_username,password=new_pass)

    elif user_cmnd=='list':
      user=UserManagement()
      user.list_user()

    elif user_cmnd=='delete':
      username = input("Username: ")
      user=UserManagement()
      user.del_user(username=username)

    elif user_cmnd=='update':
      username = input("Current Username: ")
      user=UserManagement()
      user.update_user(username=username)
      
    else:
      print("Command not found.")

  elif check_command=='W':
    print('Welcome to the weather application.\nPress 1 for Location(lat/long), 2 for city name')
    know_command = int(input())
    weather_data(know_command)

  elif check_command=='H':
    print("Enter the command:\n U to enter in UMS\n W to know the Weather data\n H to know all the commands.\n")

  else:
    print('Incorrect command. Use --help to know more.')

else:
  print('Incorrect Details.')
