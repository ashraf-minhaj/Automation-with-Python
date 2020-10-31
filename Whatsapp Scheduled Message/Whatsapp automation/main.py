""" Send scheduled whatsapp message using python
 play youtube video

install - 
$ pip install pywhatkit

All we need is signing into whatsapp web on browser (one time)
"""

import pywhatkit
import os          # to talk with the OS

def text(number, msg, hour, minute):
	# syntax (phone_number_in_text, message, hour_format_24hr, minute)
	#pywhatkit.sendwhatmsg('+97450024398', "Hello primitive human with crushable skull, how you doin'?", 2, 20)
	pywhatkit.sendwhatmsg(number, msg, hour, minute)

def play(subject):
	""" play video from youtube on browser, latest"""
	pywhatkit.playonyt(subject)

def kill_browser():
	""" kill the browser if firefox, replace name chrome"""
	os.system("TASKKILL /F /IM chrome.exe")   

# start the day with JKR's latest video
play('jhankar mahbub')

# send your gf good morning mesage before you actually wake up,
# she will think you are an early riser and a serious guy
text('+97450024298', msg="Good morning Jaanu!", hour=6, minute=30)
print("done")
kill_browser()                        # close tabs and chrome

# text your secong gf if she had eaten her lunch
# while you are busy with ..well, the first one
text('+97450024298', msg="Babu Khaiso?", hour=13, minute=24)
print("done")
kill_browser()                           # close tabs and chrome