#!/usr/bin/env python
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
bridge = CvBridge()
def callback(msg):
	cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
	cv_image = cv2.resize(cv_image, (470, 250))
	cv2.imshow("Image window", cv_image)
	cv2.waitKey(3)


rospy.init_node('image_converter', anonymous=True)
image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,callback)
rospy.spin()