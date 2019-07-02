#!/usr/bin/python
import numpy as np
import cv2 as cv
from draw import*
import time
from draw_mouths import*
import string
import synthesizer
import threading
import syllableizer

#Colors (BGR)
black = 0, 0, 0
white = 255, 255, 255
green = 0, 153, 76
pink = 203, 192, 255
backgroundColor = white
faceColor = black
eyeColor = green

fps = 150

#Neutral Face Paramters
nBottomEyeCenterY1 = 141
nBottomEyeCenterY2 = 180
nEyebrowY1 = 170
nEyebrowY2 = 70
nArchY1 = 288
nArchY2 = 150
nEyeLineY1 = 202
nEyeLineY2 = 258
nUpperMouthY1 = 500
nUpperMouthY2 = 4
nUpperMouthX2 = 58
nLowerMouthY1 = 493
nLowerMouthY2 = 10
nLowerMouthX2 = 95
nMouthY1 = 493
nMouthY2 = 10


class Speech_Animation:
    def __init__(self, img, faceDisplayObj, drawObj, computerImage, robotOn, dictPath):
        self.img = img
        self.faceDisplayObj = faceDisplayObj
        self.drawObj = drawObj
        self.computerImage = computerImage
        self.robotOn = robotOn
        self.mouth = Mouth(img)
        self.drawObj.updateMouthObj(self.mouth)
        self.synthesizer = synthesizer.Synthesizer()
        self.syllableizer = syllableizer.Syllableizer(dictPath)
        '''
        text to speech options
        '''

        try:
            import face_display
            self.robot_display = face_display.RobotDisplay()
        except:
            print "Robot off"


        self.last = self.drawObj.getCurrentFace()

        self.animateToDict = {
            'aa' : self.animateToAA,
            'oo': self.animateToOO,
            'cc': self.animateToC,
            'ff' :self.animateToFF,
            'kk' :self.animateToKK,
            'n': self.animateToNeutralFace,
            's': self.animateToSurpriseFace,
            'd': self.animateToSadFace, 
            'a': self.animateToAngryFace, 
            'h': self.animateToHappyFace,
            'default': self.animateToDefault}
        self.animateFromDict = {
            'aa' : self.animateFromAA,
            'oo': self.animateFromOO,
            'cc': self.animateFromC,
            'ff' : self.animateFromFF,
            'kk' : self.animateFromKK,
            'n': self.animateFromNeutralFace,
            's': self.animateFromSurpriseFace,
            'd': self.animateFromSadFace, 
            'a': self.animateFromAngryFace, 
            'h': self.animateFromHappyFace,
            'default': self.animateFromDefault
            }

        self.soundDict = {
            "AA" : "aa",
            "AE" : "aa",
            "AH" : "aa",
            "AO" : "oo",
            "AW" : "aa",
            "AY" : "aa",
            "B"  : "cc",
            "CH": "kk",
            "D" : "kk",
            "DH": "kk",
            "EH" : "default",
            "ER": "default",
            "EY": "aa",
            "F" : "ff",
            "G": "kk",
            "HH": "kk",
            "IH": "default",
            "IY" : "aa",
            "JH": "default",
            "K": "kk",
            "L": "default",
            "M" : "cc",
            "N": "default",
            "NG": "default",
            "OW" : "oo",
            "OY" : "oo",
            "P" : "cc",
            "R": "oo",
            "S": "kk",
            "SH": "kk",
            "T": "kk",
            "TH": "kk",
            "UH": "default",
            "UW" : "oo",
            "V" : "ff",
            "W": "oo",
            "Y": "default",
            "Z": "kk",
            "ZH": "default",
            "PUNCTUATION" : "cc",
        }
    def secToMs(self, sec):
        print (sec, sec*1000)
        return sec * 1000

    def speak(self, say):
        print say
        self.engine.say(say)
        print "entering syllableizer"
        self.syllableizer.split_words(say)
        # numWords = len(Say.split())
        # print ("numwords", numWords)
        # print len(Say)
        # numLetters = len(Say.replace(" ", ""))
        # print ("numLetters", numLetters)
        # totalSec = (numWords / 140.0) * 60.0
        # print ("totalSec", totalSec)
        # secPerWord = totalSec / numWords
        # print ("secPerWord", secPerWord)
        # fps = totalSec / (2* numLetters)
        # print ("fps", fps)
        thread = threading.Thread(target=self.synthesizer.say(say))

        # self.animateFromC()
        # self.img = self.mouth.drawFF()== "." or a == "," or a == "?" or a == "!"
        # self.img = self.mouth.drawOO()== "." or a == "," or a == "?" or a == "!"
        self.last = self.drawObj.getCurrentFace()
        self.drawObj.toggleDrawMouth()
        syllables_list = self.syllableizer.getList()
        thread.start()
        for word in syllables_list:
            print word
            sounds = word.split()
            for sound in sounds:
                mouth_shape = self.soundDict[sound]
                print mouth_shape
                if mouth_shape != self.last:
                    self.animateFromDict[self.last]()
                    pass
                # cv.waitKey(15)
                time.sleep(0.03)
                if mouth_shape != self.last:
                    self.animateToDict[mouth_shape]()
                    pass
                # cv.waitKey(int((self.secToMs(fps) - 15)))
                time.sleep(.075)
                if (sound == 'PUNCTUATION'):
                    print ("punctiation")
                    # cv.waitKey(int(self.secToMs(fps) * 2))
                    time.sleep(.09)
                self.last = mouth_shape
                # string = raw_input('hello')

        self.mouth.eraseRestTalking()
        self.mouth.eraseMouth(self.last)
        self.img = self.mouth.drawMouth(self.drawObj.getCurrentFace())
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        # cv.waitKey(100)
        self.drawObj.toggleDrawMouth()
        time.sleep(.001)
        self.last = 'c'
        return self.img

    def animateFromDefault(self):
        self.img = self.mouth.eraseMouth('default')
        self.img = self.mouth.drawRestTalking()
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateToDefault(self):
        self.mouth.eraseRestTalking()
        self.img = self.mouth.drawMouth('default')
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img


    def animateFromFF(self):
        self.img = self.mouth.eraseMouth('ff')
        self.img = self.mouth.drawRestTalking()
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateToFF(self):
        self.mouth.eraseRestTalking()
        self.img = self.mouth.drawMouth('ff')
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateFromKK(self):
        self.img = self.mouth.eraseMouth('kk')
        self.img = self.mouth.drawRestTalking()
        if self.computerImage:
            cv.imshow('Face', self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateToKK(self):
        self.mouth.eraseRestTalking()
        self.img = self.mouth.drawMouth('kk')
        if self.computerImage:
            cv.imshow('Face', self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateFromC(self):
        self.img = self.mouth.eraseMouth('cc')
        self.img = self.mouth.drawRestTalking()
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateToC(self):
        self.mouth.eraseRestTalking()
        self.img = self.mouth.drawMouth('cc')
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateFromAA(self):
        self.img = self.mouth.eraseMouth('aa')
        self.img = self.mouth.drawRestTalking()
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateToAA(self):
        self.mouth.eraseRestTalking()
        self.img = self.mouth.drawMouth('aa')
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img


    def animateFromOO(self):

        self.img = self.mouth.eraseMouth('oo')
        self.img = self.mouth.drawRestTalking()
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateToOO(self):

        self.mouth.eraseRestTalking()
        self.img = self.mouth.drawMouth('oo')
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img



    def animateFromNeutralFace(self):
        self.img = self.mouth.eraseMouth('n')
        self.img = self.mouth.drawRestTalking()
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateToNeutralFace(self):
        self.mouth.eraseRestTalking()
        self.img = self.mouth.drawMouth('n')
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateFromSurpriseFace(self):
        self.img = self.mouth.eraseMouth('s')
        self.img = self.mouth.drawRestTalking()
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img
    
    def animateToSurpriseFace(self):
        self.mouth.eraseRestTalking()
        self.img = self.mouth.drawMouth('s')
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img


    def animateFromSadFace(self):
        self.img = self.mouth.eraseMouth('d')
        self.img = self.mouth.drawRestTalking()
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img
    
    def animateToSadFace(self):
        self.mouth.eraseRestTalking()
        self.img = self.mouth.drawMouth('s')
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateFromAngryFace(self):
        self.img = self.mouth.eraseMouth('a')
        self.img = self.mouth.drawRestTalking()
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateToAngryFace(self):
        self.mouth.eraseRestTalking()
        self.img = self.mouth.drawMouth('a')
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.robot_display.display_image(self.img)
        return self.img

    def animateFromHappyFace(self):
        return

    def animateToHappyFace(self):
        return
