import numpy as np
import cv2 as cv
from draw import*
import threading
import random
from apscheduler.schedulers.background import BackgroundScheduler
import logging
import time
import math
from speech_animation import*

#Colors (BGR)
black = 0, 0, 0
green = 0, 153, 76
white = 255, 255, 255
backgroundColor = white
faceColor = black
eyeColor = green
blinkFPS = .2


class Speech:
    def __init__(self, currentFace, img, computerImage, robotOn, faceDisplay, drawObj):
        self.currentFace = currentFace
        self.img = img
        self.computerImage = computerImage
        self.robotOn = robotOn
        self.faceDisplayObj = faceDisplay
        self.drawObj = drawObj
        self.last_char = 'o'
        self.animateObj = Speeech_Animation(self.img,self.faceDisplayObj,self.drawObj,self.computerImage,self.robotOn)
        logging.basicConfig()
        self.speachDict = {'o': self.OO}

    def updateCurrentFace(self, newFace, newImg):
        self.currentFace = newFace
        self.img = newImg

    def say_sound(self, char):
        # pass
        print "2"
        print char
        self.animateObj.speak(self.last_char, char)
        # self.last_char = char

    def OO(self):
        #Draw O shape
        cv.ellipse(self.img, (512, 520), (40, 40), 0, 190,
                    350, faceColor, thickness=4)  # upperMouthArch
        cv.ellipse(self.img, (512, 488), (50, 40), 180, 220,
                    320, faceColor, thickness=4)  # lowerMouthArch
        #Display image with eyes closed for some milliseconds
        if self.computerImage:
            cv.imshow('Face', self.img)  # COMPUTER DISPLAY
            cv.waitKey(100)
        if self.robotOn:
            self.faceDisplayObj.display_image(self.img)  # ROBOT DISPLAY
            time.sleep(.1)

        #Erase O Shape
        cv.ellipse(self.img, (512, 520), (40, 40), 0, 190,
                    350, backgroundColor, thickness=4)  # upperMouthArch
        cv.ellipse(self.img, (512, 488), (50, 40), 180, 220,
                    320, backgroundColor, thickness=4)  # lowerMouthArch


    def speak(self, words_to_say):
        """
        Erase Current Mouth
        """
        """
        speak
        """
        itertations = math.ceil(len(words_to_say) * .25)
        print "1"
        for i in range(int(itertations)):
            letter = 'o'
            cv.rectangle(self.img, (801, 540), (213, 470), backgroundColor, thickness=-1)  # neutralmouth
            # self.say_sound(letter)
            self.say_sound('c')
            # if self.computerImage:
            #     cv.imshow('Face', self.img)  # COMPUTER DISPLAY
            #     cv.waitKey(200)
            # if self.robotOn:
            #     self.faceDisplayObj.display_image(self.img)  # ROBOT DISPLAY
            #     time.sleep(.2)
        """
        Draw Current Mouth
        """
        # self.img = self.drawObj.drawFace(str(self.currentFace), False)
        # if self.computerImage:
        #     cv.imshow('Face', self.img)  # COMPUTER DISPLAY
        # if self.robotOn:
        #     self.faceDisplayObj.display_image(self.img)  # ROBOT DISPLAY

