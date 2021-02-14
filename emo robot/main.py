""" Your virtual Robot pet

 author: ashraf minhaj
 mail  : ashraf_minhaj@yahoo.com 
"""

"""
install - 
$ pip install pygame
"""

# import libraries
import pygame
from time import sleep

# define colors
WHITE     = (255, 255, 255)
IMAGE_POS = (0, 0)

# initialize things
pygame.init()
pygame.mixer.init()   # Starting the mixer 


"""define window parameters"""
window = pygame.display.set_mode((450,450))
pygame.display.set_caption("My pet: EmoBot")  
clock = pygame.time.Clock()                 # frame rate

# window variables
count = 0          # to count frames
run   = 1

while run:
    clock.tick(10)         # update the window/run loop by this speed
    count += 1  # increase value of count variable
    
    #check for events
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            #quit button clicked
            run = 0
            
        # check for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            cx, cy = pygame.mouse.get_pos()          #get mouse click position
            #print(cx, " ", cy)
            
            # check for top right conrner clicks
            if (cx <= 50) and (cy <= 50):
                image = pygame.image.load('eyeup.PNG') # read image
                window.blit(image, IMAGE_POS)          # add image
                pygame.display.update()                # update the display
                pygame.mixer.music.load("look_away.mp3")  # Loading music 
                pygame.mixer.music.play()              # play the music
                sleep(5)
                continue

            # check for poke in the eye
            if (abs(100 - cx) <= 50) and (abs(100 - cy) <= 50):
                image = pygame.image.load('angry.PNG') # read image
                window.blit(image, IMAGE_POS)          # add image
                pygame.display.update()                # update the display
                pygame.mixer.music.load("angry.mp3")   # Loading music 
                pygame.mixer.music.play()              # play the music
                sleep(2)
                continue
                
            # check mouse click on the EmoBot
            if (cx >= 100) and (cy >= 100) and (cx <= 300) and (cy <= 300):
                image = pygame.image.load('laugh.PNG') # read image
                window.blit(image, IMAGE_POS)          # add image
                pygame.display.update()                # update the display
                pygame.mixer.music.load("laugh.mp3")   # Loading music 
                pygame.mixer.music.play()              # play the music
                sleep(2)
                continue

            
    
    # random movement to show the robot is alive
    if count >= 30:
        window.fill(WHITE)                        # add window color 
        image = pygame.image.load('eyeclose.PNG') # read image
        window.blit(image, IMAGE_POS)             # add image
        count = 0
        
    elif count == 25:
        window.fill(WHITE)                        # add window color 
        image = pygame.image.load('shut.PNG')     # read image
        window.blit(image, IMAGE_POS)             # add image

    elif count == 3:
        window.fill(WHITE)                        # add window color 
        image = pygame.image.load('normal.PNG')   # read image
        window.blit(image, IMAGE_POS)             # add image

    pygame.display.update()         # update the display
    #print(count)

pygame.quit()      #close everything  