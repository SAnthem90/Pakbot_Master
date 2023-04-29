import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import String
import cv2

distance_publisher = rospy.Publisher("/distance",String,queue_size=10)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

ref_image = cv2.imread("ref.png")
Known_distance = 30
Known_width = 136

GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image):

	# finding the focal length
	focal_length = (width_in_rf_image * measured_distance) / real_width
	return focal_length

# distance estimation function
def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):

	distance = (real_face_width * Focal_Length)/face_width_in_frame

	# return the distance
	return distance


def face_data(image):

	face_width = 0 # making face width to zero

	# converting color image to gray scale image
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# detecting face in the image
	faces = face_detector.detectMultiScale(gray_image, 1.3, 5)

	# looping through the faces detect in the image
	# getting coordinates x, y , width and height
	for (x, y, h, w) in faces:

		# draw the rectangle on the face
		cv2.rectangle(image, (x, y), (x+w, y+h), GREEN, 2)

		# getting face width in the pixels
		face_width = w

	# return the face width in pixel
	return face_width


# reading reference_image from directory
ref_image = cv2.imread("ref.png")

# find the face width(pixels) in the reference_image
ref_image_face_width = face_data(ref_image)

# get the focal by calling "Focal_Length_Finder"
# face width in reference(pixels),
# Known_distance(centimeters),
# known_width(centimeters)
Focal_length_found = Focal_Length_Finder(
	Known_distance, Known_width, ref_image_face_width)


def callback(data):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    frame = cv_image
    if face_width_in_frame != 0:
        Distance = Distance_finder(Focal_length_found, Known_width, face_width_in_frame)

	# draw line as background of text
        cv2.line(frame, (30, 30), (230, 30), RED, 32)
        cv2.line(frame, (30, 30), (230, 30), BLACK, 28)
        
        cv2.putText(frame, f"Distance: {round(Distance,2)} CM", (30, 35),
	fonts, 0.6, GREEN, 2)
        distance_publisher.pub(Distance)


rospy.init_node('Distance_publisher', anonymous=True)
rospy.Subscriber('/video_topic', Image, callback)
rospy.spin()
