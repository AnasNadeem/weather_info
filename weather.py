import requests, os
from datetime import date, timedelta

API_KEY = os.environ['API_KEY']
def weather_data(n):
  if n>2 or n<=0:
    print('Sorry command not found.')
  else:
    if n==1:
      exclude_param_query = "minutely,hourly,alerts"
      latitude = input('Latitude: ')
      longitude = input('Longitude: ')
      weather_params = {'lat':latitude,'lon':longitude,'exclude':exclude_param_query,'appid':API_KEY}
      weather_request = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=weather_params).json()
      inp_date = input('Date(YYYY-MM-DD): Leave it empty if you need current data: ')
      show_weather_data(inp_date, weather_request)
    elif n==2:
      city_name = input('Please enter the city name.')
      weather_params = {'q':city_name,'appid':API_KEY}
      weather_request = requests.get('http://api.openweathermap.org/data/2.5/weather', params=weather_params).json()
      main = weather_request['main']
      humidity = main['humidity']
      pressure = main['pressure']
      avg_temp = (main['temp_min'] + main['temp_max'])/2
      wind = weather_request['wind']
      wind_speed = wind['speed']
      wind_deg = wind['deg']
      # UV Index not available in current weather api.
      print(f" Humidity: {humidity} \n Pressure: {pressure} \n Average Temp: {avg_temp} \n Wind Speed: {wind_speed} \n Wind Degree: {wind_deg}")


def show_weather_data(inp_date, weather_request):
  if inp_date=="":
    crnt_weather_data = weather_request['current']
    humidity = crnt_weather_data['humidity']
    pressure = crnt_weather_data['pressure']
    avg_temp = crnt_weather_data['temp']
    wind_speed = crnt_weather_data['wind_speed']
    wind_deg = crnt_weather_data['wind_deg']
    uv_index = crnt_weather_data['uvi']
    print(humidity, pressure, avg_temp, wind_speed, wind_deg, uv_index)
  else:
    try:
      inp_date_date = date.fromisoformat(inp_date)
      max_date = date.today() + timedelta(days=7)
      diff_date = (inp_date_date-date.today()).days
      if inp_date_date<max_date:
        weather_data = weather_request['daily']
        crnt_weather_data = weather_data[diff_date]
        humidity = crnt_weather_data['humidity']
        pressure = crnt_weather_data['pressure']
        temp = crnt_weather_data['temp']
        avg_temp = (temp['min'] + temp['max'])/2
        wind_speed = crnt_weather_data['wind_speed']
        wind_deg = crnt_weather_data['wind_deg']
        uv_index = crnt_weather_data['uvi']
        print(f" Humidity: {humidity} \n Pressure: {pressure} \n Average Temp: {avg_temp} \n Wind Speed: {wind_speed} \n Wind Degree: {wind_deg}\n UV: {uv_index}")
      else:
        print('No data available for that date.')

    except Exception as ex:
      print(f'Error due to {str(ex)}')