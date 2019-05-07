cmake_minimum_required(VERSION 2.8.3)
project(face_pkg)

find_package(catkin REQUIRED COMPONENTS

  rospy
  cv_bridge
  std_msgs
  message_generation
  intera_interface
  sensor_msgs
)


## Generate messages in the 'msg' folder
add_message_files(
  FILES

)

# Generate services in the 'srv' folder
add_service_files(
  FILES
  Face.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES robot_control
  CATKIN_DEPENDS 
  rospy
  std_msgs
  intera_interface
  cv_bridge
  sensor_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

install(
  DIRECTORY scripts/
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  USE_SOURCE_PERMISSIONS
)

