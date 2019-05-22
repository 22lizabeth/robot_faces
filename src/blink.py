import numpy as np 
import cv2 as cv
from draw import*
import threading
import random
from apscheduler.schedulers.background import BackgroundScheduler
import logging
import time

#Colors (BGR)
black = 0,0,0
green = 0,153,76
white = 255,255,255
backgroundColor = white
faceColor = black
eyeColor = green
blinkFPS = .2

class Blink:
    def __init__(self,currentFace,img,scheduler,computerImage,robotOn,faceDisplay):
        self.currentFace = currentFace
        self.img = img
        self.scheduler = scheduler
        self.computerImage = computerImage
        self.robotOn = robotOn
        self.faceDisplayObj = faceDisplay

        logging.basicConfig()
        self.blinkDict = {'n': self.blinkNeutral,'s': self.blinkSurprised, 'd': self.blinkSad, 'a': self.blinkAngry, 'h': self.blinkHappy}

    def blink(self):
        self.img[:] = backgroundColor
        self.blinkDict[self.currentFace]()

    def addJob(self):
        self.blinkJob = self.scheduler.add_job(self.blink, 'interval', seconds=(random.uniform(3.0,5.0)),max_instances=2)
    
    def startSched(self):
        self.scheduler.start()
    
    def stopSched(self):
        self.scheduler.shutdown()
    
    def updateCurrentFace(self,newFace,newImg):
        self.currentFace = newFace
        self.img = newImg

    def blinkNeutral(self):
        #CloseEyes
        self.img = drawFace(self.img,'n',self.computerImage,False)
        
        #Erase top line of eye
        #LeftEye
        cv.ellipse(self.img,(280,288),(180,150),0,215,305,backgroundColor,thickness=4) #leftUpperEyeArch
        cv.line(self.img,(132,202),(170,258),backgroundColor,thickness=4) #leftEyeSideLine
        #RightEye
        cv.ellipse(self.img,(744,288),(180,150),0,235,325,backgroundColor,thickness=4) #rightUpperEyeArch
        cv.line(self.img,(892,202),(854,258),backgroundColor,thickness=4) #rightEyeSideLine
        #Extend bottom line of eye
        cv.ellipse(self.img,(744,141),(200,180),180,250,290,backgroundColor,thickness=4) #rightBottomEyeArch
        cv.ellipse(self.img,(280,141),(200,180),180,250,290,backgroundColor,thickness=4) #leftBottomEyeArch
        cv.ellipse(self.img,(744,141),(200,180),180,240,300,faceColor,thickness=4) #rightBottomEyeArch
        cv.ellipse(self.img,(280,141),(200,180),180,240,300,faceColor,thickness=4) #leftBottomEyeArch

        #Pause
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.faceDisplayObj.display_image(self.img) 
        time.sleep(blinkFPS)
        #cv.waitKey(5000)

        #OpenEyes
        cv.ellipse(self.img,(744,141),(200,180),180,240,300,backgroundColor,thickness=4) #rightBottomEyeArch
        cv.ellipse(self.img,(280,141),(200,180),180,240,300,backgroundColor,thickness=4) #leftBottomEyeArch
        
        #Show face eyes open again
        self.img = drawFace(self.img,'n',self.computerImage)
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.faceDisplayObj.display_image(self.img)

    def blinkSurprised(self):
        #CloseEyes
        self.img = drawFace(self.img,'s',self.computerImage,False)
        
        #Erase top line of eye
        #LeftEye
        cv.ellipse(self.img,(280,300),(180,180),0,215,305,backgroundColor,thickness=4) #leftUpperEyeArch
        cv.line(self.img,(132,198),(170,270),backgroundColor,thickness=4) #leftEyeSideLine
        #RightEye
        cv.ellipse(self.img,(744,300),(180,180),0,235,325,backgroundColor,thickness=4) #rightUpperEyeArch
        cv.line(self.img,(892,198),(854,270),backgroundColor,thickness=4) #rightEyeSideLine
        #Extend bottom line of eye
        cv.ellipse(self.img,(280,150),(200,180),180,250,290,backgroundColor,thickness=4) #leftBottomEyeArch
        cv.ellipse(self.img,(744,150),(200,180),180,250,290,backgroundColor,thickness=4) #rightBottomEyeArch
        cv.ellipse(self.img,(280,150),(200,180),180,240,300,faceColor,thickness=4) #leftBottomEyeArch
        cv.ellipse(self.img,(744,150),(200,180),180,240,300,faceColor,thickness=4) #rightBottomEyeArch

        #Pause
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.faceDisplayObj.display_image(self.img) 
        time.sleep(blinkFPS)

        #OpenEyes
        cv.ellipse(self.img,(280,150),(200,180),180,240,300,backgroundColor,thickness=4) #leftBottomEyeArch
        cv.ellipse(self.img,(744,150),(200,180),180,240,300,backgroundColor,thickness=4) #rightBottomEyeArch
        self.img = drawFace(self.img,'s',self.computerImage)
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.faceDisplayObj.display_image(self.img)

    def blinkAngry(self):
        #CloseEyes
        self.img = drawFace(self.img,'a',self.computerImage,False)
        
        #Erase top line of eye
        #LeftEye
        cv.ellipse(self.img,(280,296),(180,110),8,225,297,backgroundColor,thickness=4) #leftUpperEyeArch
        cv.line(self.img,(164,202),(202,258),backgroundColor,thickness=4) #leftEyeSideLine
        #RightEye
        cv.ellipse(self.img,(744,296),(180,110),352,243,315,backgroundColor,thickness=4) #rightUpperEyeArch
        cv.line(self.img,(860,202),(822,258),backgroundColor,thickness=4) #rightEyeSideLine
        #Extend bottom line of eye
        cv.ellipse(self.img,(280,351),(200,66),0,256,284,backgroundColor,thickness=4) #leftBottomEyeArch
        cv.ellipse(self.img,(744,351),(200,66),0,256,284,backgroundColor,thickness=4) #rightBottomEyeArch
        cv.ellipse(self.img,(280,351),(200,66),0,246,294,faceColor,thickness=4) #leftBottomEyeArch
        cv.ellipse(self.img,(744,351),(200,66),0,246,294,faceColor,thickness=4) #rightBottomEyeArch

        #Pause
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.faceDisplayObj.display_image(self.img)
        time.sleep(blinkFPS)

        #OpenEyes
        cv.ellipse(self.img,(280,351),(200,66),0,246,294,backgroundColor,thickness=4) #leftBottomEyeArch
        cv.ellipse(self.img,(744,351),(200,66),0,246,294,backgroundColor,thickness=4) #rightBottomEyeArch
        
        self.img = drawFace(self.img,'a',self.computerImage)
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.faceDisplayObj.display_image(self.img)

    def blinkSad(self):
        #CloseEyes
        self.img = drawFace(self.img,'d',self.computerImage,False)
        
        #Erase top line of eye
        #LeftEye
        cv.ellipse(self.img,(280,282),(180,135),0,215,305,backgroundColor,thickness=4) #leftUpperEyeArch
        cv.line(self.img,(132,205),(170,255),backgroundColor,thickness=4) #leftEyeSideLine
        #RightEye
        cv.ellipse(self.img,(744,282),(180,135),0,235,325,backgroundColor,thickness=4) #rightUpperEyeArch
        cv.line(self.img,(892,205),(854,255),backgroundColor,thickness=4) #rightEyeSideLine
        #Extend bottom line of eye
        cv.ellipse(self.img,(280,111),(200,180),180,250,290,backgroundColor,thickness=4) #leftBottomEyeArch
        cv.ellipse(self.img,(744,111),(200,180),180,250,290,backgroundColor,thickness=4) #rightBottomEyeArch
        cv.ellipse(self.img,(280,111),(200,180),180,240,300,faceColor,thickness=4) #leftBottomEyeArch
        cv.ellipse(self.img,(744,111),(200,180),180,240,300,faceColor,thickness=4) #rightBottomEyeArch

        #Pause
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.faceDisplayObj.display_image(self.img)
        time.sleep(blinkFPS)


        #OpenEyes
        cv.ellipse(self.img,(280,111),(200,180),180,240,300,backgroundColor,thickness=4) #leftBottomEyeArch
        cv.ellipse(self.img,(744,111),(200,180),180,240,300,backgroundColor,thickness=4) #rightBottomEyeArch
        
        self.img = drawFace(self.img,'d',self.computerImage)
        if self.computerImage:
            cv.imshow('Face',self.img)
        if self.robotOn:
            self.faceDisplayObj.display_image(self.img)

    def blinkHappy(self):
        return
