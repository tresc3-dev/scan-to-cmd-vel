cmake_minimum_required(VERSION 3.0.2)
project(scan_to_cmd_vel)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
  sensor_msgs
)

catkin_package(
  CATKIN_DEPENDS geometry_msgs rospy sensor_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/scan_to_cmd_vel.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)