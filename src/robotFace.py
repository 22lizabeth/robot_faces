#!/usr/bin/python
import cv2 as cv
import numpy as np
from draw import*
from animate import*
from blink import*

import face_display
import os
import cv2
import cv_bridge
import rospy
import sys
import os
import numpy as np
import threading
from sensor_msgs.msg import Image
import face_display
import signal

#Keys
#Normal = 'n'
#Surprised = 's'
#Sad = 'd'
#Happy = 'h'
#Angry = 'a'


def keyboardInterruptHandler(signal, frame):
    print("\nKeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    exit(0)


def getKey():
    key = cv.waitKey()
    return key


class robotFace:
    def __init__(self, image = False, robotOn = True):
        self.image = image
        self.robotOn = robotOn
        self.currentFace = 0
        self.escKey = 27
        self.black = 0, 0, 0
        self.green = 0, 153, 76
        self.white = 255, 255, 255
        self.backgroundColor = white
    
        self.faceDisplay = face_display.RobotDisplay()

    #Fill background with background color pixels
        self.img = np.zeros((600, 1024, 3), np.uint8)
        self.img[:] = backgroundColor
        if self.image:
            cv.imshow('Face', self.img)  # FOR COMPUTER
        if self.robotOn:
            self.faceDisplay.display_image(self.img)  # FOR ROBOT
        k = ord('n')
        self.currentFace = k
        self.img = drawFace(self.img, chr(k))
        if self.robotOn:
            self.faceDisplay.display_image(self.img)  # FOR ROBOT
        scheduler = BackgroundScheduler()
        self.blinkObj = Blink(chr(self.currentFace),self.img,scheduler,self.image,self.robotOn,self.faceDisplay)
        self.blinkObj.addJob()
        self.blinkObj.startSched()    


    def closing_handle(self):
        self.img = np.zeros((20, 20, 3), np.uint8)
        self.img.fill(255)
        if self.robotOn:
            self.faceDisplay.display_image(self.img)  # FOR ROBOT
        self.blinkObj.stopSched()
        cv.destroyAllWindows() 

    def change_face(self, k):
        if k == self.escKey:
            self.closing_handle()
            return False
        else: 
            self.img = animateFace(self.img, chr(self.currentFace), chr(k), faceDisplay, self.image, self.robotOn)
            self.currentFace = k
            if self.image:
                cv.imshow('Face', self.img)  # FOR COMPUTER
            if self.robotOn:
                self.faceDisplay.display_image(self.img)  # FOR ROBOT
            self.blinkObj.updateCurrentFace(chr(self.currentFace),self.img)    
            return True


signal.signal(signal.SIGINT, keyboardInterruptHandler)


def main(args):
    print args[0]
    try:
        print args[1]
    except:
        args.append("True")

    if args[1] == "False":
        robotOn = False
    else:
        robotOn = True

    if (robotOn):
        rospy.init_node('Face_Display')
    face = robotFace(True, robotOn)

    while (face.change_face(cv.waitKey())):
        pass

if __name__ == '__main__':
    main(sys.argv)
