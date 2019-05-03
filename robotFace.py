#!/usr/bin/python
import cv2 as cv
import numpy as np
from draw import*
from animate import*

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
    def __init__(self, image = False):
        self.image = image
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
            cv.imshow('Face', self.img)  # FOR LAPTOP
        self.faceDisplay.display_image(self.img)  # FOR ROBOT
        k = ord('n')
        self.currentFace = k
        self.img = drawFace(self.img, chr(k))
        self.faceDisplay.display_image(self.img)


    def closing_handle(self):
        self.img = np.zeros((20, 20, 3), np.uint8)
        self.img.fill(255)
        self.faceDisplay.display_image(self.img, True)  # FOR ROBOT
        cv.destroyAllWindows()  # How will this work with robot?

    def change_face(self, k):
        if k == self.escKey:
            self.closing_handle()
            return False
        else: 
            self.img = animateFace(self.img, chr(self.currentFace), chr(k), faceDisplay, self.image)
            self.currentFace = k
            if self.image:
                cv.imshow('Face', self.img)  # FOR LAPTOP
            faceDisplay.display_image(self.img)  # FOR ROBOT
            return True


signal.signal(signal.SIGINT, keyboardInterruptHandler)


def main(args):
    rospy.init_node('Face_Display')
    face = robotFace(True)

    while (face.change_face(cv.waitKey())):
        pass

if __name__ == '__main__':
    main(sys.argv)
