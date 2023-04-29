#!/usr/bin/env python
# import the opencv library
import cv2
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
from cv_bridge import CvBridge, CvBridgeError
# define a video capture object
bridge = CvBridge()
vid = cv2.VideoCapture(0)
image_pub = rospy.Publisher("/video_topic", Image, queue_size=10)
fd = rospy.Publisher("/detected_faces", Int32, queue_size=2)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#print(detector)
rospy.init_node('video_publisher')

#r = rospy.Rate()
while not rospy.is_shutdown():

	ret, frame = vid.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
        # To draw a rectangle in a face 
        	cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2) 
        	roi_gray = gray[y:y+h, x:x+w]
        	roi_color = frame[y:y+h, x:x+w]
	
	ros_image = bridge.cv2_to_imgmsg(frame, "bgr8")
	fcs = (len(faces))
	image_pub.publish(ros_image)
	fd.publish(fcs)
	#r.sleep()#print(frame.shape)
	# Display the resulting frame

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
