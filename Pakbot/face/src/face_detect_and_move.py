#!/usr/bin/env python
import cv2, rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from geometry_msgs.msg import Twist
import time as t


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
def callback(data):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    gray = cv_image
    #print(cv_image.shape)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    #for (x, y, w, h) in faces:
        #cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
    if len(faces) > 0:
        print("Found face, following")
        for i in range(abs(1)):
            twist = Twist()
            twist.linear.x = 0.15
            t.sleep(0.1)
            pub.publish(twist)
    else:
        twist = Twist()
        twist.linear.x = 0.0
        pub.publish(twist)
        

    # Do something with the image data


rospy.init_node('my_image_subscriber', anonymous=True)
rospy.Subscriber('/video_topic', Image, callback)
rospy.spin()

