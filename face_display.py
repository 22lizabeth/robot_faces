import os
import cv2
import cv_bridge
import rospy
import sys, os
import numpy as np

from sensor_msgs.msg import Image


class RobotDisplay(object):
    """
    Edit of the InteraInterface HeadDisplay Class to accept a numpy screen rather than
    an image path to allow for animated faces and redrawing
    """

    def __init__(self):
        """
        Constructor
        """
        self._image_pub = rospy.Publisher('/robot/head_display', Image, latch=True, queue_size=10)

    def _setup_image(self, img):
        """
        Takes in a numpy image and returns a ros image message
        """

        # Return msg
        return cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")

    def display_image(self, img, sleep = True):
        """
        Function to display an image, give it the numpy screen and whether it needs to sleep or not
        """

        cv_img = self._setup_image(img)

        r = rospy.Rate(10)
        """
        15hz, minnimum time for message to get to Sawyer for a single image
        if using a ros Rate in another file, sleep is not needed
        """  

        self._image_pub.publish(cv_img)
        if sleep:
            r.sleep()
