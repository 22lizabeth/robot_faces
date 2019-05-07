#!/usr/bin/python
import numpy as np 
import cv2 as cv

#Colors (BGR)
black = 0,0,0
green = 0,153,76
white = 255,255,255
backgroundColor = white
faceColor = black
eyeColor = green

def drawFace(img, faceType, image = False):
    #Draw face elements that remain unchanged based on facial expession
    drawInnerEye(img)
    drawNose(img)

    if faceType == 'n':
        drawNeutralFace(img, image)
    elif faceType == 's':
        drawSurpriseFace(img, image)
    elif faceType == 'd':
        drawSadFace(img, image)
    elif faceType == 'a':
        drawAngryFace(img, image)
    elif faceType == 'h':
        drawHappyFace(img, image)

    return img

def drawInnerEye(img):
    cv.ellipse(img,(280,230),(45,80),0,0,360,eyeColor,-1) #leftIris
    cv.ellipse(img,(280,230),(20,40),0,0,360,faceColor,-1) #leftPupil
    cv.ellipse(img,(260,210),(9,13),0,0,360,backgroundColor,-1) #leftEyeHighlight
    cv.ellipse(img,(744,230),(45,80),0,0,360,eyeColor,-1) #rightIris
    cv.ellipse(img,(744,230),(20,40),0,0,360,faceColor,-1) #rightPupil
    cv.ellipse(img,(724,210),(9,13),0,0,360,backgroundColor,-1) #rightEyeHighlight
    return img

def drawNose(img):
    cv.line(img,(512,360),(500,380),faceColor,thickness=4) #upperNoseLine
    cv.line(img,(500,380),(512,400),faceColor,thickness=4) #lowerNoseLine
    return img

def drawNeutralFace(img, image):
     #LeftEye
    cv.ellipse(img,(280,288),(180,150),0,215,305,faceColor,thickness=4) #leftUpperEyeArch
    cv.line(img,(132,202),(170,258),faceColor,thickness=4) #leftEyeSideLine
    cv.ellipse(img,(280,141),(200,180),180,250,290,faceColor,thickness=4) #leftBottomEyeArch

    #RightEye
    cv.ellipse(img,(744,288),(180,150),0,235,325,faceColor,thickness=4) #rightUpperEyeArch
    cv.line(img,(892,202),(854,258),faceColor,thickness=4) #rightEyeSideLine
    cv.ellipse(img,(744,141),(200,180),180,250,290,faceColor,thickness=4) #rightBottomEyeArch

    #Eyebrows
    cv.ellipse(img,(280,170),(190,70),0,225,305,faceColor,thickness=5) #leftEyebrow
    cv.ellipse(img,(744,170),(190,70),0,235,315,faceColor,thickness=5) #rightEyebrow

    #mouth
    cv.ellipse(img,(512,493),(95,10),180,220,320,faceColor,thickness=4) #neutralmouth
    if image:
        cv.imshow('Face',img)

    return img


def drawSurpriseFace(img, image):
                    
    #LeftEye
    cv.ellipse(img,(280,300),(180,180),0,215,305,faceColor,thickness=4) #leftUpperEyeArch
    cv.line(img,(132,198),(170,270),faceColor,thickness=4) #leftEyeSideLine
    cv.ellipse(img,(280,150),(200,180),180,250,290,faceColor,thickness=4) #leftBottomEyeArcc

    #RightEye
    cv.ellipse(img,(744,300),(180,180),0,235,325,faceColor,thickness=4) #rightUpperEyeArch
    cv.line(img,(892,198),(854,270),faceColor,thickness=4) #rightEyeSideLine
    cv.ellipse(img,(744,150),(200,180),180,250,290,faceColor,thickness=4) #rightBottomEyeArch

    #Eyebrows
    cv.ellipse(img,(280,260),(190,190),0,225,305,faceColor,thickness=5) #leftEyebrow
    cv.ellipse(img,(744,260),(190,190),0,235,315,faceColor,thickness=5) #rightEyebrow

    #mouth
    cv.ellipse(img,(512,520),(40,40),0,190,350,faceColor,thickness=4) #upperMouthArch
    cv.ellipse(img,(512,488),(50,40),180,220,320,faceColor,thickness=4) #lowerMouthArch
    if image:
        cv.imshow('Face',img)

    return img

