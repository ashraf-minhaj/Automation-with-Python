""" ** Python Smart Screen **

*** Video Player Controller ***

*Based on face detection.
It will look for face, if not found for a certain time period,
it will pause the player. If found again - resumes player.
"""
"""
author: Ashraf Minhaj
mail: ashraf_minhaj@yahoo.com
"""

import cv2          #open source computer vision library
import pyautogui    #to perform keyboard operation

# haar cascade classifier to detect faces
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

THRESHOLD = 100             # almost 5 seconds for opencv cycle (20fps)
pause_flag = True           # a flag is used to avoid unnecessary memory consumption by counter
counter = 0                 # counter variable
cap = cv2.VideoCapture(0)   # read from 1st cam (built in cam)

# ==== Read from camera ======
while True:
    _, frame = cap.read()                             # image frame from camera
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                                       # convert image into gray
    faces = face_classifier.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)  # detect face
    face_found = len(faces)                                                              # count faces

    if face_found > 0 and counter == THRESHOLD:
        pyautogui.press('space')  # press the Space key
        counter = 0
        pause_flag = True

    if (face_found > 0):
        for (x, y, w, h) in faces:
            roi_gray = gray[y: y+h, x: x+w]                              #region of interest is face
            cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0, 0), 2)    # draw black rectangle around face

    elif counter == THRESHOLD and (pause_flag == True):
        # pause the player
        pyautogui.press('space')  # press the Space key
        pause_flag = False

    elif (face_found == 0) and (pause_flag == True):
        # this elif statement is put aside so that it doesn't eat the memory by counting
        counter += 1
    
    #print(counter)
    #print(pause_flag)
    #frame = cv2.resize(frame, (200, 150))     # uncomment to make image frame smaller

    cv2.imshow("Controller", frame)
    if cv2.waitKey(10) == ord('q'):
        break

cv2.destroyAllWindows()  #destroy all open windows