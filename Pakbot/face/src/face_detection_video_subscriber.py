#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image,CompressedImage
from cv_bridge import CvBridge
from std_msgs.msg import String
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
face_publisher = rospy.Publisher("/faces_detected",String,queue_size=10)
def callback(data):
    bridge = CvBridge()
    cv_image = bridge.compressed_imgmsg_to_cv2(data,"bgr8")
    gray = cv_image
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    print(str(len(faces)) + " Face(s) found")
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
    face_publisher.publish(str(len(faces)))

rospy.init_node('my_image_subscriber', anonymous=True)
rospy.Subscriber('/image/video/compressed', CompressedImage, callback)
rospy.spin()

