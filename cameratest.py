#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
bridge = CvBridge()
rospy.init_node("imageSubscriber")
def img(image_message):
	# print("publisher")
	cv_image = bridge.imgmsg_to_cv2(image_message,'bgr8')
	half = cv2.resize(cv_image, (0, 0), fx = 0.35, fy = 0.35) 
	cv2.imshow('image',half)
	cv2.waitKey(0) 
camera_sub = rospy.Subscriber('/camera/rgb/image_raw', Image,img)
rospy.spin()
