from user_management import UserManagement
from weather import weather_data

wanna_quit = False

def wanna_continue():
  want_to_con = input('Enter e to exit or h to go to home: ')
  if want_to_con.lower()=='e':
    wanna_quit=True
  elif want_to_con.lower()=='h':
    home()
  else:
    wanna_continue()

def home():
  username = input('Username: ')
  password = input('Password: ')
  user = UserManagement()
  genuine_user = user.check_user(username=username, password=password)
  if genuine_user:
    wanna_exit = False
    while not wanna_exit:
      print('Welcome to the application.')
      check_command = input("""Enter the command:
      U to enter in UMS
      W to know the Weather data
      L to logout
      --help to know all the commands.\n""")

      if check_command.upper()=='U':
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

      elif check_command.upper()=='W':
        print('Welcome to the weather application.\nPress 1 for Location(lat/long), 2 for city name')
        know_command = input()
        if know_command.isnumeric():
            weather_data(int(know_command))
        else:
            print('Please select correct option.')

      elif check_command.upper()=='L':
        wanna_exit=True

      elif check_command.upper()=='H':
        print("""Welcome to Help. Following are the commands:
        U to enter in UMS
        W to know the Weather data
        L to logout
        --help to know all the commands.\n""")

      else:
        print('Incorrect command. Use --help to know more.')

  else:
    print('Incorrect Details.')
    wanna_continue()


if __name__=="__main__":
  print('Please login to continue to the application.')
  home()