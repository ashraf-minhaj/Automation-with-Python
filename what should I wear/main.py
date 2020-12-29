"""
** Ask your robot what to wear before you go out **

	This Robot checks weather data and suggests 
	you what kind of clothes to wear.

	author : Ashraf Minhaj
	email  : ashraf_minhaj@yahoo.com
"""

"""
install -
$ pip install speechRecognition
$ pip install pyttsx3
"""

import speech_recognition as sr      # voice recognition library
import requests                      # to make get requests
import pyttsx3                       # to talk back

# get your API Key from http://openweathermap.org 
# url = api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}
url = "http://api.openweathermap.org/data/2.5/weather?q=Dhaka,bd&appid=****************"

listener = sr.Recognizer()      # initialize speech recognition API
engine = pyttsx3.init()         # init pyttsx3 engine

print("[Hi, I'm alice, your very own clothing assistant robot]")

while 1:   # runs forever (CTRL+C to exit)
	with sr.Microphone() as source:                 # get input from mic

		voice = listener.listen(source)             # listen from microphone
		command = listener.recognize_google(voice)  # use google API
		command = command.lower()                   # all words lowercase- so that we can process easily
		print(command)

		# it's purpose is to know about weather, so we load it here
		response = requests.get(url)
		data = response.json()

        # process data
		if command == 'what should i wear today':
			# if user asks what the robot
			if data['main']['humidity'] >= 80:
				engine.say("ummm, it may rain today, better take an umbrellay unless you want to have shower in the rain.")
				engine.runAndWait()
				#continue

			temp = data['main']['temp'] - 273.15
            
			if temp >= 27:
				engine.say("It's pretty hot out there, better wear light clothes, or nothing!")
				engine.runAndWait()
				continue

			if temp <= 23:
				engine.say("It's cold out there, put on some clothes.")
				engine.runAndWait()
				continue

		else:
			engine.say("Pleae say again")
			engine.runAndWait()