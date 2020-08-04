""" 
A. Detect a specific color in camera feed.
  1. set color lower and upper value.
      we used array because images are array of pixel values. 
  2. create a mask- higlight only the colored object
  3. mark only certain size (based on area) - cancel noice and 
    let's us mark only what we need

B. Divide the screen into half (draw line)
  1. get camera feed height width
  2. then draw a line in the middle of frame

C. Get object positon
  1. subtract by the value of (screen_width/2) [line 57]

D. Control game
  1. if pos is negative - jump - press space
  2. if positive - do nothing
"""

import numpy as np   # numerical python for scientific operations
import cv2           # open source computer vision library - image processing operations
import pyautogui     # to use mouse, keyboard functionality

# define area range of detected object (to clear noise)
# objects out of the area range will be ignored
min_area = 300
max_area = 1000

# define color values (blue here)
lower_blue = np.array([110, 50, 50]) 
upper_blue = np.array([130, 255, 255])

cap = cv2.VideoCapture(0)                 # video capture camera object

# get width and height of your image frame
width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 
#print(width, " " ,height) 

# get line start, end points. line must be at the middle
line_start = (0, int(height/2))                      # (x = 0, y = height/2)    
line_end = (int(width), int(height/2))               # (x = width, y = height/2)

while True:	 
    _, frame = cap.read()          # captures the live cam feed frame-by-frame  
    frame = cv2.flip(frame, 1)     # mirror (flip image)

    # detect color and find contours
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                                     # converts images from BGR to HSV 
    mask = cv2.inRange(hsv, lower_blue, upper_blue)                                  # this creates a mask of blue coloured object 
    _, cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # contour of object

    # draw a white line at the middle of the frame
    image = cv2.line(frame, line_start, line_end, (255, 255, 255), 1)

    # check contour areas
    for c in cnts:
        area = cv2.contourArea(c)      # measure area of object
        #print(area)
        if (area > min_area) and (area < max_area):                   # if object is within the range
            x, y, w, h = cv2.boundingRect(c)                          # get bounding rect of of contour
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # draw rectangle around the object
            #print(x, " ", y)

            # get vertical object position (in y axis) - for vertical position of object
            object_pos = y - int(height/2)
            #print(object_pos)

            if object_pos < 0:           # if object is taken up - jump
              pyautogui.press('space')   # press space - dino jumps

    cv2.imshow('frame',frame)         # show image
    if cv2.waitKey(10) == ord('q'):   # press q to quit
        break                         # break to exit

cv2.destroyAllWindows()  # close all the windows
cap.release()            # relsease camera 