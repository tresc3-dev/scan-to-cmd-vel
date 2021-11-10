#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class TestPub(object):
    def __init__(self):
        self.lin_vel = rospy.get_param('~lin_vel', 0.2)
        self.ang_vel = rospy.get_param('~ang_vel', 1.5757)

        self._cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self._scan_sub = rospy.Subscriber('scan', LaserScan, self.callBack)

    def callBack(self, data):
        # scan 데이터 처리
        # data.ranges : list of scan

        
        # twist msg 생성 (commanded velocities)
        cmd_vel = Twist()

        # 전진
        cmd_vel.linear.x = self.lin_vel
        # 후진
        cmd_vel.linear.x = -self.lin_vel
        # 좌회전
        cmd_vel.angular.z = self.ang_vel
        # 우회전
        cmd_vel.angular.z = -self.ang_vel

        # twist msg 발행
        self._cmd_vel_pub.publish(cmd_vel)

if __name__ == "__main__":
    try:
        # start ROS node
        rospy.init_node('test_node')
        # initialize keyboard teleoperation
        test_pub = TestPub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
        