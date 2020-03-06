#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from fiducial_msgs.msg import FiducialTransformArray, FiducialTransform
import tf

class sub():
    def __init__(self):
        rospy.init_node('Get_Fiducial_Transforms', anonymous=True)
        rospy.Subscriber("/fiducial_transforms", FiducialTransformArray, self.get_fidu_tf)
        # self.list = FiducialTransform()

    def get_fidu_tf(self, msg):
        self.currentSeq = msg.image_seq
        self.imageTime = msg.header.stamp
        self.aruco = msg.transforms[0]
        self.aruco_tf = self.aruco.transform
        self.aruco_id = self.aruco.fiducial_id
        self.aruco_tf_trans = self.aruco_tf.translation
        self.aruco_tf_rot   = self.aruco_tf.rotation

        # tf data:
        # x = self.aruco_tf_trans.x
        # y = self.aruco_tf_trans.y
        # z = self.aruco_tf_trans.z
        



if __name__ == '__main__':
    try:
        a = sub()
        while not rospy.is_shutdown():
            pass

    except rospy.ROSInterruptException:
        pass



           