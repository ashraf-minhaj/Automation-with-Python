""" Halloween Scary App

author: ashraf minhaj
mail: ashraf_minhaj@yahoo.com

install -
$ pip install pygame
"""


import pygame
from time import sleep  # to make delay

#game variables
BLACK = (0, 0, 0)                         #Tuple to store color RGB values (R, G, B)

IMAGE_POS = (0, 0)           #x, y coordinates of image to be displayed

pygame.init()         # initialize pygame window
pygame.mixer.init()   # Starting the mixer 

image = pygame.image.load('scr.jpg')        # read scary image
pygame.mixer.music.load("ratsasan.mp3")     # Loading ratsasab piano music 
pygame.mixer.music.play()                   # play the music


"""define window parameters"""
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)  # make the window full screen
pygame.display.set_caption("Your PC is Haunted!")          # game name on the title bar

""" make the delay """
sleep(20)                  # 20 sec

# Start playing the song 
#pygame.mixer.music.set_volume(100) 
pygame.mixer.music.load("scary.mp3")    # Loading the scream sound
pygame.mixer.music.play() 

"""setup game loop"""
clock = pygame.time.Clock()  # game clock
run = 1

while run:
    clock.tick(60)         # update the window/run loop by this speed

    window.fill(BLACK)              # make black window
    window.blit(image, IMAGE_POS)   # add last image

    pygame.display.update()         # update the display

    #check for events
    for event in pygame.event.get():    #quit button
        if event.type == pygame.QUIT:
            run = 0

pygame.quit()      #close everything