""" get mouse position using this code"""

import pyautogui
from time import sleep

while True:
    print(pyautogui.displayMousePosition(), "\n")
    sleep(1)