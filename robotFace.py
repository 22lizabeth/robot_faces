import cv2 as cv 
import numpy as np 
from draw import*
from animate import*

'''import face_display
import os
import cv2
import cv_bridge
import rospy
import sys, os
import numpy as np
import threading
from sensor_msgs.msg import Image
import face_display
import signal'''

#Keys
#Normal = 'n'
#Surprised = 's'
#Sad = 'd'
#Happy = 'h'
#Angry = 'a'

#Colors (BGR)
black = 0,0,0
green = 0,153,76
white = 255,255,255
backgroundColor = white

#faceDisplay = face_display.RobotDisplay()

#Fill background with background color pixels
img = np.zeros((600,1024,3), np.uint8)
img[:] = backgroundColor
cv.imshow('Face',img) #FOR LAPTOP
#faceDisplay.display_image(img) #FOR ROBOT

#Draw the first face the user chooses
currentFace = 0
escKey = 27
k = cv.waitKey()
if k == escKey:
    cv.destroyAllWindows() #How will this work with robot?
else:
    currentFace = k
    img = drawFace(img, chr(k))
    #faceDisplay.display_image(img) #FOR ROBOT

#Continue to whichever faces the user chooses
if currentFace != 0:
    k = cv.waitKey()
    while(True):
        if k == escKey:
            cv.destroyAllWindows() #Again how will this work?
            break
        img = animateFace(img, chr(currentFace), chr(k))
        currentFace = k
        cv.imshow('Face', img) #FOR LAPTOP
        #faceDisplay.display_image(img) #FOR ROBOT
        k = cv.waitKey()




        

    