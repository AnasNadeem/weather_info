from user_management import UserManagement
import requests, json
import os

API_KEY = os.environ['API_KEY']
print('Please login to continue to the application.')
username = input('Username: ')
password = input('Password: ')
user = UserManagement()
if user.check_user(username=username, password=password):
  print('Welcome to the application.')
  check_command = input("Enter the command:\n --user to enter in UMS\n --weather to know the Weather data\n --help to know all the commands.")
  if check_command=='--user':
    print("""Welcome to the user management. Command
      create <username> <password>
      list (to list all users)
      delete <username> <password>
      update <current_username> <new_password>
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
      username = input("Username: ")
      password = input("New Password: ")
      user=UserManagement()
      user.update_user(username=username, password=password)     
    else:
      print("Command not found.")
  elif check_command=='--weather':
    print('Welcome to the weather application.\nPress 1 for Location(lat/long), 2 for city name')
    know_command = int(input())
    def weather_data(n):
      if n>2 or n<=0:
        print('Sorry command not found.')
      else:
        if n==1:
          latitude = input('Please input the lattitude.')
          longitude = input('Please input the longitude.')
          weather_params = {'lat':latitude,'lon':longitude,'appid':API_KEY}
          weather_request_json = requests.get('http://api.openweathermap.org/data/2.5/weather', params=weather_params).text
        elif n==2:
          city_name = input('Please enter the city name.')
          weather_params = {'q':city_name,'appid':API_KEY}
          weather_request_json = requests.get('http://api.openweathermap.org/data/2.5/weather', params=weather_params).text
        weather_request = json.loads(weather_request_json)
        main = weather_request['main']
        humidity = main['humidity']
        pressure = main['pressure']
        avg_temp = (main['temp_min'] + main['temp_max'])/2
        wind = weather_request['wind']
        wind_speed = wind['speed']
        wind_deg = wind['deg']
        # 6. UV Index
        print(f" Humidity: {humidity} \n Pressure: {pressure} \n Average Temp: {avg_temp} \n Wind Speed: {wind_speed} \n Wind Degree: {wind_deg}")
    weather_data(know_command)
  elif check_command=='--help':
      print("Enter the command:\n --user to enter in UMS\n --weather to know the Weather data\n --help to know all the commands")
  else:
      print('Incorrect command. Use --help to know more.')
else:
    print('Incorrect Details.')
