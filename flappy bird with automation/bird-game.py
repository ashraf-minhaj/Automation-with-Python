""" Flappy bird game with score counting

  author: ashraf minhaj
  mail  : ashraf_minhaj@yahoo.com
"""

""" install -
$ pip install pygame
"""

# import library
import pygame
from random import randint

# initialize things 
pygame.init()

# create game window according to our background image
window = pygame.display.set_mode((320, 568))

# load images
BACKGROUND = pygame.image.load('bg.png')
bird = pygame.image.load('angry-bird.png')
BIRD = pygame.transform.scale(bird, (50, 50))  # make it 50x50

# color variables 
WHITE = (255, 255, 255)

# object position variables
bird_x = 50         # remains always the same
bird_y = 300        # initial position
bird_y_change = 0   # determines number of y pixel the bird will fall or rise

# obstacles- poles
POLE_WIDTH = 70
top_pole_height = randint(100, 350)
POLE_COLOR = (220, 85, 57)      # brick color
pole_x = 310                    # will start appearing from here
GAP = 160                       # gap for the bird to pass
pole_x_change = -3              # reduce x value of pole at this rate

# store score in this variable
score = 0
FONT = pygame.font.Font('freesansbold.ttf', 30)

# game running flag and variables
clock = pygame.time.Clock()       # game clock
FPS = 60                          # frame rate of game
run = 1
while run:
    # tick clock in this rate
    clock.tick(FPS)
    # fill window with white color
    #window.fill(WHITE)

    # add background image
    window.blit(BACKGROUND, (0,0))

    # check for keyboard ations
    for event in pygame.event.get():
        # if user wants to exit
        if event.type == pygame.QUIT:
            run = 0

        # check if space key is pressed
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            bird_y_change = -6

        if (event.type == pygame.KEYUP) and (event.key == pygame.K_SPACE):
            bird_y_change = 3

    # restrict from dropping below the floor
    if bird_y > 460:
        bird_y = 460  # stay on floor

    # restrict bird from going space
    if bird_y < 0:
        bird_y = 0    # stay on top

    # move pole
    pole_x -= 3
    # if reaches left wall, make another obstacle and count score
    if pole_x <= -10:
        pole_x = 310
        top_pole_height = randint(100, 350)

        # update score
        score += 1
        #print(score)

    # add poles/obstacles
    pygame.draw.rect(window, POLE_COLOR, (pole_x, 0, POLE_WIDTH, top_pole_height))
    bottom_pole_height = 510 - top_pole_height - GAP
    pygame.draw.rect(window, POLE_COLOR, (pole_x, 510, POLE_WIDTH, -bottom_pole_height))
    
    # show bird
    bird_y += bird_y_change
    window.blit(BIRD, (bird_x, bird_y))

    # collision detection 
    if (pole_x >= bird_x) and (pole_x <= (bird_x + POLE_WIDTH)):
        print("[ In line with obstacles ]")
        if (bird_y <= top_pole_height):
            print("Hit top pole")
            run = 0
        
        if (bird_y >= (top_pole_height + GAP - 50)):  # mind the gap and bird's height 50
            print("Hit bottom pole")
            run = 0

        print(bird_y, top_pole_height, bird_y, top_pole_height+GAP-50)

    # display score
    score_point = FONT.render(f'Score: {score}', True, WHITE)
    window.blit(score_point, (5, 5))

    # update window
    pygame.display.update()

# close the game app
pygame.quit()