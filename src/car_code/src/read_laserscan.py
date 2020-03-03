#! /usr/bin/env python
import rospy
import math
from sensor_msgs.msg import LaserScan
import numpy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats


class readLaserscan:
    def __init__(self):
        rospy.init_node('read_laserscan')
        # get angle deviation
        self.angle_deviation = rospy.get_param('~angle_deviation')
        self.x_deviation = rospy.get_param('~x_deviation')
        self.y_deviation = rospy.get_param('~y_deviation')
        # define publisher and subscriber
        self.pub = rospy.Publisher('/laser_xy', numpy_msg(Floats), queue_size=10)
        self.rate = rospy.Rate(10)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.callback)
        rospy.spin()

    def callback(self, msg):
        # Lidar data array : msg.ranges
        # i : point radius
        # [i]*0.352 : point angle
        self.data = msg.ranges

        for i in range( len(self.data) ): 
            self.angle = ((i-341)*0.352)*math.pi/180 + self.angle_deviation
            self.radius = self.data[i]
            if self.radius < 5:
                self.y = math.sin(self.angle) * self.radius + self.y_deviation
                self.x = math.cos(self.angle) * self.radius + self.x_deviation
                # print([self.x, self.y])
                self.xy = numpy.array([self.x, self.y], dtype = numpy.float32)
                self.pub.publish(self.xy)


if __name__ == "__main__":
    try:
        readLaserscan()

        while not rospy.is_shutdown():
            readLaserscan.rate.sleep()

    except rospy.ROSInterruptException:
        pass



