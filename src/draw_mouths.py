#!/usr/bin/python
import numpy as np
import cv2 as cv

#Colors (BGR)
black = 0, 0, 0
green = 0, 153, 76
white = 255, 255, 255
backgroundColor = white
faceColor = black
eyeColor = green

class Mouth:
    def __init__(self, img):
        self.img = img
        self.drawDict = {'default': self.drawDefaultTalking, 'cc': self.drawClosed, 'oo': self.drawOO, 'aa':self.drawAA, 
                        'ff':self.drawFF, 'kk':self.drawRestTalking, 'n': self.drawNeutralFace, 's': self.drawSurpriseFace,
                         'd': self.drawSadFace, 'a': self.drawAngryFace, 'h': self.drawHappyFace, 'rt': self.drawRestTalking}
        self.eraseDict = {'default': self.eraseDefaultTalking, 'cc': self.eraseClosed, 'oo': self.eraseOO, 'aa': self.eraseAA, 
                        'ff': self.eraseFF, 'kk':self.eraseRestTalking,'n': self.eraseNeutralFace, 's': self.eraseSurpriseFace,
                         'd': self.eraseSadFace, 'a': self.eraseAngryFace, 'h': self.eraseHappyFace}   
        self.temp = 560
        self.currentMouth = 'cc'
    def drawMouth(self, mouthType):
        # print ("here")
        # print ("mouth type ", mouthType)
        self.currentMouth = mouthType
        return self.drawDict[mouthType]()

    def eraseMouth(self, mouthType):
        # print ("here")
        self.currentMouth = 'rt'
        return self.eraseDict[mouthType]()

    def drawCurrentMouth(self):
        # print ("here")
        return self.drawDict[self.currentMouth]()

    def drawClosed(self):
       
        cv.ellipse(self.img, (512, 493), (95, 10), 180, 220,
                   320, faceColor, thickness=4)  # neutralmouth
        return self.img

    def eraseClosed(self):
       
        cv.ellipse(self.img, (512, 493), (95, 10), 180, 220,
                   320, backgroundColor, thickness=4)  # neutralmouth
        return self.img

    def drawOO(self):
        #mouth
        # self.temp = self.temp + 1
        # print self.temp
        cv.ellipse(self.img, (512, 520), (30, 40), 0, 190, 350,
                   faceColor, thickness=4)  # upperMouthArch
        cv.ellipse(self.img, (512, 488), (40, 40), 180, 220,
                   320, faceColor, thickness=4)  # lowerMouthArch
        
        return self.img
    
    def drawFF(self):
        #mouth
        # self.temp = self.temp + 1
        # print self.temp
        cv.ellipse(self.img,(512,515),(85,35),0,190,350,faceColor,thickness=4)
        cv.ellipse(self.img, (525, 530), (10, 15), 180, 112,
                   170, faceColor, thickness=4)  # lowerMouthArch
        cv.ellipse(self.img, (485, 530), (10, 15), 180, 112,
                   170, faceColor, thickness=4)  # lowerMouthArch
        cv.ellipse(self.img, (454, 552), (80, 40), 180, 70,
                   115, faceColor, thickness=4)  # lowerMouthArch
        cv.ellipse(self.img, (512, 562), (80, 50), 180, 75,
                   105, faceColor,thickness=4)  # lowerMouthArch
        cv.ellipse(self.img, (570, 552), (80, 40), 180, 65,
                   110, faceColor, thickness=4)  # lowerMouthArch

        return self.img
    def eraseFF(self):
        #mouth
        # self.temp = self.temp + 1
        # print self.temp
        cv.ellipse(self.img,(512,515),(85,35),0,190,350,backgroundColor,thickness=4)
        cv.ellipse(self.img, (525, 530), (10, 15), 180, 112,
                   170, backgroundColor, thickness=4)  # lowerMouthArch
        cv.ellipse(self.img, (485, 530), (10, 15), 180, 112,
                   170, backgroundColor, thickness=4)  # lowerMouthArch
        cv.ellipse(self.img, (454, 552), (80, 40), 180, 70,
                   115, backgroundColor, thickness=4)  # lowerMouthArch
        cv.ellipse(self.img, (512, 562), (80, 50), 180, 75,
                   105, backgroundColor,thickness=4)  # lowerMouthArch
        cv.ellipse(self.img, (570, 552), (80, 40), 180, 65,
                   110, backgroundColor, thickness=4)  # lowerMouthArch

        return self.img

    def drawAA(self):
        #mouth
        # self.temp = self.temp + 1
        # print self.temp
        cv.ellipse(self.img, (512, 520), (30, 60), 0, 180, 360,
                   faceColor, thickness=4)  # upperMouthArch
        cv.ellipse(self.img, (512, 488), (40, 50), 180, 220,
                   320, faceColor, thickness=4)  # lowerMouthArch
        
        return self.img

    def eraseAA(self):
        #mouth
        # self.temp = self.temp + 1
        # print self.temp
        cv.ellipse(self.img, (512, 520), (30, 60), 0, 180, 360,
                   backgroundColor, thickness=4)  # upperMouthArch
        cv.ellipse(self.img, (512, 488), (40, 50), 180, 220,
                   320, backgroundColor, thickness=4)  # lowerMouthArch
        
        return self.img

    def eraseOO(self):
        #mouth
        # self.temp = self.temp + 1
        # print self.temp
        cv.ellipse(self.img, (512, 520), (30, 40), 0, 190, 350,
                   backgroundColor, thickness=4)  # upperMouthArch
        cv.ellipse(self.img, (512, 488), (40, 40), 180, 220,
                   320, backgroundColor, thickness=4)  # lowerMouthArch
        
        return self.img


    def drawDefaultTalking(self):
        cv.ellipse(self.img,(552,505),(40,25),30,230,460,faceColor,thickness=4)
        cv.ellipse(self.img,(472,505),(40,25),150,260,490,faceColor,thickness=4)
        cv.ellipse(self.img,(512,500),(100,25),0,250,290,faceColor,thickness=4)
        cv.ellipse(self.img,(512,560),(50,40),0,240,300,faceColor,thickness=4)
        # cv.ellipse(self.img,(512,500),(100,25),0,0,360,faceColor,thickness=4)
        return self.img

    def eraseDefaultTalking(self):
        cv.ellipse(self.img,(552,505),(40,25),30,230,460,backgroundColor,thickness=4)
        cv.ellipse(self.img,(472,505),(40,25),150,260,490,backgroundColor,thickness=4)
        cv.ellipse(self.img,(512,500),(100,25),0,250,290,backgroundColor,thickness=4)
        cv.ellipse(self.img,(512,560),(50,40),0,240,300,backgroundColor,thickness=4)
        # cv.ellipse(self.img,(512,500),(100,25),0,0,360,backgroundColor,thickness=4)
        return self.img


    def drawRestTalking(self):
        cv.ellipse(self.img, (512, 510), (80, 30), 0, 180, 360,
                   faceColor, thickness=4)  # upperMouthArch
        cv.ellipse(self.img, (512, 488), (120, 30), 180, 230,
                   310, faceColor, thickness=4)  # lowerMouthArch
        return self.img

    def eraseRestTalking(self):
        cv.ellipse(self.img, (512, 510), (80, 30), 0, 180, 360,
                   backgroundColor, thickness=4)  # upperMouthArch
        cv.ellipse(self.img, (512, 488), (120, 30), 180, 230,
                   310, backgroundColor, thickness=4)  # lowerMouthArch
        return self.img

    def drawNeutralFace(self):
        #mouth
        cv.ellipse(self.img, (512, 493), (95, 10), 180, 220,
                   320, faceColor, thickness=4)  # neutralmouth
        return self.img

    def drawSurpriseFace(self):
        #mouth
        cv.ellipse(self.img, (512, 520), (40, 40), 0, 190, 350,
                   faceColor, thickness=4)  # upperMouthArch
        cv.ellipse(self.img, (512, 488), (50, 40), 180, 220,
                   320, faceColor, thickness=4)  # lowerMouthArch
        return self.img

    def drawSadFace(self):

        #mouth
        cv.ellipse(self.img, (512, 560), (95, 68), 0, 220,
                   320, faceColor, thickness=4)  # sadmouth

        return self.img

    def drawAngryFace(self):
        #mouth
        cv.ellipse(self.img, (512, 545), (95, 51), 0, 229,
                   311, faceColor, thickness=4)  # angrymouth

        return self.img

    def drawHappyFace(self):
        return self.img

    def eraseNeutralFace(self):
        #mouth
        cv.ellipse(self.img, (512, 493), (95, 10), 180, 220,
                   320, backgroundColor, thickness=4)  # neutralmouth
        return self.img

    def eraseSurpriseFace(self):
        #mouth
        cv.ellipse(self.img, (512, 520), (40, 40), 0, 190, 350,
                   backgroundColor, thickness=4)  # upperMouthArch
        cv.ellipse(self.img, (512, 488), (50, 40), 180, 220,
                   320, backgroundColor, thickness=4)  # lowerMouthArch
        return self.img

    def eraseSadFace(self):

        #mouth
        cv.ellipse(self.img, (512, 560), (95, 68), 0, 220,
                   320, backgroundColor, thickness=4)  # sadmouth

        return self.img

    def eraseAngryFace(self):
        #mouth
        cv.ellipse(self.img, (512, 545), (95, 51), 0, 229,
                   311, backgroundColor, thickness=4)  # angrymouth

        return self.img

    def eraseHappyFace(self):
        return self.img
