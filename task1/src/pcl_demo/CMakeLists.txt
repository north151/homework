
# 最低cmake版本
cmake_minimum_required(VERSION 3.0.2)
# 功能包名/项目名
project(pcl_demo)


# 依赖包
find_package(catkin REQUIRED COMPONENTS
  pcl_conversions
  pcl_ros
  roscpp
  sensor_msgs
)
find_package(PCL)

# 构建时
catkin_package(
  # INCLUDE_DIRS include
  # LIBRARIES pcl_demo
  CATKIN_DEPENDS pcl_conversions pcl_ros roscpp sensor_msgs
  # DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${PCL_INCLUDE_DIRS}
)

# 节点名 源代码文件路径
add_executable(pcl_demo_node src/pcl_demo_node.cpp)

# 第一个是节点名
target_link_libraries(pcl_demo_node
  ${catkin_LIBRARIES}
  ${PCL_LIBRARIES}
)