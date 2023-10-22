cmake_minimum_required(VERSION 3.0.2)
project(info_demo)

find_package(catkin REQUIRED COMPONENTS
  nav_msgs
  roscpp
  std_msgs
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES info_demo
  CATKIN_DEPENDS nav_msgs roscpp std_msgs
#  DEPENDS system_lib
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(info_demo_node src/info_demo_node.cpp)



target_link_libraries(info_demo_node
   ${catkin_LIBRARIES}
 )

add_dependencies(info_demo_node 
${${PROJECT_NAME}_EXPORTED_TARGETS} 
${catkin_EXPORTED_TARGETS}
)
