#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import MultiArrayDimension
import random
import numpy as np
from math import *
rospy.init_node("publisher")
gripper_pub = rospy.Publisher('/gimbal_controller/command',    Float64MultiArray, queue_size=1)
mat = Float64MultiArray()
mat.layout.dim.append(MultiArrayDimension())
mat.layout.dim.append(MultiArrayDimension())
mat.data = [pi/2,pi]
while not rospy.is_shutdown():
    gripper_pub.publish(mat)
