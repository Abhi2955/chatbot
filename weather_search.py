#!/usr/bin/python3
#writer: Abhishek Bishnoi
# importing open weather msp library
import pyowm
#api key to access api 
owm = pyowm.OWM('a3ac1a7d13422b804a326029769907f2')
# this function returns all values 
def common(city):
    global observation,weather,status,temperature,wind_speed,humidity,pressure
    observation = owm.weather_at_place(city)
    weather = observation.get_weather()
    status = weather.get_status()
    temperature = weather.get_temperature('celsius')['temp']
    wind_speed = weather.get_wind()['speed']
    humidity = weather.get_humidity()
    pressure = weather.get_pressure()['press']
# this is used to get complete weather
def completeWeather(city):
   global wind_speed,status,temperature,humidity,pressure
   common(city)
   return "The weather in "+city+" is "+status+" with temperature of "+str(temperature)+" degree Celsius "+"with wind speed of "+str(wind_speed)+" meter per second "+"and with humidity of "+str(humidity)+" %"+" and with "+str(pressure)+" Atmospheric pressure."
# this function is used to know status about weather in a particular city
def statusWeather(city):
    global status
    common(city)
    return "The weather in "+city+" is "+status
# this function is used to find temprature of a city 
def tempWeather(city):
    global temperature
    common(city)
    return "The temperature in "+city+" is "+str(temperature)+" degree Celsius"
# this function is used to find wind speed of any city 
def wspeedWeather(city):
    global wind_speed
    common(city)
    return "The wind speed in "+city+" is "+str(wind_speed)+" meter per second"
# this function is used to find humidity of any city
def humidityWeather(city):
    global humidity
    common(city)
    return "The humidity in "+city+" is "+str(humidity)+"%"
# this function gives the value of pressure in city 
def pressureWeather(city):
    global pressure
    common(city)
    return "The pressure in "+city+" is "+str(pressure)+" Atmospheric pressure."
