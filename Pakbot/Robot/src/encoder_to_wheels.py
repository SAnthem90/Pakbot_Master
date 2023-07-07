import rospy
from std_msgs.msg import Int64
rospy.init_node("Encoders_to_TF")

lwheel = rospy.Publisher("/lwheel",Int64,queue_size=10)
rwheel = rospy.Publisher("/rwheel",Int64,queue_size=10)


def encoder1(data):
    encoder1 = data.data
    rwheel.publish(int(encoder1))

def encoder2(data):
    encoder2 = data.data
    lwheel.publish(int(encoder2))

rospy.Subscriber("/encoder1",Int64,encoder1)
rospy.Subscriber("/encoder2",Int64,encoder2)
#rwheel.publish(encoder1/100)
#lwheel.publish(encoder2/100)
rospy.spin()

