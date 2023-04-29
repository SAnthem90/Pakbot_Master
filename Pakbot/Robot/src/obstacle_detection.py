#!/usr/bin/env python
import rospy
import time as t
from std_msgs.msg import Float32,String
om = rospy.Publisher("/move_robot",String,queue_size=10)
rospy.init_node("obstacle_detection")

def stop():
    om.publish("s")

def callback(data):
    dis = data.data
    if dis >= 25:
        om.publish("w")
    if dis <25:
        om.publish("s")

#rospy.on_shutdown(callback)
rospy.Subscriber("/distance",Float32,callback)
rospy.on_shutdown(stop)
rospy.spin()
