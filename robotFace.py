import cv2 as cv 
import numpy as np 
from draw import*
from animate import*

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

#Fill background with background color pixels
img = np.zeros((600,1024,3), np.uint8)
img[:] = backgroundColor
cv.imshow('Face',img)

#Draw the first face the user chooses
currentFace = 0
esc = 27
k = cv.waitKey()
if k == esc:
    cv.destroyAllWindows()
else:
    currentFace = k
    drawFace(img, chr(k))

#Continue to whichever faces the user chooses
if currentFace != 0:
    k = cv.waitKey()
    while(True):
        if k == esc:
            cv.destroyAllWindows()
            break
        img = animateFace(img, chr(currentFace), chr(k))
        currentFace = k
        cv.imshow('Face', img)
        k = cv.waitKey()




        

    