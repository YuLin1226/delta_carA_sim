#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

class WheelControl():

    def __init__(self):
        rospy.init_node('wheel_controller', anonymous=True)
        # pub1 : left wheel // pub2 : right wheel
        self.pub1 = rospy.Publisher('/car/left_wheel_controller/command', Float64, queue_size=10)
        self.pub2 = rospy.Publisher('/car/right_wheel_controller/command', Float64, queue_size=10)
        self.sampling_rate = 10
        self.rate = rospy.Rate(self.sampling_rate)
        self.last_left_vel = 0
        self.last_right_vel = 0
        rospy.Subscriber('/cmd_vel', Twist, self.get_value)
        rospy.spin()

    def get_value(self, cmd_value):
        self.cmd_lx = cmd_value.linear.x / self.sampling_rate
        self.cmd_az = cmd_value.angular.z / self.sampling_rate
        self.cal_diff_cmd(self.cmd_lx, self.cmd_az)
        self.move_control(self.left_vel, self.right_vel)

    def cal_diff_cmd(self, lx, az):
        self.left_vel  = self.last_left_vel  + (lx - az*0.35)*0.15
        self.right_vel = self.last_right_vel + (lx + az*0.35)*0.15
        self.last_left_vel  = self.left_vel
        self.last_right_vel = self.right_vel

    def move_control(self, left_vel, right_vel): 
        self.pub1.publish(left_vel)
        self.pub2.publish(right_vel)
        
    
if __name__ == '__main__':
    try:
        WheelControl()
        
            
    except rospy.ROSInterruptException:
        pass