def drawSadFace(img, image): 

    #Erase bottom part of Iris
    bottomEyeCenterY = 141
    for i in range(10):
        cv.ellipse(img,(280,bottomEyeCenterY),(200,180),180,250,290,backgroundColor,thickness=4) #leftBottomEyeArch
        cv.ellipse(img,(744,bottomEyeCenterY),(200,180),180,250,290,backgroundColor,thickness=4) #rightBottomEyeArch
        bottomEyeCenterY = bottomEyeCenterY - 3
    
    #LeftEye
    cv.ellipse(img,(280,282),(180,135),0,215,305,faceColor,thickness=4) #leftUpperEyeArch
    cv.line(img,(132,205),(170,255),faceColor,thickness=4) #leftEyeSideLine
    cv.ellipse(img,(280,111),(200,180),180,250,290,faceColor,thickness=4) #leftBottomEyeArch

    #RightEye
    cv.ellipse(img,(744,282),(180,135),0,235,325,faceColor,thickness=4) #rightUpperEyeArch
    cv.line(img,(892,205),(854,255),faceColor,thickness=4) #rightEyeSideLine
    cv.ellipse(img,(744,111),(200,180),180,250,290,faceColor,thickness=4) #rightBottomEyeArch

    #Eyebrows
    cv.ellipse(img,(280,85),(190,51),180,235,315,faceColor,thickness=5) #leftEyebrow
    cv.ellipse(img,(744,85),(190,51),180,225,305,faceColor,thickness=5) #rightEyebrow

    #mouth
    cv.ellipse(img,(512,560),(95,68),0,220,320,faceColor,thickness=4) #sadmouth
    if image:
        cv.imshow('Face',img)

    return img

def drawAngryFace(img, image):

    #Erase bottom part of iris
    bottomEyeCenterY1 = 141
    bottomEyeCenterY2 = 180
    bottomEyeStartAngle = 250
    bottomEyeEndAngle = 290
    bottomEyeAxes = 180
    bottomEyeCurvedDown = False
    for i in range(13):
        cv.ellipse(img,(280,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,backgroundColor,thickness=4) #leftBottomEyeArch
        cv.ellipse(img,(744,bottomEyeCenterY1),(200,bottomEyeCenterY2),bottomEyeAxes,bottomEyeStartAngle,bottomEyeEndAngle,backgroundColor,thickness=4) #rightBottomEyeArch
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
        cv.ellipse(img,(744,archY1),(180,archY2),rUpperEyeRotation,rUpperEyeStartAngle,rUpperEyeEndAngle,backgroundColor,thickness=5) #rightUpperEyeArch
        cv.ellipse(img,(280,archY1),(180,archY2),lUpperEyeRotation,lUpperEyeStartAngle,lUpperEyeEndAngle,backgroundColor,thickness=5) #leftUpperEyeArch
        archY1 = archY1 + 1
        archY2 = archY2 - 5
        lUpperEyeRotation = lUpperEyeRotation + 1
        lUpperEyeEndAngle = lUpperEyeEndAngle - 1
        lUpperEyeStartAngle = lUpperEyeStartAngle + 1
        rUpperEyeRotation = rUpperEyeRotation - 1
        rUpperEyeStartAngle = rUpperEyeStartAngle + 1
        rUpperEyeEndAngle = rUpperEyeEndAngle - 1

    #LeftEye
    cv.ellipse(img,(280,296),(180,110),8,225,297,faceColor,thickness=4) #leftUpperEyeArch
    cv.line(img,(164,202),(202,258),faceColor,thickness=4) #leftEyeSideLine
    cv.ellipse(img,(280,351),(200,66),0,256,284,faceColor,thickness=4) #leftBottomEyeArch

    #RightEye
    cv.ellipse(img,(744,296),(180,110),352,243,315,faceColor,thickness=4) #rightUpperEyeArch
    cv.line(img,(860,202),(822,258),faceColor,thickness=4) #rightEyeSideLine
    cv.ellipse(img,(744,351),(200,66),0,256,284,faceColor,thickness=4) #rightBottomEyeArch

    #Eyebrows
    cv.ellipse(img,(280,170),(190,20),20,265,325,faceColor,thickness=5) #leftEyebrowStraightPiece
    cv.ellipse(img,(744,170),(190,20),340,215,275,faceColor,thickness=5) #rightEyebrowStraightPiece
    cv.ellipse(img,(280,222),(190,70),20,215,265,faceColor,thickness=5) #leftEyebrowCurvedPart
    cv.ellipse(img,(744,222),(190,70),340,275,325,faceColor,thickness=5) #rightEyebrowCurvedPart

    #mouth
    cv.ellipse(img,(512,545),(95,51),0,229,311,faceColor,thickness=4) #angrymouth
    if image:
        cv.imshow('Face',img)

    return img

def drawHappyFace(img, image):
    return img
