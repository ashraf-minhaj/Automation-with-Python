""" This little code automatically reacts through all posts
    on FaceBook """
"""
author: Ashraf Minhaj
mail: ashraf_minhaj@yahoo.com
"""

"""
facebook provides some keyboard comamnds that we
will use to make a auto_react_robot

j - scroll down posts
l - select react menu
"""

import pyautogui          # for keyboard operation
from time import sleep    # to make delay

while True:     # a forever loop
    pyautogui.typewrite('j')  # scroll down
    sleep(2)                  # wait for 2 seconds to load the post
    pyautogui.typewrite('l')  # open reaction menu
    sleep(.100)               # wait for 100 ms to open the menu
    pyautogui.press('tab')    # go to love react (use tabs to navigate among reactions)
    sleep(.100)               # wait for 100 ms
    pyautogui.press('enter')  # press enter to react 'love'
    sleep(.100)               # a little more delay