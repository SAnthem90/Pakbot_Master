#!/usr/bin/env python

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('map_odom_transform')

    # Create a transform broadcaster
    tf_broadcaster = tf.TransformBroadcaster()

    rate = rospy.Rate(10)  # Adjust the publishing rate as needed

    while not rospy.is_shutdown():
        # Define the transformation parameters
        translation = (0.0, 0.0, 0.0)  # Adjust the translation values as needed
        rotation = tf.transformations.quaternion_from_euler(0.0, 0.0, 1.57)  # Adjust the rotation values as needed

        # Publish the transform
        tf_broadcaster.sendTransform(translation,
                                     rotation,
                                     rospy.Time.now(),
                                     "odom",
                                     "map")

        rate.sleep()
