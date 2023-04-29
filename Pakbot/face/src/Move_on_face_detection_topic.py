#!/usr/bin/env python
import cv2, rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import time as t

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
def callback(data):
    faces = int(data.data)
    print(faces)
    if faces != 0:
        print("Found face, following")
        for i in range(abs(10)):
            twist = Twist()
            twist.linear.x = 0.15
            t.sleep(0.1)
            pub.publish(twist)
        t.sleep(2)
    else:
        twist = Twist()
        twist.linear.x = 0.0
        pub.publish(twist)
        

    # Do something with the image data


rospy.init_node('my_image_subscriber', anonymous=True)
rospy.Subscriber('/faces_detected', String, callback)
rospy.spin()
