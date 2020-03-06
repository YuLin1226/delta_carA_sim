#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from fiducial_msgs.msg import FiducialTransformArray, FiducialTransform
import tf

class aruco_detect():
    def __init__(self):
        rospy.init_node('Get_Fiducial_Transforms', anonymous=True)
        rospy.Subscriber("/fiducial_transforms", FiducialTransformArray, self.get_fidu_tf)
        # tf part
        self.br = tf.TransformBroadcaster()
        self.rate = rospy.Rate(10)


    def get_fidu_tf(self, msg):
        self.currentSeq = msg.image_seq
        self.imageTime = msg.header.stamp
        self.aruco = msg.transforms[0]
        self.aruco_tf = self.aruco.transform
        self.aruco_id = self.aruco.fiducial_id
        self.aruco_tf_trans = self.aruco_tf.translation
        self.aruco_tf_rot   = self.aruco_tf.rotation
        # print(type(self.aruco_tf_trans.x))
        
        # tf data:
        # x = self.aruco_tf_trans.x  # red axis in RViz
        # y = self.aruco_tf_trans.y  # green axis in RViz
        # z = self.aruco_tf_trans.z  # blue axis in RViz
        
        self.br.sendTransform(  (self.aruco_tf_trans.x, self.aruco_tf_trans.y, self.aruco_tf_trans.z), 
                                (self.aruco_tf_rot.x, self.aruco_tf_rot.y, self.aruco_tf_rot.z, self.aruco_tf_rot.w), 
                                rospy.Time.now(), 
                                "aruco_%d" %self.aruco_id, 
                                "camera")
        self.rate.sleep()


if __name__ == '__main__':
    try:
        a = aruco_detect()
        while not rospy.is_shutdown():
            pass

    except rospy.ROSInterruptException:
        pass



           