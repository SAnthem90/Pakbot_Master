import rospy
import tf
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import TransformStamped

def scan_callback(scan_msg):
    # Create a transform from 'laser_frame' to 'base_link'
    tf_broadcaster.sendTransform(
        (0.0, 0.0, 0.0),  # Translation (x, y, z)
        (0.0, 0.0, 0.0, 1.0),  # Rotation (quaternion)
        rospy.Time.now(),  # Timestamp
        'laser',  # Child frame
        'odom'  # Parent frame
    )
    #$scan_msg.ranges = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5]

if __name__ == '__main__':
    rospy.init_node('scan_transform_publisher')

    tf_broadcaster = tf.TransformBroadcaster()

    rospy.Subscriber('scan', LaserScan, scan_callback)

    rospy.spin()
