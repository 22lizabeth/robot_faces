#!/usr/bin/python
import numpy as np 
import cv2 as cv
from draw import*



#Colors (BGR)
black = 0,0,0
white = 255,255,255
green = 0,153,76
pink = 203,192,255
backgroundColor = white
faceColor = black
eyeColor = green

fps = 30

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

class Animate:
    def __init__(self,img,faceDisplayObj,drawObj,computerImage,robotOn):
        self.img = img
        self.faceDisplayObj = faceDisplayObj
        self.drawObj = drawObj
        self.computerImage = computerImage
        self.robotOn = robotOn
        if (robotOn):
            import face_display
        self.animateToDict = {'s': self.animateToSurprised, 'd': self.animateToSad, 'a': self.animateToAngry, 'h': self.animateToHappy}
        self.animateFromDict = {'s': self.animateFromSurprised, 'd': self.animateFromSad, 'a': self.animateFromAngry, 'h': self.animateFromHappy}

    def animateFace(self, animateFrom, animateTo):
        print(animateFrom,animateTo)
        if animateFrom == animateTo:
            return self.img
        if animateFrom != 'n':
            self.img = self.animateFromDict[animateFrom]()
        if animateTo != 'n':
            print("from neutral")
            self.img = self.animateToDict[animateTo]()
        return self.img

    def animateFromSurprised(self):
        #Animation Variables
        bottomEyeArchMaxChange = 3
        eyebrowMaxChange = 6
        upperEyeArchMaxChange = 6
        eyeSideLineMaxChange = 12
        mouthMaxChange = 9

        bottomEyeCenterY1 = 150
        eyebrowY1 = 260
        eyebrowY2 = 190
        archY1 = 300
        archY2 = 180
        eyeLineY2 = 270
        eyeLineY1 = 198
        upperMouthY1 = 520
        upperMouthY2 = 40
        lowerMouthY1 = 488
        lowerMouthY2 = 40
        upperMouthX2 = 40
        lowerMouthX2 = 50

        maxChange = max([bottomEyeArchMaxChange,eyebrowMaxChange,upperEyeArchMaxChange,eyeSideLineMaxChange,mouthMaxChange])

        #Animate from surprised face to neutral face
        for i in range(maxChange):

            #Mouth animation to neutral mouth
            if i < mouthMaxChange and i > 0:

                #Animate upper mouth until it melds with lower mouth then stop animating upper mouth
                if i < 8:
                    cv.ellipse(self.img,(512,upperMouthY1),(upperMouthX2,upperMouthY2),0,190,350,backgroundColor,thickness=4) #upperMouthArch
                    if i < 7:
                        #Decrease row radius of upper mouth to move it close to lower mouth
                        upperMouthY2 = upperMouthY2 - 6
                        #Decrease center y-coordinate of upper mouth to keep it matching with lower mouth as they come together
                        if i == 2:
                            upperMouthY1 = upperMouthY1 - 5
                        else:
                            upperMouthY1 = upperMouthY1 - 3
                        #Increase upper mouth column radius to widen the mouth until it is nearly straight
                        if i == 2 or i == 3:
                            upperMouthX2 = upperMouthX2 + 5
                        else:
                            upperMouthX2 = upperMouthX2 + 2

                        cv.ellipse(self.img,(512,upperMouthY1),(upperMouthX2,upperMouthY2),0,190,350,faceColor,thickness=4) #upperMouthArch

                #Animate Lower Mouth
                cv.ellipse(self.img,(512,lowerMouthY1),(lowerMouthX2,lowerMouthY2),180,220,320,backgroundColor,thickness=4) #lowerMouthArch
                #Decrease row radius of lower mouth to move it closer to upper mouth
                if i < 4:
                    lowerMouthY2 = lowerMouthY2 - 10
                #Increase center y-coordinate of lower mouth for the first set of animation iterations
                if i < 4:
                    lowerMouthY1 = lowerMouthY1 + 3
                #Decrease centery y-coordinate of lower mouth for the last of the animation iterations
                elif i > 4:
                    lowerMouthY1 = lowerMouthY1 - 1
                #Increase lower mouth column radius to widen the mouth until it is nearly straight
                if i > 1:
                    lowerMouthX2 = lowerMouthX2 + 6
                else:
                    lowerMouthX2 = lowerMouthX2 + 3
                cv.ellipse(self.img,(512,lowerMouthY1),(lowerMouthX2,lowerMouthY2),180,220,320,faceColor,thickness=4) #lowerMouthArch

            #Bottom eye arch animation to neutral eyes
            if i >= maxChange - bottomEyeArchMaxChange:
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,180),180,250,290,backgroundColor,thickness=4) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,180),180,250,290,backgroundColor,thickness=4) #rightBottomEyeArch
                bottomEyeCenterY1 = bottomEyeCenterY1 - 3
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,180),180,250,290,faceColor,thickness=4) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,180),180,250,290,faceColor,thickness=4) #rightBottomEyeArch
            
            #Eyebrow animation to neutral eyebrows
            if i >= maxChange - eyebrowMaxChange:
                cv.ellipse(self.img,(280,eyebrowY1),(190,eyebrowY2),0,225,305,backgroundColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,eyebrowY1),(190,eyebrowY2),0,235,315,backgroundColor,thickness=5) #rightEyebrow
                eyebrowY1 = eyebrowY1 - 15
                eyebrowY2 = eyebrowY2 - 20
                cv.ellipse(self.img,(280,eyebrowY1),(190,eyebrowY2),0,225,305,faceColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,eyebrowY1),(190,eyebrowY2),0,235,315,faceColor,thickness=5) #rightEyebrow
            
            #Upper eye animation to neutral eyes
            if i >= maxChange - upperEyeArchMaxChange:
                cv.ellipse(self.img,(744,archY1),(180,archY2),0,235,325,backgroundColor,thickness=4) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(180,archY2),0,215,305,backgroundColor,thickness=4) #leftUpperEyeArch
                archY1 = archY1 - 2
                archY2 = archY2 - 5
                cv.ellipse(self.img,(744,archY1),(180,archY2),0,235,325,faceColor,thickness=4) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(180,archY2),0,215,305,faceColor,thickness=4) #leftUpperEyeArch
            
            #Eye side line animation
            if i >= maxChange - eyeSideLineMaxChange:
                cv.line(self.img,(132,eyeLineY1),(170,eyeLineY2),backgroundColor,thickness=4) #leftEyeSideLine
                cv.line(self.img,(892,eyeLineY1),(854,eyeLineY2),backgroundColor,thickness=4) #rightEyeSideLine
                #move the eyeline vertically up from the base of the line
                eyeLineY2 = eyeLineY2 - 1
                if i > maxChange//2:
                    #move the eyeline vertically down from the top of the line
                    eyeLineY1 = eyeLineY1 + 1
                cv.line(self.img,(132,eyeLineY1),(170,eyeLineY2),faceColor,thickness=4) #leftEyeSideLine
                cv.line(self.img,(892,eyeLineY1),(854,eyeLineY2),faceColor,thickness=4) #rightEyeSideLine
            
            #Show each stage of animation
            if self.computerImage:
                cv.imshow('Face',self.img) #COMPUTER DISPLAY
            if self.robotOn:
                self.faceDisplayObj.display_image(self.img)  #ROBOT DISPLAY
            cv.waitKey(fps)

        return self.drawObj.drawFace('n')

    def animateFromSad(self):
        #Animation Variables
        bottomEyeArchMaxChange = 13
        upperEyeArchMaxChange = 3 
        eyebrowMaxChange = 9
        eyeSideLineMaxChange = 3
        irisMaxChange = 8
        mouthMaxChange = 5

        maxChange = max([bottomEyeArchMaxChange,eyebrowMaxChange,upperEyeArchMaxChange,eyeSideLineMaxChange,
            mouthMaxChange,irisMaxChange])

        startAngleL = 235
        endAngleL = 315
        startAngleR = 225
        endAngleR = 305
        eyebrowCurvedDown = False
        eyebrowAxes = 180
        bottomEyeCenterY1 = 111
        eyebrowY1 = 85
        eyebrowY2 = 51
        archY1 = 282
        archY2 = 135
        eyeLineY1 = 205
        eyeLineY2 = 255
        irisStartAngle = 253
        irisEndAngle = 287
        irisCenterY = 211
        mouthY1 = 560
        mouthY2 = 68
        mouthAxes = 0
        mouthCurvedDown = True

        #Animation from sad to neutral face
        for i in range(maxChange):

            #Mouth animation to neutral mouth
            if i >= maxChange - mouthMaxChange:
                cv.ellipse(self.img,(512,mouthY1),(95,mouthY2),mouthAxes,220,320,backgroundColor,thickness=4)
                if mouthCurvedDown:
                    mouthY1 = mouthY1 - 15
                    mouthY2 = mouthY2 - 17
                else:
                    mouthY1 = mouthY1 - 7
                    mouthY2 = mouthY2 + 10
                if mouthY2 == 0:
                    mouthCurvedDown = False
                    mouthAxes = 180
                cv.ellipse(self.img,(512,mouthY1),(95,mouthY2),mouthAxes,220,320,faceColor,thickness=4)

            #Bottom eye arch animation to neutral eyes
            if i >= maxChange - bottomEyeArchMaxChange:
                #draw background color lines to cover old black lines
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,180),180,250,290,backgroundColor,thickness=4) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,180),180,250,290,backgroundColor,thickness=4) #rightBottomEyeArch
                #redraw the bottom eye arch lower
                if i > 3:
                    bottomEyeCenterY1 = bottomEyeCenterY1 + 2
                else:
                    bottomEyeCenterY1 = bottomEyeCenterY1 + 3
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,180),180,250,290,faceColor,thickness=4) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,180),180,250,290,faceColor,thickness=4) #rightBottomEyeArch

            #Iris change to neutral eyes
            if i <= irisMaxChange:
                #redraw parts of the iris as the bottom eye arch moves down
                cv.ellipse(self.img,(280,irisCenterY),(100,80),180,irisStartAngle,irisEndAngle,eyeColor,thickness=3) #leftIris
                cv.ellipse(self.img,(744,irisCenterY),(100,80),180,irisStartAngle,irisEndAngle,eyeColor,thickness=3) #rightIris
                if i < 4 or i == 5:
                    irisStartAngle = irisStartAngle + 1
                    irisEndAngle = irisEndAngle - 1
                elif i == 4 or i == 6:
                    irisStartAngle = irisStartAngle + 2
                    irisEndAngle = irisEndAngle - 2
                else:
                    irisStartAngle = irisStartAngle + 3
                    irisEndAngle = irisEndAngle - 3
                irisCenterY = irisCenterY + 2
                
            #Eyebrow animation to neutral eyebrows
            if i >= maxChange - eyebrowMaxChange:
                cv.ellipse(self.img,(280,eyebrowY1),(190,eyebrowY2),eyebrowAxes,startAngleL,endAngleL,backgroundColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,eyebrowY1),(190,eyebrowY2),eyebrowAxes,startAngleR,endAngleR,backgroundColor,thickness=5) #rightEyebrow
                if eyebrowCurvedDown:
                    eyebrowY1 = eyebrowY1 + 15
                    eyebrowY2 = eyebrowY2 + 17
                elif eyebrowY2 == 11:
                    eyebrowY2 = 2
                    eyebrowY1 = 110
                    eyebrowCurvedDown = True
                    eyebrowAxes = 0
                    startAngleL = 225
                    endAngleL = 305
                    startAngleR = 235
                    endAngleR = 315
                else:
                    eyebrowY1 = eyebrowY1 + 5
                    eyebrowY2 = eyebrowY2 - 10
                cv.ellipse(self.img,(280,eyebrowY1),(190,eyebrowY2),eyebrowAxes,startAngleL,endAngleL,faceColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,eyebrowY1),(190,eyebrowY2),eyebrowAxes,startAngleR,endAngleR,faceColor,thickness=5) #rightEyebrow
            
            #Upper eye animation to neutral eyes
            if i >= maxChange - upperEyeArchMaxChange:
                cv.ellipse(self.img,(744,archY1),(180,archY2),0,235,325,backgroundColor,thickness=4) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(180,archY2),0,215,305,backgroundColor,thickness=4) #leftUpperEyeArch
                archY1 = archY1 + 2
                archY2 = archY2 + 5
                cv.ellipse(self.img,(744,archY1),(180,archY2),0,235,325,faceColor,thickness=4) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(180,archY2),0,215,305,faceColor,thickness=4) #leftUpperEyeArch
            
            #Eye side line animation
            if i >= maxChange - eyeSideLineMaxChange:
                cv.line(self.img,(132,eyeLineY1),(170,eyeLineY2),backgroundColor,thickness=4) #leftEyeSideLine
                cv.line(self.img,(892,eyeLineY1),(854,eyeLineY2),backgroundColor,thickness=4) #rightEyeSideLine
                #move the eyeline vertically up from the base of the line
                eyeLineY2 = eyeLineY2 + 1
                #move the eyeline vertically down from the top of the line
                eyeLineY1 = eyeLineY1 - 1
                cv.line(self.img,(132,eyeLineY1),(170,eyeLineY2),faceColor,thickness=4) #leftEyeSideLine
                cv.line(self.img,(892,eyeLineY1),(854,eyeLineY2),faceColor,thickness=4) #rightEyeSideLine

            #Show the images
            if self.computerImage:
                cv.imshow('Face',self.img) #COMPUTER DISPLAY
            if self.robotOn:
                self.faceDisplayObj.display_image(self.img)  #ROBOT DISPLAY
            cv.waitKey(fps)

        return self.drawObj.drawFace('n')

    def animateFromAngry(self):
        #Animation Variables
        bottomEyeArchMaxChange = 13
        upperEyeArchMaxChange = 8
        eyebrowMaxChange = 10
        eyeSideLineMaxChange = 9
        mouthMaxChange = 13
        irisMaxChange = 12

        maxChange = max([bottomEyeArchMaxChange,eyebrowMaxChange,upperEyeArchMaxChange,eyeSideLineMaxChange,mouthMaxChange,irisMaxChange])

        mouthCurvedDown = True
        bottomEyeCurvedDown = True
        mouthAxes = 0
        bottomEyeAxes = 0
        rUpperEyeRotation = 352
        lUpperEyeRotation = 8
        lUpperEyeEndAngle = 297
        rUpperEyeEndAngle = 317
        rUpperEyeStartAngle = 243
        lUpperEyeStartAngle = 223
        lEyeLineX1 = 164
        rEyeLineX1 = 860
        lEyeLineX2 = 202
        rEyeLineX2 = 822
        bottomEyeStartAngle = 256
        bottomEyeEndAngle = 284
        rEyebrowRotation = 340
        lEyebrowRotation = 20
        startAngleL = 265
        endAngleL =  325
        startAngleR = 215
        endAngleR = 275
        mouthStartAngle = 229
        mouthEndAngle = 311
        irisStartAngle = 250#253
        irisEndAngle = 290#287
        irisCenterY = 205#211
        lUpperIrisStartAngle = 236
        lUpperIrisEndAngle = 282
        upperIrisCenterY = 266
        lIrisRotation = 15
        rIrisRotation = 345
        rUpperIrisStartAngle = 259
        rUpperIrisEndAngle = 305

        eyebrowY1 = 222
        eyebrowY2 = 20

        bottomEyeCenterY1 = 351
        bottomEyeCenterY2 = 66
        archY1 = 296
        archY2 = 110
        mouthY1 = 545
        mouthY2 = 51

        #Animation from neutral face to angry face
        for i in range(maxChange):

            #Mouth animation to angry mouth
            if i < mouthMaxChange:
                cv.ellipse(self.img,(512,mouthY1),(95,mouthY2),mouthAxes,mouthStartAngle,mouthEndAngle,backgroundColor,thickness=4)
                if i > 8:
                    if mouthCurvedDown:
                        mouthY1 = mouthY1 - 15
                        mouthY2 = mouthY2 - 17
                    else:
                        mouthY1 = mouthY1 - 7
                        mouthY2 = mouthY2 + 10
                    if mouthY2 == 0:
                        mouthCurvedDown = False
                        mouthAxes = 180
                if i < 9:
                    mouthStartAngle = mouthStartAngle - 1
                    mouthEndAngle = mouthEndAngle + 1
                cv.ellipse(self.img,(512,mouthY1),(95,mouthY2),mouthAxes,mouthStartAngle,mouthEndAngle,faceColor,thickness=4)
            
            #Bottom eye arch animation to angry eyes
            if i >= maxChange - bottomEyeArchMaxChange:
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,backgroundColor,thickness=4) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,backgroundColor,thickness=4) #rightBottomEyeArch
            
            #Draw initial line for upper iris
            if i == 2:
                cv.ellipse(self.img,(280,268),(100,80),lIrisRotation,lUpperIrisStartAngle,lUpperIrisEndAngle,eyeColor,thickness=4) #leftIris
                cv.ellipse(self.img,(744,268),(100,80),rIrisRotation,rUpperIrisStartAngle,rUpperIrisEndAngle,eyeColor,thickness=4) #rightIris

            #Iris change to neutral eyes (lower iris)
            if i >= maxChange - irisMaxChange:
                #redraw parts of the iris as the bottom eye arch moves down
                cv.ellipse(self.img,(280,irisCenterY),(100,80),180,irisStartAngle,irisEndAngle,eyeColor,thickness=3) #leftIris
                cv.ellipse(self.img,(744,irisCenterY),(100,80),180,irisStartAngle,irisEndAngle,eyeColor,thickness=3) #rightIris
                if i < 8 or i == 9:
                    irisStartAngle = irisStartAngle + 1
                    irisEndAngle = irisEndAngle - 1
                elif i == 8 or i == 10:
                    irisStartAngle = irisStartAngle + 2
                    irisEndAngle = irisEndAngle - 2
                else:
                    irisStartAngle = irisStartAngle + 3
                    irisEndAngle = irisEndAngle - 3
                irisCenterY = irisCenterY + 2
            
            #Iris change to neutral eyes (upper iris)
            if i < upperEyeArchMaxChange + 1 and i > 1:
                cv.ellipse(self.img,(280,upperIrisCenterY),(100,80),lIrisRotation,lUpperIrisStartAngle,lUpperIrisEndAngle,eyeColor,thickness=3) #leftIris
                cv.ellipse(self.img,(744,upperIrisCenterY),(100,80),rIrisRotation,rUpperIrisStartAngle,rUpperIrisEndAngle,eyeColor,thickness=3) #rightIris
                upperIrisCenterY = upperIrisCenterY - 2
                if lIrisRotation > 0:
                    lIrisRotation = lIrisRotation - 3
                    rIrisRotation = rIrisRotation + 3
                    lUpperIrisStartAngle = lUpperIrisStartAngle + 3
                    lUpperIrisEndAngle = lUpperIrisEndAngle + 2
                    rUpperIrisEndAngle = rUpperIrisEndAngle - 3
                    rUpperIrisStartAngle = rUpperIrisStartAngle - 2
                elif i > 6:
                    lUpperIrisEndAngle = lUpperIrisEndAngle - 3
                    lUpperIrisStartAngle = lUpperIrisStartAngle + 2
                    rUpperIrisEndAngle = lUpperIrisEndAngle
                    rUpperIrisStartAngle = lUpperIrisStartAngle
                else:
                    lUpperIrisEndAngle = lUpperIrisEndAngle - 2
                    lUpperIrisStartAngle = lUpperIrisStartAngle + 1
                    rUpperIrisEndAngle = lUpperIrisEndAngle
                    rUpperIrisStartAngle = lUpperIrisStartAngle
                cv.ellipse(self.img,(280,upperIrisCenterY),(100,80),lIrisRotation,lUpperIrisStartAngle,lUpperIrisEndAngle,eyeColor,thickness=3) #leftIris
                cv.ellipse(self.img,(744,upperIrisCenterY),(100,80),rIrisRotation,rUpperIrisStartAngle,rUpperIrisEndAngle,eyeColor,thickness=3) #rightIris
                upperIrisCenterY = upperIrisCenterY - 3
                if lIrisRotation > 0:
                    lIrisRotation = lIrisRotation - 3
                    rIrisRotation = rIrisRotation + 3
                    lUpperIrisStartAngle = lUpperIrisStartAngle + 3
                    lUpperIrisEndAngle = lUpperIrisEndAngle + 2
                    rUpperIrisEndAngle = rUpperIrisEndAngle - 3
                    rUpperIrisStartAngle = rUpperIrisStartAngle - 1
                elif i > 6:
                    lUpperIrisEndAngle = lUpperIrisEndAngle - 2
                    lUpperIrisStartAngle = lUpperIrisStartAngle + 2
                    rUpperIrisEndAngle = lUpperIrisEndAngle
                    rUpperIrisStartAngle = lUpperIrisStartAngle
                else:
                    lUpperIrisEndAngle = lUpperIrisEndAngle - 2
                    lUpperIrisStartAngle = lUpperIrisStartAngle + 1
                    rUpperIrisEndAngle = lUpperIrisEndAngle
                    rUpperIrisStartAngle = lUpperIrisStartAngle
            
            #Bottom eye arch animation to angry eyes
            if i >= maxChange - bottomEyeArchMaxChange:
                if bottomEyeCenterY2 == 0:
                    bottomEyeCurvedDown = False
                    bottomEyeAxes = 180
                if bottomEyeCurvedDown:
                    bottomEyeCenterY1 = bottomEyeCenterY1 - 20
                    bottomEyeCenterY2 = bottomEyeCenterY2 - 22
                else:
                    bottomEyeCenterY1 = bottomEyeCenterY1 - 15
                    bottomEyeCenterY2 = bottomEyeCenterY2 + 18
                if i < 5:
                    bottomEyeStartAngle = bottomEyeStartAngle - 1
                    bottomEyeEndAngle = bottomEyeEndAngle + 1
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,faceColor,thickness=4) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,faceColor,thickness=4) #rightBottomEyeArch
            
            #Upper eye animation to angry eyes
            if i <= upperEyeArchMaxChange and i > 0:#i >= maxChange - upperEyeArchMaxChange:
                cv.ellipse(self.img,(744,archY1),(180,archY2),rUpperEyeRotation,rUpperEyeStartAngle,rUpperEyeEndAngle,backgroundColor,thickness=5) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(180,archY2),lUpperEyeRotation,lUpperEyeStartAngle,lUpperEyeEndAngle,backgroundColor,thickness=5) #leftUpperEyeArch
                archY1 = archY1 - 1
                archY2 = archY2 + 5
                lUpperEyeRotation = lUpperEyeRotation - 1
                lUpperEyeEndAngle = lUpperEyeEndAngle + 1
                lUpperEyeStartAngle = lUpperEyeStartAngle - 1
                rUpperEyeRotation = rUpperEyeRotation + 1
                rUpperEyeStartAngle = rUpperEyeStartAngle - 1
                rUpperEyeEndAngle = rUpperEyeEndAngle + 1
                cv.ellipse(self.img,(744,archY1),(180,archY2),rUpperEyeRotation,rUpperEyeStartAngle,rUpperEyeEndAngle,faceColor,thickness=4) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(180,archY2),lUpperEyeRotation,lUpperEyeStartAngle,lUpperEyeEndAngle,faceColor,thickness=4) #leftUpperEyeArch
            
            #Eyebrow animation to angry eyebrows
            if i >= maxChange - eyebrowMaxChange:
                cv.ellipse(self.img,(280,nEyebrowY1),(190,eyebrowY2),lEyebrowRotation,startAngleL,endAngleL,backgroundColor,thickness=5) #leftEyebrowStraightPiece
                cv.ellipse(self.img,(744,nEyebrowY1),(190,eyebrowY2),rEyebrowRotation,startAngleR,endAngleR,backgroundColor,thickness=5) #rightEyebrowStraightPiece
                if i < 9:
                    cv.ellipse(self.img,(280,eyebrowY1),(190,nEyebrowY2),lEyebrowRotation,215,startAngleL,backgroundColor,thickness=5) #leftEyebrowCurvedPiece
                    cv.ellipse(self.img,(744,eyebrowY1),(190,nEyebrowY2),rEyebrowRotation,endAngleR,325,backgroundColor,thickness=5) #rightEyebrowCurvedPiece
                eyebrowY2 = eyebrowY2 + 5
                lEyebrowRotation = lEyebrowRotation - 2
                rEyebrowRotation = rEyebrowRotation + 2
                endAngleL = endAngleL - 2
                startAngleR = startAngleR + 2
                if i > 7:
                    startAngleL = startAngleL + 2
                    endAngleR = endAngleR - 2
                if i == 8:
                    startAngleL = startAngleL - 50
                    endAngleR = endAngleR + 50
                    eyebrowY1 = eyebrowY1 - 20
                elif i == 9 or i == 10:
                    eyebrowY1 = eyebrowY1 - 6
                elif i == 11 or i == 12:
                    eyebrowY1 = eyebrowY1 - 6
                elif i == 3 or i == 4 or i == 7:
                    eyebrowY1 = eyebrowY1 - 5
                elif i == 5 or i == 6:
                    eyebrowY1 = eyebrowY1 - 6
                if i < 8:
                    cv.ellipse(self.img,(280,eyebrowY1),(190,nEyebrowY2),lEyebrowRotation,215,startAngleL,faceColor,thickness=5) #leftEyebrow
                    cv.ellipse(self.img,(744,eyebrowY1),(190,nEyebrowY2),rEyebrowRotation,endAngleR,325,faceColor,thickness=5) #rightEyebrow

                cv.ellipse(self.img,(280,nEyebrowY1),(190,eyebrowY2),lEyebrowRotation,startAngleL,endAngleL,faceColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,nEyebrowY1),(190,eyebrowY2),rEyebrowRotation,startAngleR,endAngleR,faceColor,thickness=5) #rightEyebrow
            
            #Eye side line animation
            if i < eyeSideLineMaxChange and i > 0:
                cv.line(self.img,(lEyeLineX1,nEyeLineY1),(lEyeLineX2,nEyeLineY2),backgroundColor,thickness=4) #leftEyeSideLine
                cv.line(self.img,(rEyeLineX1,nEyeLineY1),(rEyeLineX2,nEyeLineY2),backgroundColor,thickness=4) #rightEyeSideLine
                lEyeLineX1 = lEyeLineX1 - 4
                lEyeLineX2 = lEyeLineX2 - 4
                rEyeLineX1 = rEyeLineX1 + 4
                rEyeLineX2 = rEyeLineX2 + 4
                cv.line(self.img,(lEyeLineX1,nEyeLineY1),(lEyeLineX2,nEyeLineY2),faceColor,thickness=4) #leftEyeSideLine
                cv.line(self.img,(rEyeLineX1,nEyeLineY1),(rEyeLineX2,nEyeLineY2),faceColor,thickness=4) #rightEyeSideLine

            #Show the images at each stage of animation
            if self.computerImage:
                cv.imshow('Face',self.img) #COMPUTER DISPLAY
            if self.robotOn:
                self.faceDisplayObj.display_image(self.img)  #ROBOT DISPLAY
            cv.waitKey(fps)

        return self.drawObj.drawFace('n')

    def animateFromHappy(self):
        #Animation Variables
        eyebrowMaxChange = 2
        mouthMaxChange = 8
        maxChange = max([eyebrowMaxChange,mouthMaxChange])

        eyebrowY1 = 220
        eyebrowY2 = 110
        archY1 = 270
        archY2 = 66
        archX2 = 160
        upperMouthY1 = 478
        upperMouthX2 = 169
        lowerMouthY1 = 388
        lowerMouthY2 = 150
        lowerMouthX2 = 167

        #Animation to neutral face from happy face
        for i in range(maxChange):

            if i == 5: 
                #Open eyes suddenly
                #LeftEye
                cv.ellipse(self.img,(280,270),(160,66),0,215,305,backgroundColor,thickness=8) #leftEyeArch
                #RightEye
                cv.ellipse(self.img,(744,270),(160,66),0,235,325,backgroundColor,thickness=8) #rightEyeArch

                self.drawObj.drawInnerEye()
                #LeftEye
                cv.ellipse(self.img,(280,288),(180,150),0,215,305,faceColor,thickness=4) #leftUpperEyeArch
                cv.line(self.img,(132,202),(170,258),faceColor,thickness=4) #leftEyeSideLine
                cv.ellipse(self.img,(280,141),(200,180),180,250,290,faceColor,thickness=4) #leftBottomEyeArch

                #RightEye
                cv.ellipse(self.img,(744,288),(180,150),0,235,325,faceColor,thickness=4) #rightUpperEyeArch
                cv.line(self.img,(892,202),(854,258),faceColor,thickness=4) #rightEyeSideLine
                cv.ellipse(self.img,(744,141),(200,180),180,250,290,faceColor,thickness=4) #rightBottomEyeArch

            #Mouth animation to neutral mouth
            if i < mouthMaxChange:
                #Animate upper mouth before it melds with lower mouth
                #Animate upper mouth
                cv.ellipse(self.img,(512,upperMouthY1),(upperMouthX2,nUpperMouthY2),180,220,320,backgroundColor,thickness=4) #upperMouthArch
                if i < 7:
                    #Decrease column radius to shorten upper lip while increasing center coord to lower upper lip
                    if i > 3:
                        upperMouthX2 = upperMouthX2 - 5
                        upperMouthY1 = upperMouthY1 + 4
                    else:
                        upperMouthX2 = upperMouthX2 - 12
                        upperMouthY1 = upperMouthY1 + 2
                    cv.ellipse(self.img,(512,upperMouthY1),(upperMouthX2,nUpperMouthY2),180,220,320,faceColor,thickness=4) #upperMouthArch

                #Animate lower mouth
                cv.ellipse(self.img,(512,lowerMouthY1),(lowerMouthX2,lowerMouthY2),180,220,320,backgroundColor,thickness=4) #lowerMouthArch
                if i < 7:
                    #Decrease row radius to mover lower mouth closer to upper mouth
                    lowerMouthY2 = lowerMouthY2 - 20
                    #Increase center y-coordinate of lower mouth
                    lowerMouthY1 = lowerMouthY1 + 15
                #Decrease lower mouth column radius to shorten the mouth
                lowerMouthX2 = lowerMouthX2 - 9
                cv.ellipse(self.img,(512,lowerMouthY1),(lowerMouthX2,lowerMouthY2),180,220,320,faceColor,thickness=4) #lowerMouthArch

            #Eyebrow animation to neutral eyebrows
            if i < eyebrowMaxChange:
                cv.ellipse(self.img,(280,eyebrowY1),(190,eyebrowY2),0,225,305,backgroundColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,eyebrowY1),(190,eyebrowY2),0,235,315,backgroundColor,thickness=5) #rightEyebrow
                eyebrowY1 = eyebrowY1 - 25
                eyebrowY2 = eyebrowY2 - 20
                cv.ellipse(self.img,(280,eyebrowY1),(190,eyebrowY2),0,225,305,faceColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,eyebrowY1),(190,eyebrowY2),0,235,315,faceColor,thickness=5) #rightEyebrow   

            #Show the images at each stage of animation
            if self.computerImage:
                cv.imshow('Face',self.img) #COMPUTER DISPLAY
            if self.robotOn:
                self.faceDisplayObj.display_image(self.img)  #ROBOT DISPLAY
            cv.waitKey(fps)

        return self.drawObj.drawFace('n')

    def animateToSurprised(self):
        print("to surprised")
        #Animation Variables
        bottomEyeArchMaxChange = 4
        eyebrowMaxChange = 6
        upperEyeArchMaxChange = 6
        eyeSideLineMaxChange = 6
        mouthMaxChange = 8
        maxChange = max([bottomEyeArchMaxChange,eyebrowMaxChange,upperEyeArchMaxChange,eyeSideLineMaxChange,mouthMaxChange])

        bottomEyeCenterY1 = nBottomEyeCenterY1
        eyebrowY1 = nEyebrowY1
        eyebrowY2 = nEyebrowY2
        archY1 = nArchY1
        archY2 = nArchY2
        eyeLineY1 = nEyeLineY1
        eyeLineY2 = nEyeLineY2
        upperMouthY1 = nUpperMouthY1
        upperMouthY2 = nUpperMouthY2
        upperMouthX2 = nUpperMouthX2
        lowerMouthY1 = nLowerMouthY1
        lowerMouthY2 = nLowerMouthY2
        lowerMouthX2 = nLowerMouthX2

        #Animation to surprised face from neutral face
        for i in range(maxChange):

            #Mouth animation to neutral mouth
            if i >= maxChange - mouthMaxChange:
                #Animate upper mouth after it unmelds with lower mouth
                if i > 2:
                    cv.ellipse(self.img,(512,upperMouthY1),(upperMouthX2,upperMouthY2),0,190,350,backgroundColor,thickness=4) #upperMouthArch 
                if i > 1:
                    #Increase row radius to mover upper mouth further from lower mouth
                    upperMouthY2 = upperMouthY2 + 6
                    #Increase center y-coordinate of upper mouth to keep it matching with lower mouth as they pull apart
                    if i == 6:
                        upperMouthY1 = upperMouthY1 + 5
                    else:
                        upperMouthY1 = upperMouthY1 + 3
                    #Decrease upper mouth column radius to shrink the mouth
                    if i == 6 or i == 5:
                        upperMouthX2 = upperMouthX2 - 5
                    else:
                        upperMouthX2 = upperMouthX2 - 2
                    cv.ellipse(self.img,(512,upperMouthY1),(upperMouthX2,upperMouthY2),0,190,350,faceColor,thickness=4) #upperMouthArch

                #Animate lower mouth
                cv.ellipse(self.img,(512,lowerMouthY1),(lowerMouthX2,lowerMouthY2),180,220,320,backgroundColor,thickness=4) #lowerMouthArch
                #Increase row radius to mover lower mouth further from upper mouth
                if i > 4:
                    lowerMouthY2 = lowerMouthY2 + 10
                #Decrease center y-coordinate of lower mouth for the last set of animation iterations
                if i > 4:
                    lowerMouthY1 = lowerMouthY1 - 3
                #Increase centery y-coordinate of lower mouth for the first set of the animation
                elif i < 4:
                    lowerMouthY1 = lowerMouthY1 + 1
                #Decrease lower mouth column radius to shrink the mouth
                if i == 7:
                    lowerMouthX2 = lowerMouthX2 - 3
                else:
                    lowerMouthX2 = lowerMouthX2 - 6
                cv.ellipse(self.img,(512,lowerMouthY1),(lowerMouthX2,lowerMouthY2),180,220,320,faceColor,thickness=4) #lowerMouthArch

            #Bottom eye arch animation to surprised eyes
            if i <= bottomEyeArchMaxChange:
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,180),180,250,290,backgroundColor,thickness=4) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,180),180,250,290,backgroundColor,thickness=4) #rightBottomEyeArch
                if i == 3:
                    bottomEyeCenterY1 = bottomEyeCenterY1 + 1
                else:
                    bottomEyeCenterY1 = bottomEyeCenterY1 + 2
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,180),180,250,290,faceColor,thickness=4) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,180),180,250,290,faceColor,thickness=4) #rightBottomEyeArch
            
            #Eyebrow animation to surprised eyebrows
            if i >= maxChange - eyebrowMaxChange:
                cv.ellipse(self.img,(280,eyebrowY1),(190,eyebrowY2),0,225,305,backgroundColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,eyebrowY1),(190,eyebrowY2),0,235,315,backgroundColor,thickness=5) #rightEyebrow
                eyebrowY1 = eyebrowY1 + 15
                eyebrowY2 = eyebrowY2 + 20
                cv.ellipse(self.img,(280,eyebrowY1),(190,eyebrowY2),0,225,305,faceColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,eyebrowY1),(190,eyebrowY2),0,235,315,faceColor,thickness=5) #rightEyebrow
            
            #Upper eye animation to surprised eyes
            if i >= maxChange - upperEyeArchMaxChange:
                cv.ellipse(self.img,(744,archY1),(180,archY2),0,235,325,backgroundColor,thickness=4) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(180,archY2),0,215,305,backgroundColor,thickness=4) #leftUpperEyeArch
                archY1 = archY1 + 2
                archY2 = archY2 + 5
                cv.ellipse(self.img,(744,archY1),(180,archY2),0,235,325,faceColor,thickness=4) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(180,archY2),0,215,305,faceColor,thickness=4) #leftUpperEyeArch
            
            #Eye side line animation
            if i >= maxChange - eyeSideLineMaxChange:
                cv.line(self.img,(132,eyeLineY1),(170,eyeLineY2),backgroundColor,thickness=4) #leftEyeSideLine
                cv.line(self.img,(892,eyeLineY1),(854,eyeLineY2),backgroundColor,thickness=4) #rightEyeSideLine
                #move the eyeline vertically up from the base of the line
                eyeLineY2 = eyeLineY2 + 2
                if i > maxChange//2:
                    #move the eyeline vertically down from the top of the line
                    eyeLineY1 = eyeLineY1 - 2
                cv.line(self.img,(132,eyeLineY1),(170,eyeLineY2),faceColor,thickness=4) #leftEyeSideLine
                cv.line(self.img,(892,eyeLineY1),(854,eyeLineY2),faceColor,thickness=4) #rightEyeSideLine
            
            #Show each stage of animation
            if self.computerImage:
                cv.imshow('Face',self.img) #COMPUTER DISPLAY
            if self.robotOn:
                self.faceDisplayObj.display_image(self.img)  #ROBOT DISPLAY
            cv.waitKey(fps)
     
        #Draw one final line over eye side lines
        cv.line(self.img,(132,eyeLineY1),(170,eyeLineY2),backgroundColor,thickness=4) #leftEyeSideLine
        cv.line(self.img,(892,eyeLineY1),(854,eyeLineY2),backgroundColor,thickness=4) #rightEyeSideLine

        return self.drawObj.drawFace('s')

    def animateToSad(self):
        #Animation Variables
        bottomEyeArchMaxChange = 10
        upperEyeArchMaxChange = 3
        eyebrowMaxChange = 9
        eyeSideLineMaxChange = 3
        mouthMaxChange = 5

        maxChange = max([bottomEyeArchMaxChange,eyebrowMaxChange,upperEyeArchMaxChange,eyeSideLineMaxChange,mouthMaxChange])

        startAngleL = 225
        endAngleL = 305
        startAngleR = 235
        endAngleR = 315
        eyebrowCurvedDown = True
        mouthCurvedDown = False
        eyebrowAxes = 0
        mouthAxes = 180

        bottomEyeCenterY1 = nBottomEyeCenterY1
        eyebrowY1 = nEyebrowY1
        eyebrowY2 = nEyebrowY2
        archY1 = nArchY1
        archY2 = nArchY2
        eyeLineY1 = nEyeLineY1
        eyeLineY2 = nEyeLineY2
        mouthY1 = nMouthY1
        mouthY2 = nMouthY2

        #Animation from neutral face to sad face
        for i in range(maxChange):

            #Mouth animation to sad mouth
            if i < mouthMaxChange:
                cv.ellipse(self.img,(512,mouthY1),(95,mouthY2),mouthAxes,220,320,backgroundColor,thickness=4)
                if mouthCurvedDown:
                    mouthY1 = mouthY1 + 15
                    mouthY2 = mouthY2 + 17
                elif mouthY2 == 10:
                    mouthY2 = 0
                    mouthY1 = 500
                    mouthCurvedDown = True
                    mouthAxes = 0
                else:
                    mouthY1 = mouthY1 + 5
                    mouthY2 = mouthY2 - 10
                cv.ellipse(self.img,(512,mouthY1),(95,mouthY2),mouthAxes,220,320,faceColor,thickness=4)
            
            #Bottom eye arch animation to sad eyes
            if i >= maxChange - bottomEyeArchMaxChange:
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,180),180,250,290,backgroundColor,thickness=4) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,180),180,250,290,backgroundColor,thickness=4) #rightBottomEyeArch
                bottomEyeCenterY1 = bottomEyeCenterY1 - 3
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,180),180,250,290,faceColor,thickness=4) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,180),180,250,290,faceColor,thickness=4) #rightBottomEyeArch
            
            #Eyebrow animation to sad eyebrows
            if i >= maxChange - eyebrowMaxChange:
                cv.ellipse(self.img,(280,eyebrowY1),(190,eyebrowY2),eyebrowAxes,startAngleL,endAngleL,backgroundColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,eyebrowY1),(190,eyebrowY2),eyebrowAxes,startAngleR,endAngleR,backgroundColor,thickness=5) #rightEyebrow
                if eyebrowY2 == 2:
                    eyebrowY2 = 1
                    eyebrowCurvedDown = False
                    eyebrowAxes = 180
                    startAngleL = 235
                    endAngleL = 315
                    startAngleR = 225
                    endAngleR = 305
                if eyebrowCurvedDown:
                    eyebrowY1 = eyebrowY1 - 15
                    eyebrowY2 = eyebrowY2 - 17
                else:
                    eyebrowY1 = eyebrowY1 - 5
                    eyebrowY2 = eyebrowY2 + 10
                cv.ellipse(self.img,(280,eyebrowY1),(190,eyebrowY2),eyebrowAxes,startAngleL,endAngleL,faceColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,eyebrowY1),(190,eyebrowY2),eyebrowAxes,startAngleR,endAngleR,faceColor,thickness=5) #rightEyebrow
            
            #Upper eye animation to sad eyes
            if i >= maxChange - upperEyeArchMaxChange:
                cv.ellipse(self.img,(744,archY1),(180,archY2),0,235,325,backgroundColor,thickness=4) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(180,archY2),0,215,305,backgroundColor,thickness=4) #leftUpperEyeArch
                archY1 = archY1 - 2
                archY2 = archY2 - 5
                cv.ellipse(self.img,(744,archY1),(180,archY2),0,235,325,faceColor,thickness=4) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(180,archY2),0,215,305,faceColor,thickness=4) #leftUpperEyeArch
            
            #Eye side line animation
            if i >= maxChange - eyeSideLineMaxChange:
                cv.line(self.img,(132,eyeLineY1),(170,eyeLineY2),backgroundColor,thickness=4) #leftEyeSideLine
                cv.line(self.img,(892,eyeLineY1),(854,eyeLineY2),backgroundColor,thickness=4) #rightEyeSideLine
                #move the eyeline vertically up from the base of the line
                eyeLineY2 = eyeLineY2 - 1
                #move the eyeline vertically down from the top of the line
                eyeLineY1 = eyeLineY1 + 1
                cv.line(self.img,(132,eyeLineY1),(170,eyeLineY2),faceColor,thickness=4) #leftEyeSideLine
                cv.line(self.img,(892,eyeLineY1),(854,eyeLineY2),faceColor,thickness=4) #rightEyeSideLine

            #Show the images
            if self.computerImage:
                cv.imshow('Face',self.img) #COMPUTER DISPLAY
            if self.robotOn:
                self.faceDisplayObj.display_image(self.img)  #ROBOT DISPLAY
            cv.waitKey(fps)

        return self.drawObj.drawFace('d')
        
    def animateToAngry(self):
        #Animation Variables
        bottomEyeArchMaxChange = 13
        upperEyeArchMaxChange = 8
        eyebrowMaxChange = 10
        eyeSideLineMaxChange = 8
        mouthMaxChange = 13

        maxChange = max([bottomEyeArchMaxChange,eyebrowMaxChange,upperEyeArchMaxChange,eyeSideLineMaxChange,mouthMaxChange])

        startAngleL = 225
        endAngleL = 305
        startAngleR = 235
        endAngleR = 315
        eyebrowCurvedDown = True
        mouthCurvedDown = False
        bottomEyeCurvedDown = False
        mouthAxes = 180
        bottomEyeAxes = 180
        rUpperEyeRotation = 360
        lUpperEyeRotation = 0
        lUpperEyeEndAngle = 305
        rUpperEyeEndAngle = 325
        rUpperEyeStartAngle = 235
        lUpperEyeStartAngle = 215
        lEyeLineX1 = 132
        rEyeLineX1 = 892
        lEyeLineX2 = 170
        rEyeLineX2 = 854
        bottomEyeStartAngle = 250
        bottomEyeEndAngle = 290
        rEyebrowRotation = 360
        lEyebrowRotation = 0
        mouthStartAngle = 220
        mouthEndAngle = 320

        bottomEyeCenterY1 = nBottomEyeCenterY1
        bottomEyeCenterY2 = nBottomEyeCenterY2
        eyebrowY1 = nEyebrowY1
        eyebrowY2 = nEyebrowY2
        archY1 = nArchY1
        archY2 = nArchY2
        mouthY1 = nMouthY1
        mouthY2 = nMouthY2

        #Animation from neutral face to angry face
        for i in range(maxChange):

            #Mouth animation to angry mouth
            if i < mouthMaxChange:
                cv.ellipse(self.img,(512,mouthY1),(95,mouthY2),mouthAxes,mouthStartAngle,mouthEndAngle,backgroundColor,thickness=4)
                if i < 4:
                    if mouthCurvedDown:
                        mouthY1 = mouthY1 + 15
                        mouthY2 = mouthY2 + 17
                    elif mouthY2 == 10:
                        mouthY2 = 0
                        mouthY1 = 500
                        mouthCurvedDown = True
                        mouthAxes = 0
                    else:
                        mouthY1 = mouthY1 + 5
                        mouthY2 = mouthY2 - 10
                if i > 3:
                    mouthStartAngle = mouthStartAngle + 1
                    mouthEndAngle = mouthEndAngle - 1
                cv.ellipse(self.img,(512,mouthY1),(95,mouthY2),mouthAxes,mouthStartAngle,mouthEndAngle,faceColor,thickness=4)
            
            #Bottom eye arch animation to angry eyes
            if i >= maxChange - bottomEyeArchMaxChange:
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,backgroundColor,thickness=5) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,backgroundColor,thickness=5) #rightBottomEyeArch
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
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,faceColor,thickness=4) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,faceColor,thickness=4) #rightBottomEyeArch
            
            #Eyebrow animation to angry eyebrows
            if i >= maxChange - eyebrowMaxChange:
                cv.ellipse(self.img,(280,nEyebrowY1),(190,eyebrowY2),lEyebrowRotation,startAngleL,endAngleL,backgroundColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,nEyebrowY1),(190,eyebrowY2),rEyebrowRotation,startAngleR,endAngleR,backgroundColor,thickness=5) #rightEyebrow
                if i > 7:
                    cv.ellipse(self.img,(280,eyebrowY1),(190,nEyebrowY2),lEyebrowRotation,215,startAngleL,backgroundColor,thickness=5) #leftEyebrow
                    cv.ellipse(self.img,(744,eyebrowY1),(190,nEyebrowY2),rEyebrowRotation,endAngleR,325,backgroundColor,thickness=5) #rightEyebrow
                if eyebrowY2 > 20:
                    eyebrowY2 = eyebrowY2 - 5
                lEyebrowRotation = lEyebrowRotation + 2
                rEyebrowRotation = rEyebrowRotation - 2
                endAngleL = endAngleL + 2
                startAngleR = startAngleR - 2
                if i < 8:
                    startAngleL = startAngleL - 2
                    endAngleR = endAngleR + 2
                elif i == 8:
                    startAngleL = startAngleL + 50
                    endAngleR = endAngleR - 50
                    eyebrowY1 = eyebrowY1 + 30#
                elif i == 9 or i == 10:
                    eyebrowY1 = eyebrowY1 + 6
                elif i == 11 or i == 12:
                    eyebrowY1 = eyebrowY1 + 5
                if i > 7:
                    cv.ellipse(self.img,(280,eyebrowY1),(190,nEyebrowY2),lEyebrowRotation,215,startAngleL,faceColor,thickness=5) #leftEyebrow
                    cv.ellipse(self.img,(744,eyebrowY1),(190,nEyebrowY2),rEyebrowRotation,endAngleR,325,faceColor,thickness=5) #rightEyebrow

                cv.ellipse(self.img,(280,nEyebrowY1),(190,eyebrowY2),lEyebrowRotation,startAngleL,endAngleL,faceColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,nEyebrowY1),(190,eyebrowY2),rEyebrowRotation,startAngleR,endAngleR,faceColor,thickness=5) #rightEyebrow
            
            #Upper eye animation to angry eyes
            if i >= maxChange - upperEyeArchMaxChange:
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
                cv.ellipse(self.img,(744,archY1),(180,archY2),rUpperEyeRotation,rUpperEyeStartAngle,rUpperEyeEndAngle,faceColor,thickness=4) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(180,archY2),lUpperEyeRotation,lUpperEyeStartAngle,lUpperEyeEndAngle,faceColor,thickness=4) #leftUpperEyeArch
            
            #Eye side line animation
            if i >= maxChange - eyeSideLineMaxChange:
                cv.line(self.img,(lEyeLineX1,nEyeLineY1),(lEyeLineX2,nEyeLineY2),backgroundColor,thickness=5) #leftEyeSideLine
                cv.line(self.img,(rEyeLineX1,nEyeLineY1),(rEyeLineX2,nEyeLineY2),backgroundColor,thickness=5) #rightEyeSideLine
                lEyeLineX1 = lEyeLineX1 + 4
                lEyeLineX2 = lEyeLineX2 + 4
                rEyeLineX1 = rEyeLineX1 - 4
                rEyeLineX2 = rEyeLineX2 - 4
                cv.line(self.img,(lEyeLineX1,nEyeLineY1),(lEyeLineX2,nEyeLineY2),faceColor,thickness=4) #leftEyeSideLine
                cv.line(self.img,(rEyeLineX1,nEyeLineY1),(rEyeLineX2,nEyeLineY2),faceColor,thickness=4) #rightEyeSideLine

            #Show the images
            if self.computerImage:
                cv.imshow('Face',self.img) #COMPUTER DISPLAY
            if self.robotOn:
                self.faceDisplayObj.display_image(self.img)  #ROBOT DISPLAY
            cv.waitKey(fps)

        return self.drawObj.drawFace('a')

    def animateToHappy(self):
        #Animation Variables
        bottomEyeArchMaxChange = 12
        eyebrowMaxChange = 2
        upperEyeArchMaxChange = 14
        eyeSideLineMaxChange = 8
        mouthMaxChange = 12
        maxChange = max([bottomEyeArchMaxChange,eyebrowMaxChange,upperEyeArchMaxChange,eyeSideLineMaxChange,mouthMaxChange])

        bottomEyeCurvedDown = False
        bottomEyeAxes = 180
        bottomEyeStartAngle = 250
        bottomEyeEndAngle = 290
        bottomEyeCenterY1 = nBottomEyeCenterY1
        bottomEyeCenterY2 = nBottomEyeCenterY2
        eyebrowY1 = nEyebrowY1
        eyebrowY2 = nEyebrowY2
        archY1 = nArchY1
        archY2 = nArchY2
        archX2 = 180
        upperEyeArchThickness = 4
        eyeLineY1 = nEyeLineY1
        eyeLineY2 = nEyeLineY2
        lEyeLineX1 = 132
        rEyeLineX1 = 892
        lEyeLineX2 = 170
        rEyeLineX2 = 854
        upperMouthY1 = nUpperMouthY1
        upperMouthX2 = 125
        lowerMouthY1 = nLowerMouthY1
        lowerMouthY2 = nLowerMouthY2
        lowerMouthX2 = nLowerMouthX2

        #Animation to happy face from neutral face
        for i in range(maxChange):

            #Mouth animation to happy mouth
            if i < mouthMaxChange:
                #Animate upper mouth after it unmelds with lower mouth
                if i > 4:
                    #Animate upper mouth
                    cv.ellipse(self.img,(512,upperMouthY1),(upperMouthX2,nUpperMouthY2),180,220,320,backgroundColor,thickness=4) #upperMouthArch
                    #Increase column radius to widen upper lip while decreasing center coord to raise upper lip
                    if i < 9:
                        upperMouthX2 = upperMouthX2 + 5
                        upperMouthY1 = upperMouthY1 - 4
                    else:
                        upperMouthX2 = upperMouthX2 + 8
                        upperMouthY1 = upperMouthY1 - 2
                    cv.ellipse(self.img,(512,upperMouthY1),(upperMouthX2,nUpperMouthY2),180,220,320,faceColor,thickness=4) #upperMouthArch

                #Animate lower mouth
                cv.ellipse(self.img,(512,lowerMouthY1),(lowerMouthX2,lowerMouthY2),180,220,320,backgroundColor,thickness=4) #lowerMouthArch
                if i > 4:
                    #Increase row radius to mover lower mouth further from upper mouth
                    lowerMouthY2 = lowerMouthY2 + 20
                    #Decrease center y-coordinate of lower mouth
                    lowerMouthY1 = lowerMouthY1 - 15
                #Increase lower mouth column radius to widen the mouth
                lowerMouthX2 = lowerMouthX2 + 6
                cv.ellipse(self.img,(512,lowerMouthY1),(lowerMouthX2,lowerMouthY2),180,220,320,faceColor,thickness=4) #lowerMouthArch

            #Bottom eye arch animation to happy eyes
            if i < bottomEyeArchMaxChange: #>= maxChange - bottomEyeArchMaxChange:
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,backgroundColor,thickness=10) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,backgroundColor,thickness=10) #rightBottomEyeArch
                if bottomEyeCenterY2 == 0:
                    bottomEyeCurvedDown = True
                    bottomEyeAxes = 0
                if bottomEyeCurvedDown:
                    bottomEyeCenterY1 = bottomEyeCenterY1 + 15
                    bottomEyeCenterY2 = bottomEyeCenterY2 + 22
                else:
                    bottomEyeCenterY1 = bottomEyeCenterY1 + 10
                    bottomEyeCenterY2 = bottomEyeCenterY2 - 18
                if i > 6:
                    bottomEyeStartAngle = bottomEyeStartAngle - 1
                    bottomEyeEndAngle = bottomEyeEndAngle + 1
                cv.ellipse(self.img,(280,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,faceColor,thickness=4) #leftBottomEyeArch
                cv.ellipse(self.img,(744,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,faceColor,thickness=4) #rightBottomEyeArch

            #Eyebrow animation to happy eyebrows
            if i >= maxChange - eyebrowMaxChange:
                cv.ellipse(self.img,(280,eyebrowY1),(190,eyebrowY2),0,225,305,backgroundColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,eyebrowY1),(190,eyebrowY2),0,235,315,backgroundColor,thickness=5) #rightEyebrow
                eyebrowY1 = eyebrowY1 + 25
                eyebrowY2 = eyebrowY2 + 20
                cv.ellipse(self.img,(280,eyebrowY1),(190,eyebrowY2),0,225,305,faceColor,thickness=5) #leftEyebrow
                cv.ellipse(self.img,(744,eyebrowY1),(190,eyebrowY2),0,235,315,faceColor,thickness=5) #rightEyebrow

            #Upper eye animation to happy eyes
            if i >= maxChange - upperEyeArchMaxChange:
                cv.ellipse(self.img,(744,archY1),(archX2,archY2),0,235,325,backgroundColor,thickness=8) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(archX2,archY2),0,215,305,backgroundColor,thickness=8) #leftUpperEyeArch
                if i < bottomEyeArchMaxChange:
                    archY1 = archY1 - 4
                    archY2 = archY2 - 12
                else:
                    archY2 = archY2 + 30
                    archX2 = archX2 - 10
                    archY1 = archY1 + 15
                if i == bottomEyeArchMaxChange - 1:
                    upperEyeArchThickness = 8
                cv.ellipse(self.img,(744,archY1),(archX2,archY2),0,235,325,faceColor,upperEyeArchThickness) #rightUpperEyeArch
                cv.ellipse(self.img,(280,archY1),(archX2,archY2),0,215,305,faceColor,upperEyeArchThickness) #leftUpperEyeArch

            #Eye side line animation
            if i < eyeSideLineMaxChange:
                cv.line(self.img,(lEyeLineX1,eyeLineY1),(lEyeLineX2,eyeLineY2),backgroundColor,thickness=4) #leftEyeSideLine
                cv.line(self.img,(rEyeLineX1,eyeLineY1),(rEyeLineX2,eyeLineY2),backgroundColor,thickness=4) #rightEyeSideLine
                eyeLineY2 = eyeLineY2 - 4
                eyeLineY1 = eyeLineY1 + 1
                lEyeLineX2 = lEyeLineX2 - 4
                rEyeLineX2 = rEyeLineX2 + 4
                if i > 2:
                    lEyeLineX1 = lEyeLineX1 + 2
                    rEyeLineX1 = rEyeLineX1 - 2
                    eyeLineY1 = eyeLineY1 + 2
                if i < 5:
                    eyeLineY1 = eyeLineY1 + 1
                    lEyeLineX2 = lEyeLineX2 + 2
                    rEyeLineX2 = rEyeLineX2 - 2
                if i < 7:
                    cv.line(self.img,(lEyeLineX1,eyeLineY1),(lEyeLineX2,eyeLineY2),faceColor,thickness=4) #leftEyeSideLine
                    cv.line(self.img,(rEyeLineX1,eyeLineY1),(rEyeLineX2,eyeLineY2),faceColor,thickness=4) #rightEyeSideLine

             #Show the images
            if self.computerImage:
                cv.imshow('Face',self.img) #COMPUTER DISPLAY
            if self.robotOn:
                self.faceDisplayObj.display_image(self.img)  #ROBOT DISPLAY
            cv.waitKey(fps)

        return self.drawObj.drawFace('h',False)



