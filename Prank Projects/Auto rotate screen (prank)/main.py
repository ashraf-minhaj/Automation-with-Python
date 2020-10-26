""" Rotate screen randomly to get your 
friend wonder what the heck is happening 
to his pc.

author: ashraf minhaj
mail: ashraf_minhaj@yahoo.com
"""
"""
install-
$ pip install rotate-screen
"""

import rotatescreen as rs # just to make the name short
from time import sleep    # to make delays

screen = rs.get_primary_display() # get primary display

screen.set_portrait_flipped()
sleep(1) # 1 sec delay

screen.set_landscape_flipped()
sleep(1) # 1 sec delay

screen.set_portrait()
sleep(1)

screen.set_landscape() # back to normal