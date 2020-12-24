""" Voice Controlled Email sender Robot

* To run this program you must allow low security apps 
 from your google account on a browser.

author: ashraf minhaj
mail: ashraf_minhaj@yahoo.com
"""

""" 
install -
$ pip install speechRecognition
$ pip install pyttsx3
"""

# import necessary libraries
import speech_recognition as sr      # voice recognition library
import pyttsx3
import smtplib

# change mail address and password
sender_mail          = 'yourmail@gmail.com'
sender_mail_pass     = '############'

# mail addresses
# those mail addresses are fake
addresses = {'ashraf' : 'ashraf_minhaj@gmail.com',
             'fish' : 'dhorimachnachhuipani@yahoo.com'
			 }

# connect to server 
server = smtplib.SMTP('smtp.gmail.com', '587')
server.connect('smtp.gmail.com', '587')
server.ehlo()
server.starttls()

# login to account
server.login(sender_mail, sender_mail_pass)

# initilize tts and stt engine
engine = pyttsx3.init()
listener = sr.Recognizer()      # initialize speech recognition API


def listen():
	""" listen to what user says"""
	try:
		with sr.Microphone() as source:                 # get input from mic
			print("Talk>>")
			voice = listener.listen(source)             # listen from microphone
			command = listener.recognize_google(voice)  # use google API
			command = command.lower()                   # all words lowercase- so that we can process easily
			#print(command)
			return command
	except:
		pass

def talk(sentence):
	""" talk / respond to the user """
	engine.say(sentence)
	engine.runAndWait()

""" run """
# get command
resp = listen()

if resp == 'send mail':
	talk("Please say the reciver name")
	name = listen()
	#print(name)
	receiver_mail = addresses[name]
	#print(receiver_mail)

	talk('please say the message')
	msg = listen()
	#print(msg)

	server.sendmail(sender_mail, receiver_mail, msg)