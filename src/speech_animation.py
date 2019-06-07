#!/usr/bin/python
import numpy as np
import cv2 as cv
from draw import*
import time
import face_display

#Colors (BGR)
black = 0, 0, 0
white = 255, 255, 255
green = 0, 153, 76
pink = 203, 192, 255
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


class Speeech_Animation:
    def __init__(self, img, faceDisplayObj, drawObj, computerImage, robotOn):
        self.img = img
        self.faceDisplayObj = faceDisplayObj
        self.drawObj = drawObj
        self.computerImage = computerImage
        self.robotOn = robotOn

        self.animateToDict = {'o': self.animateToOO}
        self.animateFromDict = {'o': self.animateFromOO}

    def speak(self, animateFrom, animateTo):
        print(animateFrom, animateTo)
        if animateFrom == animateTo:
            return self.img
        if animateFrom != 'c':
            self.img = self.animateFromDict[animateFrom]()
        if animateTo != 'c':
            # print("from neutral")
            self.img = self.animateToDict[animateTo]()
        return self.img

    def animateFromOO(self):
        print "from O to C"
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

        maxChange = max([bottomEyeArchMaxChange, eyebrowMaxChange,
                         upperEyeArchMaxChange, eyeSideLineMaxChange, mouthMaxChange])

        #Animate from surprised face to neutral face
        for i in range(maxChange):

            #Mouth animation to neutral mouth
            if i < mouthMaxChange and i > 0:

                #Animate upper mouth until it melds with lower mouth then stop animating upper mouth
                if i < 8:
                    cv.ellipse(self.img, (512, upperMouthY1), (upperMouthX2, upperMouthY2),
                               0, 190, 350, backgroundColor, thickness=4)  # upperMouthArch
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

                        cv.ellipse(self.img, (512, upperMouthY1), (upperMouthX2, upperMouthY2),
                                   0, 190, 350, faceColor, thickness=4)  # upperMouthArch

                #Animate Lower Mouth
                cv.ellipse(self.img, (512, lowerMouthY1), (lowerMouthX2, lowerMouthY2),
                           180, 220, 320, backgroundColor, thickness=4)  # lowerMouthArch
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
                cv.ellipse(self.img, (512, lowerMouthY1), (lowerMouthX2, lowerMouthY2),
                           180, 220, 320, faceColor, thickness=4)  # lowerMouthArch
            # time.sleep(1)
            if self.computerImage:
                cv.imshow('Face', self.img)  # COMPUTER DISPLAY
                cv.waitKey(20)
            if self.robotOn:
                self.faceDisplayObj.display_image(self.img)  # ROBOT DISPLAY
                time.sleep(.035)
        return self.img

    def animateToOO(self):
        print("from c to O")
        #Animation Variables
        bottomEyeArchMaxChange = 4
        eyebrowMaxChange = 6
        upperEyeArchMaxChange = 6
        eyeSideLineMaxChange = 6
        mouthMaxChange = 8
        maxChange = max([bottomEyeArchMaxChange, eyebrowMaxChange,
                         upperEyeArchMaxChange, eyeSideLineMaxChange, mouthMaxChange])

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
                    cv.ellipse(self.img, (512, upperMouthY1), (upperMouthX2, upperMouthY2),
                               0, 190, 350, backgroundColor, thickness=4)  # upperMouthArch
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
                    cv.ellipse(self.img, (512, upperMouthY1), (upperMouthX2, upperMouthY2),
                               0, 190, 350, faceColor, thickness=4)  # upperMouthArch

                #Animate lower mouth
                cv.ellipse(self.img, (512, lowerMouthY1), (lowerMouthX2, lowerMouthY2),
                           180, 220, 320, backgroundColor, thickness=4)  # lowerMouthArch
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
                cv.ellipse(self.img, (512, lowerMouthY1), (lowerMouthX2, lowerMouthY2),
                           180, 220, 320, faceColor, thickness=4)  # lowerMouthArch
            # time.sleep(1)
            if self.computerImage:
                cv.imshow('Face', self.img)  # COMPUTER DISPLAY
                cv.waitKey(20)
            if self.robotOn:
                self.faceDisplayObj.display_image(self.img)  # ROBOT DISPLAY
                time.sleep(.035)

        return self.img
