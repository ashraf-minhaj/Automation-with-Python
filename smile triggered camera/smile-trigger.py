""" Wait until smiled again

 author: ashraf minhaj
 mail  : ashraf_minhaj@yahoo.com
"""

""" install-
$ pip install opencv-contrib-python
"""

import cv2
from datetime import datetime
import winsound 

# add a flag to determine when to capture image
capture = True

# load classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while 1:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # find facess
    face = face_cascade.detectMultiScale(gray, 1.5, 5)

    # iterate through all faces and draw rectangle
    for(x, y, w, h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)

        # get regions
        face_roi = frame[y:y+h, x:x+w]
        face_gray = gray[y:y+h, x:x+w]
        
        # detect smile 
        smiles =  smile_cascade.detectMultiScale(face_gray, 1.3, 25)

        # if captured an image and now no smiles are detected, change flag
        if (len(smiles) == 0) and (capture == False):
            capture = True

        # if capture = True
        if capture:
            for(x, y, w, h) in smiles:
                # draw bounding box around smile region
                cv2.rectangle(face_roi, (x,y), (x+w, y+h), (0, 0, 255), 2)

                # save image
                f_name = str(datetime.now().strftime("%H.%M.%S.%d")) + ".jpg"
                print(f_name)
                cv2.imwrite(f_name, frame)

                # play click sound
                winsound.PlaySound('camera_click.wav', winsound.SND_FILENAME)

                # change flag after capturing once
                capture = False
                break            # to get out of the for loop

    cv2.imshow("Output", frame)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()