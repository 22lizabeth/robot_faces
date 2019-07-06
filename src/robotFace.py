#!/usr/bin/python
import cv2 as cv
import numpy as np
from draw import*
from animate import*
from blink import*
from speech_animation import*

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
# import synthesizer

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
    def __init__(self, image=False, robotOn=True, dictPath="cmudict-modified.txt"):
        self.image = image
        self.robotOn = robotOn
        self.currentFace = 0
        self.escKey = 27
        self.black = 0, 0, 0
        self.green = 0, 153, 76
        self.white = 255, 255, 255
        self.backgroundColor = white


        #Fill background with background color pixels
        self.img = np.zeros((600, 1024, 3), np.uint8)
        self.img[:] = backgroundColor
    
        #Create the objects that will be used
        self.drawObj = Draw(self.img)
        self.faceDisplay = face_display.RobotDisplay()
        self.animateObj = Animate(self.img,self.faceDisplay,self.drawObj,self.image,self.robotOn)

        #Display blank background image
        if self.image:
            cv.imshow('Face', self.img)  #COMPUTER DISPLAY
        if self.robotOn:
            self.faceDisplay.display_image(self.img)  #ROBOT DISPLAY
        
        #Set starting face to neutral
        self.currentFace = ord('n')

        #Draw and display first face
        self.img = self.drawObj.drawFace(chr(self.currentFace))

        if self.robotOn:
            self.faceDisplay.display_image(self.img)  #ROBOT DISPLAY
        if self.image:
            cv.imshow('Face',self.img) #COMPUTER DISPLAY

        #Start the blinking
        self.blinkObj = Blink(chr(self.currentFace),self.img,self.image,self.robotOn,self.faceDisplay,self.drawObj)
        self.blinkObj.addJob()
        self.blinkObj.startSched()
        self.speachObj = Speech_Animation(self.img, self.faceDisplay, self.drawObj, self.image, self.robotOn, dictPath)


    def closing_handle(self):
        ###Throw sleeping face in here when done
        self.img = np.zeros((20, 20, 3), np.uint8)
        self.img.fill(255)
        if self.robotOn:
            self.faceDisplay.display_image(self.img)  #ROBOT DISPLAY
        if self.image:
            cv.destroyAllWindows() #CLOSE COMPUTER DISPLAY
        self.blinkObj.stopSched() 

    def speak(self, speech):
        # print ("here")
        self.speachObj.speak(speech)    

    def change_face(self, k):
        if k == self.escKey:
            self.closing_handle()
            return False
        else: 
            self.img = self.animateObj.animateFace(chr(self.currentFace), chr(k))
            self.currentFace = k
            if self.image:
                cv.imshow('Face', self.img)  #COMPUTER DISPLAY
            if self.robotOn:
                self.faceDisplay.display_image(self.img)  #ROBOT DISPLAY
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
