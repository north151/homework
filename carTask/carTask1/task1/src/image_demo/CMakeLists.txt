cmake_minimum_required(VERSION 3.0.2)
project(image_demo)

find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  image_transport
  roscpp
  rospy
  sensor_msgs
)
find_package(OpenCV)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ImageConverter
 CATKIN_DEPENDS cv_bridge image_transport roscpp rospy sensor_msgs
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)


add_executable(image_demo_node  src/image_demo_node.cpp)


target_link_libraries(image_demo_node
${catkin_LIBRARIES}
${OpenCV_LIBRARIES}
)


add_dependencies(image_demo_node 
${${PROJECT_NAME}_EXPORTED_TARGETS} 
${catkin_EXPORTED_TARGETS}
)

