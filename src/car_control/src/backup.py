#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import Joy

class WheelControl():

    def __init__(self, node, topic):
        self.cmd_value = 0.0
        #Define a subscriber to get an array of joystick
        rospy.init_node(node, anonymous=True)
        rospy.Subscriber(topic, Joy, self.get_value)
        self.vel = 0
        self.cmd_Forward = 0
        self.cmd_Turn =0

    def get_value(self, cmd_value):
        self.cmd_Forward = cmd_value.axes[3]
        self.cmd_Turn = cmd_value.axes[0]

    def move_control(self, topic, vel_cmd, vel_last):
        #Define publisher
        self.vel_publisher = rospy.Publisher(topic, Float64, queue_size=10)

        # use pub rate to adjust the speed.
        self.rate = rospy.Rate(100)

        # Determine vel command
        self.vel = Float64()
        self.vel = vel_last + 0.031415*vel_cmd*0.5
        
        # Pub command
        self.vel_publisher.publish(self.vel)
        

if __name__ == '__main__':
    try:
        wheel = WheelControl('move', "joy")

        left_vel_last = 0
        right_vel_last = 0

        while not rospy.is_shutdown():

            cmd_Forward = wheel.cmd_Forward
            cmd_Turn = wheel.cmd_Turn
            if cmd_Turn > 0:
                cmd_Left = 0
                cmd_Right = cmd_Turn
            
            else:
                cmd_Left = -cmd_Turn
                cmd_Right = 0

            cmd_Left += cmd_Forward
            cmd_Right += cmd_Forward

            # wheel.move_control('test',cmd_Left,left_vel_last)
            wheel.move_control('/car/joint1_position_controller/command', cmd_Left, left_vel_last)
            left_vel_last += wheel.vel
            wheel.rate.sleep()
            wheel.move_control('/car/joint2_position_controller/command', cmd_Right, right_vel_last)
            right_vel_last += wheel.vel
            wheel.rate.sleep()
            

    except rospy.ROSInterruptException:
        pass
