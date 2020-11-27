""" Auto join online classes - Google Meet

*Simplest and the most hassle free way to join online classes automatically*

author: ashraf minhaj
mail: ashraf_minhaj@yahoo.com
"""

"""
install -
$ pip insall pyautogui
$ pip install webbrowser
"""

import webbrowser
import pyautogui
from time import sleep

class_url = "https://meet.google.com/yge-wimu-jpc?authuser=0&hs=179"

# variables
# run the get_x_y.py code and save all the coordinates
mic_x, mic_y = 408, 606            # mic button
cam_x, cam_y = 490, 606            # camera button
join_x, join_y = 990, 442          # join button


webbrowser.open(class_url)
sleep(15)                   # wait for 15 seconds, depends on net connection
#print("loaded")

# silent the mic
pyautogui.moveTo(mic_x, mic_y)
pyautogui.click()

# turn off video
pyautogui.moveTo(cam_x, cam_y)
pyautogui.click()

# Finally Join video
pyautogui.moveTo(join_x, join_y)
pyautogui.click()