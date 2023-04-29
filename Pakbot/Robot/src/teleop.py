#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import readchar
rospy.init_node("mv_bot")
move = rospy.Publisher("/move_robot",String)
while not  rospy.is_shutdown():
    #print("Use w,x,d,a,s to move robot")
    #m = input("Enter your move : ")
    key = readchar.readkey()
    move.publish(key)
