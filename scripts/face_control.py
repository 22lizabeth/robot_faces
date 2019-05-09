#!/usr/bin/python
import intera_interface
import rospy
import math
import os
import cv2
import cv_bridge
from intera_interface import CHECK_VERSION
from RobotFaces.srv import *
from sensor_msgs.msg import Image
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import robotFace

class Sawyer_Face:


    def __init__(self):
       
        self._face = robotFace.robotFace()

        change_face_service = rospy.Service('face/change_emotion', Face, self.changeEmotion)

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






    

if __name__ == '__main__':
    print('ready for face commands')
    rospy.init_node('Face_Display')

    face = Sawyer_Face()
    # rospy.on_shutdown(head.clean_shutdown)
    rospy.spin()
