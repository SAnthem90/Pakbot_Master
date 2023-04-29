#!/usr/bin/env python
import cv2, rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import time as t

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
def callback(data):
    distance = float(data.data)
    print("Distance : "+str(distance))
    if distance:
        print("Found face, following")
        for i in range(int(distance/10)):
            twist = Twist()
            twist.linear.x = 0.15
            t.sleep(0.1)
            pub.publish(twist)
        t.sleep(2)
    else:
        twist = Twist()
        twist.linear.x = 0.0
        pub.publish(twist)

rospy.init_node('my_image_subscriber', anonymous=True)
rospy.Subscriber('/distance', String, callback)
rospy.spin()
