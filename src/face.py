import numpy as np
import os
import cv2 as cv
import draw_face as draw
from speech_animation import*
import subprocess
import signal
import pyttsx3
import threading

black = 0, 0, 0
green = 0, 153, 76
white = 255, 255, 255
backgroundColor = white
img = np.zeros((600, 1024, 3), np.uint8)
img[:] = backgroundColor
face = draw.Draw(img) 
img = face.drawFace('a')
robotOn=False

def keyboardInterruptHandler(signal, frame):
    print("\nKeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    cv.destroyAllWindows()
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)
try:
    import rospy
    rospy.init_node("Face")
    robotOn=True
    import face_display
    robot_display = face_display.RobotDisplay()
except:
    robotOn= False
    print "robot off"

cv.imshow('Face',img)
cv.waitKey(10)
if robotOn:
    robot_display.display_image(img)
display = "None"
speak = Speech_Animation(img, display, face, True, robotOn)
last_key = 'c'
next_key = 'o'
string = raw_input("what would you like me to say?")

while (string != 'x'):
    # subprocess.call("espeak -p70 -ven-rp+m7 -s160\""+ string + "\"", shell=True)
    speak.speak(string)
    string = raw_input("what would you like me to say?")

    # pass
cv.destroyAllWindows()  # CLOSE COMPUTER DISPLAY

