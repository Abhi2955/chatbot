#!/usr/bin/python3
# module chatbot 
# by ABHISHEK BISHNOI 
import speech_recognition # google speech recognigation
from chatterbot import ChatBot #importing chatbot 
from chatterbot.trainers import ListTrainer #method to train chatbot
import os 
import pyttsx3 # this is module to convert text to speech
import google_search # this module is developed for searching on google 
import weather_search #this module is developed for searching about weather
import wiki_search
import load_cities #this modules is used to load cities
# operational function 
# fun_humidity is used for checking humidity in weather 
def fun_humidity():
	strres=str(response)
	strlen=len(strres)
	finalstr=request[strlen:]
	print(finalstr)
	humdty = weather_search.humidityWeather(finalstr[0:])
	print(humdty)
	speak(humdty)
# fun_temp is used for checking temprature in weather 
def fun_temp():
	strres=str(response)
	strlen=len(strres)
	finalstr=request[strlen:]
	temp = weather_search.tempWeather(finalstr[0:])
	print(temp+"\n")
	speak(temp)
#fun_weather is know whole report of weather 
def fun_weather():
	strres=str(response)
	strlen=len(strres)
	finalstr=request[strlen:]
	status = weather_search.statusWeather(finalstr[0:])
	print(status)
	speak(status)
#fun fun_complete_weather() is for all over weather
def fun_complete_weather():
	strres=str(response)
	strlen=len(strres)
	finalstr=request[strlen:]
	report = weather_search.completeWeather(finalstr[0:])
	print(report+"\n")
	speak(report)
def fun_wind_speed():
	strres=str(response)
	strlen=len(strres)
	finalstr=request[strlen:]
	wspeed = weather_search.wspeedWeather(finalstr[0:])
	print(wspeed)
	speak(wspeed)
def fun_wind_pressure():
	strres=str(response)
	strlen=len(strres)
	finalstr=request[strlen:]
	press = weather_search.pressureWeather(finalstr[0:])
	print(press)
	speak(press)
# defining various function for its featurs:
# this part is text to speech convertor
engine = pyttsx3.init()#engine instance will use the given driver
rate = engine.getProperty('rate')
engine.setProperty('rate', rate) # this function is used to set the rate of speech
def speak(text):
	engine.say(text)
	engine.runAndWait()
# this part is written for google speech recognigation
identifier = speech_recognition.Recognizer() 
#loading speech recognizer function from google speech recognizer
def listencommand():
	print("speak: ")
	with speech_recognition.Microphone() as source:
		identifier.adjust_for_ambient_noise(source)
		#removes noise from source 
		audio=identifier.listen(source)
		# this will convert source data to audio format 
	try:
		return identifier.recognize_google(audio)
		# this will return text converted from audio file
	except speech_recognition.UnknownValueError:
		#when their is any exception
		print ("I'm waiting for your command")

	return ""
pressure = "how much is the weather pressure in "
# main code starts here
bot = ChatBot('module chatbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.5,
            # thresold value is used for confidence level
            'default_response': 'I am sorry, but I do not understand.'
            # default_response will be sent is confidence level will below 70%
        }
    ],
    trainer='chatterbot.trainers.ListTrainer') # creating chatbot
bot.set_trainer(ListTrainer) #setting the trainer
# defining method of input
print("press 1 for text input\npress 2 for voice input")
choice=int(input("choice: "))
# string
google="google"
# this is testing part of bot 
while (True):
	if(choice==1):
		request = input('you: ') # user requesting here with a message
	else:
		request=listencommand()

	response = bot.get_response(request) #bot responding to their request
	# action based on response of bot
	if(response=="bye"):
		#
		strrespo=str(response)+" Happy to help you"
		print('Bot: ',strrespo) # printing the response of Bot
		speak(strrespo)
		break
	elif(request==google+request[6:]):
		speak("here we go")
		google_search.search(request[6:])
	elif(response=="google on" or response=="google about" 
		or response=="google it" or response=="google this" or 
		response=="search on google"):
		#
		print(response)
		strres=str(response)
		strlen=len(strres)
		finalstr=request[strlen:]
		speak("here we go")
		google_search.search(finalstr[0:])
	elif(response=="wiki about" or response=="wikipedia about" or 
		response=="tell me about" or response=="tell me" or response=="who is" or 
		response=="what is a" or response=="what is an" or response=="wikipedia" or 
		response=="wiki on" or response=="what is"):
		#
		strres=str(response)
		strlen=len(strres)
		finalstr=request[strlen:]
		speak("sure")
		data = wiki_search.wiki(finalstr[0:])
		print ("Bot: ",data)
		speak(data)
	elif(response=="what is the humidity in" or response=="what is the humidity of" or response=="what is the humidity at" or response=="humidity at"):
		fun_humidity()
	elif(response=="humidity in" or response=="humidity of" or response=="tell me humidity of" or response=="tell me humidity in" or response=="tell me humidity at"):
		fun_humidity()
	elif(response=="what is the temperature in" or response=="what is the temperature of" or response=="what is the temperature at"):
		fun_temp()
	elif(response=="temperature of" or response=="temperature at" or response=="temperature in" or response=="tell me temperature of"):
		fun_temp()
	elif(response=="tell me temperature in" or response=="tell me temperature at"):
		fun_temp()
	elif(response=="tell me weather forecast of" or response=="weather forecast of" or response=="tell me weather of" or response=="weather of" ):
		fun_complete_weather()
	elif(response=="weather in" or response=="tell me weather in" or response=="the weather in"):
		fun_complete_weather()
	elif(response=="how is the weather in" or response=="how is the weather of" or response=="how is the weather at" or response=="weather status of" or response=="weather status at" or response=="weather status in"):
		fun_weather()
	elif(response=="tell me weather status at" or response=="what is weather staus of" or response=="what is weather staus in" or response=="what is weather staus at" or response=="tell me weather status of"):
		fun_weather()
	elif(response=="status of weather in" or response=="status of weather of" or response=="status of weather at" or response=="tell me weather status in"):
		fun_weather()
	elif(response=="what is the wind speed in" or response=="what is the wind speed of" or response=="what is the wind speed at"):
		fun_wind_speed()
	elif(response=="wind speed of" or response=="wind speed in" or response=="tell me wind speed at" or response=="tell me wind speed of" or response=="tell me wind speed in"):
		fun_wind_speed()
	elif(response=="how much is the weather pressure in" or response=="how much is the weather pressure at" or response=="how much is the weather pressure of" or response=="tell me weather pressure of"):
		fun_wind_pressure()
	elif(response=="weather pressure in" or response=="weather pressure of" or response=="weather pressure at" or response=="tell me weather pressure in" or response=="tell me weather pressure at"):
		fun_wind_pressure()
	else:	
		print('Bot: ',response) # printing the response of Bot
		speak(response)