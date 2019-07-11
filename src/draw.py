#!/usr/bin/python
import numpy as np 
import cv2 as cv
from draw_mouths import *

#Colors (BGR)
black = 0,0,0
green = 0,153,76
white = 255,255,255
backgroundColor = white
faceColor = black
eyeColor = green

class Draw:
    def __init__(self, img):
        self.drawMouth = True
        self.mouthObj = Mouth(img)
        # print("here")
        self.currentFace = 'n'
        self.img = img
        self.drawDict = {'n': self.drawNeutralFace, 's': self.drawSurpriseFace, 'd': self.drawSadFace, 'a': self.drawAngryFace, 'h': self.drawHappyFace}

    def drawFace(self,faceType,drawIris = True):
        if not self.drawMouth:
            self.img = self.mouthObj.drawCurrentMouth()

        if drawIris:
            self.img = self.drawInnerEye()
            
        self.img = self.drawNose()

        self.currentFace = faceType

        return self.drawDict[faceType]()

    def getCurrentFace(self):
        # print ("current face", self.currentFace)
        return self.currentFace

    # def updateCurrentFace(self, faceType, newImg):
    #     print ("current face", self.currentFace)
    #     self.currentFace = faceType
    #     self.img = newImg
    #     print ("updated face", self.currentFace)
    #     return self.currentFace

    def updateMouthObj(self, newMouthObj):
        self.mouthObj = newMouthObj

    def toggleDrawMouth(self):
        if self.drawMouth:
            self.drawMouth = False
            # print self.drawMouth
            return
        self.drawMouth = True
        # print self.drawMouth
    
    def drawInnerEye(self):
        cv.ellipse(self.img,(280,230),(45,80),0,0,360,eyeColor,-1) #leftIris
        cv.ellipse(self.img,(280,230),(20,40),0,0,360,faceColor,-1) #leftPupil
        cv.ellipse(self.img,(260,210),(9,13),0,0,360,backgroundColor,-1) #leftEyeHighlight
        cv.ellipse(self.img,(744,230),(45,80),0,0,360,eyeColor,-1) #rightIris
        cv.ellipse(self.img,(744,230),(20,40),0,0,360,faceColor,-1) #rightPupil
        cv.ellipse(self.img,(724,210),(9,13),0,0,360,backgroundColor,-1) #rightEyeHighlight
        return self.img

    def drawNose(self):
        cv.line(self.img,(512,360),(500,380),faceColor,thickness=4) #upperNoseLine
        cv.line(self.img,(500,380),(512,400),faceColor,thickness=4) #lowerNoseLine
        return self.img

    def drawNeutralFace(self):
        #LeftEye
        cv.ellipse(self.img,(280,288),(180,150),0,215,305,faceColor,thickness=4) #leftUpperEyeArch
        cv.line(self.img,(132,202),(170,258),faceColor,thickness=4) #leftEyeSideLine
        cv.ellipse(self.img,(280,141),(200,180),180,250,290,faceColor,thickness=4) #leftBottomEyeArch

        #RightEye
        cv.ellipse(self.img,(744,288),(180,150),0,235,325,faceColor,thickness=4) #rightUpperEyeArch
        cv.line(self.img,(892,202),(854,258),faceColor,thickness=4) #rightEyeSideLine
        cv.ellipse(self.img,(744,141),(200,180),180,250,290,faceColor,thickness=4) #rightBottomEyeArch

        #Eyebrows
        cv.ellipse(self.img,(280,170),(190,70),0,225,305,faceColor,thickness=5) #leftEyebrow
        cv.ellipse(self.img,(744,170),(190,70),0,235,315,faceColor,thickness=5) #rightEyebrow

        #mouth
        if self.drawMouth:
            cv.ellipse(self.img,(512,493),(95,10),180,220,320,faceColor,thickness=4) #neutralmouth
        return self.img

    def drawSurpriseFace(self):                
        #LeftEye
        cv.ellipse(self.img,(280,300),(180,180),0,215,305,faceColor,thickness=4) #leftUpperEyeArch
        cv.line(self.img,(132,198),(170,270),faceColor,thickness=4) #leftEyeSideLine
        cv.ellipse(self.img,(280,150),(200,180),180,250,290,faceColor,thickness=4) #leftBottomEyeArcc

        #RightEye
        cv.ellipse(self.img,(744,300),(180,180),0,235,325,faceColor,thickness=4) #rightUpperEyeArch
        cv.line(self.img,(892,198),(854,270),faceColor,thickness=4) #rightEyeSideLine
        cv.ellipse(self.img,(744,150),(200,180),180,250,290,faceColor,thickness=4) #rightBottomEyeArch

        #Eyebrows
        cv.ellipse(self.img,(280,260),(190,190),0,225,305,faceColor,thickness=5) #leftEyebrow
        cv.ellipse(self.img,(744,260),(190,190),0,235,315,faceColor,thickness=5) #rightEyebrow

        #mouth
        if self.drawMouth:
            cv.ellipse(self.img,(512,520),(40,40),0,190,350,faceColor,thickness=4) #upperMouthArch
            cv.ellipse(self.img,(512,488),(50,40),180,220,320,faceColor,thickness=4) #lowerMouthArch
        return self.img

    def drawSadFace(self): 

        #Erase bottom part of Iris
        bottomEyeCenterY = 141
        for i in range(10):
            cv.ellipse(self.img,(280,bottomEyeCenterY),(200,180),180,250,290,backgroundColor,thickness=4) #leftBottomEyeArch
            cv.ellipse(self.img,(744,bottomEyeCenterY),(200,180),180,250,290,backgroundColor,thickness=4) #rightBottomEyeArch
            bottomEyeCenterY = bottomEyeCenterY - 3
        
        #LeftEye
        cv.ellipse(self.img,(280,282),(180,135),0,215,305,faceColor,thickness=4) #leftUpperEyeArch
        cv.line(self.img,(132,205),(170,255),faceColor,thickness=4) #leftEyeSideLine
        cv.ellipse(self.img,(280,111),(200,180),180,250,290,faceColor,thickness=4) #leftBottomEyeArch

        #RightEye
        cv.ellipse(self.img,(744,282),(180,135),0,235,325,faceColor,thickness=4) #rightUpperEyeArch
        cv.line(self.img,(892,205),(854,255),faceColor,thickness=4) #rightEyeSideLine
        cv.ellipse(self.img,(744,111),(200,180),180,250,290,faceColor,thickness=4) #rightBottomEyeArch

        #Eyebrows
        cv.ellipse(self.img,(280,85),(190,51),180,235,315,faceColor,thickness=5) #leftEyebrow
        cv.ellipse(self.img,(744,85),(190,51),180,225,305,faceColor,thickness=5) #rightEyebrow

        #mouth
        if self.drawMouth:
            cv.ellipse(self.img,(512,560),(95,68),0,220,320,faceColor,thickness=4) #sadmouth

        return self.img

    def drawAngryFace(self):

        #Erase bottom part of iris
        bottomEyeCenterY1 = 141
        bottomEyeCenterY2 = 180
        bottomEyeStartAngle = 250
        bottomEyeEndAngle = 290
        bottomEyeAxes = 180
        bottomEyeCurvedDown = False
        for i in range(13):
            cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,backgroundColor,thickness=4) #leftBottomEyeArch
            cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,backgroundColor,thickness=4) #rightBottomEyeArch
            if bottomEyeCenterY2 == 0:
                bottomEyeCurvedDown = True
                bottomEyeAxes = 0
            if bottomEyeCurvedDown:
                bottomEyeCenterY1 = bottomEyeCenterY1 + 20
                bottomEyeCenterY2 = bottomEyeCenterY2 + 22
            else:
                bottomEyeCenterY1 = bottomEyeCenterY1 + 15
                bottomEyeCenterY2 = bottomEyeCenterY2 - 18
            if i > 6:
                bottomEyeStartAngle = bottomEyeStartAngle + 1
                bottomEyeEndAngle = bottomEyeEndAngle - 1
        
        #Erase top part of Iris
        rUpperEyeRotation = 360
        lUpperEyeRotation = 0
        lUpperEyeEndAngle = 305
        rUpperEyeEndAngle = 325
        rUpperEyeStartAngle = 235
        lUpperEyeStartAngle = 215
        archY1 = 288
        archY2 = 150
        for i in range(8):
            cv.ellipse(self.img,(744,archY1),(180,archY2),rUpperEyeRotation,rUpperEyeStartAngle,rUpperEyeEndAngle,backgroundColor,thickness=5) #rightUpperEyeArch
            cv.ellipse(self.img,(280,archY1),(180,archY2),lUpperEyeRotation,lUpperEyeStartAngle,lUpperEyeEndAngle,backgroundColor,thickness=5) #leftUpperEyeArch
            archY1 = archY1 + 1
            archY2 = archY2 - 5
            lUpperEyeRotation = lUpperEyeRotation + 1
            lUpperEyeEndAngle = lUpperEyeEndAngle - 1
            lUpperEyeStartAngle = lUpperEyeStartAngle + 1
            rUpperEyeRotation = rUpperEyeRotation - 1
            rUpperEyeStartAngle = rUpperEyeStartAngle + 1
            rUpperEyeEndAngle = rUpperEyeEndAngle - 1

        #LeftEye
        cv.ellipse(self.img,(280,296),(180,110),8,225,297,faceColor,thickness=4) #leftUpperEyeArch
        cv.line(self.img,(164,202),(202,258),faceColor,thickness=4) #leftEyeSideLine
        cv.ellipse(self.img,(280,351),(200,66),0,256,284,faceColor,thickness=4) #leftBottomEyeArch

        #RightEye
        cv.ellipse(self.img,(744,296),(180,110),352,243,315,faceColor,thickness=4) #rightUpperEyeArch
        cv.line(self.img,(860,202),(822,258),faceColor,thickness=4) #rightEyeSideLine
        cv.ellipse(self.img,(744,351),(200,66),0,256,284,faceColor,thickness=4) #rightBottomEyeArch

        #Eyebrows
        cv.ellipse(self.img,(280,170),(190,20),20,265,325,faceColor,thickness=5) #leftEyebrowStraightPiece
        cv.ellipse(self.img,(744,170),(190,20),340,215,275,faceColor,thickness=5) #rightEyebrowStraightPiece
        cv.ellipse(self.img,(280,222),(190,70),20,215,265,faceColor,thickness=5) #leftEyebrowCurvedPart
        cv.ellipse(self.img,(744,222),(190,70),340,275,325,faceColor,thickness=5) #rightEyebrowCurvedPart

        #mouth
        if self.drawMouth:
            cv.ellipse(self.img,(512,545),(95,51),0,229,311,faceColor,thickness=4) #angrymouth

        return self.img

    def drawHappyFace(self):
        return self.img

