#!/usr/bin/python
import intera_interface
import rospy
import math
import os
import cv2 as cv
import cv_bridge
from intera_interface import CHECK_VERSION
from robot_faces.srv import *
from sensor_msgs.msg import Image
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import robotFace
import synthesizer

class Sawyer_Face:


    def __init__(self, image, robotOn, dictPath):
       
        self._face = robotFace.robotFace(image, robotOn, dictPath)
        self.synthesizer = synthesizer.Synthesizer()
        change_face_service = rospy.Service('face/change_emotion', Face, self.changeEmotion)
        speak_service = rospy.Service('face/say', Face, self.speak)
        speak_no_animation_service = rospy.Service('face/say_demo', Face, self.speak_no_animation)

    def changeEmotion(self, req):
        try:
            emotion = req.character
            if (emotion == 'x'):
                self._face.change_face(27)
                return FaceResponse(True)
            self._face.change_face(ord(emotion))
            return FaceResponse(True)
        except:
            return FaceResponse(False)

    def speak(self, req):
        try:
            # print req
            self._face.speak(req.character)

            return FaceResponse(True)
        except:
            return FaceResponse(False)

    def speak_no_animation(self, req):
        try:
            # print req
            self.synthesizer.say(req.character)

            return FaceResponse(True)
        except:
            return FaceResponse(False)

def main(args):
    image = False
    robotOn = True
    try:
        args[1]
    except:
        args.append("False")

    if args[1] == "True":
        image = True

    try:
        args[2]
    except:
        args.append("True")

    if args[2] == "False":
        robotOn = False

    print args[3]
    print('ready for face commands')
    rospy.init_node('Face_Display')

    face = Sawyer_Face(image, robotOn, args[3])
    # rospy.on_shutdown(head.clean_shutdown)
    if (image):
        while (face.changeEmotion(chr(cv.waitKey()))):
            pass

    rospy.spin()  
    # rospy.on_shutdown(face._face.closing_handle())


if __name__ == '__main__':
    main(sys.argv)
