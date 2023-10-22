



## 基本概念

```python
# ROS
	开发机器人 "应用程序" 的、类似操作系统的机器人 "软件平台"
```



```
消息通信、
消息文件、
名称(Name)、
坐标变换(TF)、
客户端库、
不同设备之间的通信、
文件系统
构建系统

```





```python
# 节点  （可视为: 实现某个功能的一个进程）
  运行的最小处理器单元,可以把它看作一个可执行程序
  节点节点： 直接通信，与主节点无关，(ROS_HOSTNAME)
  创建节点： 一个目的创建一个节点
           向主节点注册节点的 名称,注册消息形式、URI地址、端口、
                           发布者、订阅者、服务服务器、服务客户端。
```



```python
# 主节点
  类似于名称服务器,负责节点间的 "连接" 和 "消息通信"。\
  默认端口：11311 (ROS_MASTER_URI)
  roscore: 主节点运行命令,注册每个节点。没有主节点,节点间不能建立访问。
  
  主节点使用XMLRPC与节点进行通信。
  (XML远程过程调用,XML-Remote Procedure Call,基于HTTP) 
  节点不与主节点保持连接,只在需要注册自己的信息或向其他节点发送请求信息时才能访问主节点。
```



```python
# 功能包 (package) 
  构成ROS的基本单元, ROS应用程序是以功能包为单位开发。
    
  至少包括一个以上的"节点" 或 拥有用于运行其他功能包的节点的配置文件
  它还包含功能包所需的所有文件,如用于运行各种进程的ROS依赖库、数据集和配置文件等。
```



```python
# 元功能包
  元功能包(metapackage) 是一个 "具有共同目的" 的功能包的 "集合"。
  例如,导航元功能包包含AMCL、DWA、EKF和map_server等10余个功能包。
```





## 消息通信

### 消息

```python
  节点之间通过消息(message) 来发送和接收数据。
  数据结构：整型,浮点型,布尔型，简单数据结构，列举消息的消息数组。
  通信方法: TCPROS,UDPROS等,
  消息类型:
    单向消息: "发送/接收"方式的话题(topic)
    双向消息: "请求(request)/响应(response)" 方式的服务。
        
        
```



![1111](https://cdn.jsdelivr.net/gh/north151/ImageBed1/image_Linux/1111.png)





### 异步单向通信

```python
# 话题   (需要连续发送消息的传感器数据； 直接发）
  发布者节点关于话题向主节点注册,
    
  发布关于该话题的消息,
  订阅者节点从 主节点 获取 发布者节点 的信息,
  订阅者节点 直接连接 到 发布者节点, 用话题发送和接收消息。

# 发布者节点
  发送话题内容对应的消息,单个节点可以成为多个发布者。
  在主节点上注册自己话题等多种信息,
  向订阅者节点发送消息,声明自己是执行发布的个体。
  

# 订阅与订阅者
  接收话题内容对应的消息,单个节点可以成为多个订阅者。
  在主节点上注册自己的话题等多种信息,并从主节点接收发布者节点的信息,
  直接联系发布者节点来接收消息,并声明自己执行订阅的个体。
  

```





### 同步双向通信

```python
# 服务:  （执行特定操作时； 接到请求才发送）
  响应请求的服务服务器 和 请求后接收响应的服务客户端。
  与话题不同,是一次性的消息通信。请求和响应完成时,两个节点的连接被断开。

# 服务 服务器 （请求和响应都是消息）
  输入: 请求
  输出: 响应  
  服务服务器收到服务请求后,执行指定命令的节点,并将结果下发给服务客户端。

# 服务 客户端
  输出: 请求
  输入: 响应
  服务客户端用于传达给定命令并接收结果值的节点。


```







### 异步双向通信

```python
# 动作
  在处理请求之后需要很长的响应,并且需要中途反馈值。
    
# 动作 服务器
  输入: 接收的目标
  输出: 结果和反馈值

# 动作客户端
  输出: 目标
  输入: 结果和反馈值
  给出下一个指示或取消目标。


```





### 参数

```bash
# 参数 (配置文件)
  节点中使用的全局变量
  是默认(default)设置, 可指定与外部设备连接的PC的USB端口、相机校准值、电机速度或命令的最大值和最小值等设置值。

# 参数服务器 (parameter server) 
	 在功能包中使用参数时,注册各参数的服务器。参数服务器是主节点的一个功能。
    
    
```





















## 文件系统

```bash
# 功能包安装: 
	二进制：sudo apt-get install 功能包名
	源代码: git到src下，再catkin_make
	
	
# 安装目录: /opt/ros/
# 工作目录： ~/catkin_ws/
									/build  构建相关的文件
									/devel  msg、srv头文件、用户包库、可执行文件
									/src    用户功能包
									
# 用户功能包目录
  CMakeLists.txt 构建配置文件
  package.xml    功能包配置文件
  /include       头文件
  /launch        用于roslaunch的启动文件
  /node          用于rospy的脚本
  
  /msg           消息文件
  /srv           服务文件
  /action        动作文件
  
  /src           源代码文件
  

```











## 构建系统

```python
# catkin
  将CMake修改成专为ROS定制的catkin构建系统
  CMakeLists.txt : 描述构建环境
  package..xml   : 描述功能包信息
    
# roscore
  运行ROS主节点的命令。
  可在同一个网络内的计算机上运行它。但除支持多roscore的情况,一个网络中只能运行一个。使用在ROS_MASTER_URI变量中列出的URI地址和端口,默认本地IP:11311。
    
# rosrun [功能包] [要运行的节点]
  运行一个节点,ROS_HOSTNAME为URI,端口为任意固有值。
    
# roslauch
  运行多个节点
  使用*.launch文件设置可执行节点,它基于可扩展标记语言(XML),并提供XML标记形式的多种选项。

# rosbag
  用户可以保存ROS中发送和接收的消息的数据,保存格式为*.bag
  用来存储信息并在需要时可以回放以前的情况。即不重复执行之前的实验,也能通过回放保存的bag文件来反复利用当时的传感器值,在开发那些需要反复修改程序算法的时候会非常有用。

# 状态图
  直观表示：节点、话题、发布者和订阅者之间关系。是正在运行的消息通信的图形表示。
  但不能为一次性服务创建状态图。
  由rqt_graph功能包的rqt_graph节点完成。
  rqt_graph , rosrun rqt_graph rqt_graph。

# 名称
  节点、参数、话题和服务都有名称
  在运行时可被更改,也能设定多个不同的名称。

```



```python
# MD5
  检查消息发送/接收的完整性
# RPC
  远程过程调用,调用另一台计算机的子程序
# XML
  可扩展标记语言,使用标签来指定数据结构,
  ROS中用于*.launch、*.urdf和package.xml等
# XMLRPC
  用既不保持连接状态、也不检查连接状态的请求和响应方式的HTTP协议
# 消息方式
  基于TCP/IP：TCPROS
  基于UDP：   UDPROS
```





```python
# 创建功能包 (在~/catkin/src下,名称全英文小写/_)
  catkin_create_pkg [功能包名] [依赖功能包1] [依赖功能包n]
  依赖包可在package.xml中添加
  
```





### CMakeLists.txt

```bash
# cmake最低版本
cmake_minimum_required(VERSION 3.0.2)

# 功能包名称
project(test)

# 构建时的依赖包
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

# 使用 Boost 时必须安装system功能包
find_package(Boost REQUIRED COMPONENTS system)

# 使用rospy时的配置选项
catkin_python_setup()


#######################################################

# 添加消息文件
add_message_files(
  FILES          # 引用msg目录.msg文件,自动生成头文件
  Message1.msg
  Message2.msg
)

# 添加服务文件
add_service_files(
  FILES          # 引用srv目录.srv文件,自动生成头文件
  Service1.srv
  Service2.srv
)

# 添加动作文件
add_action_files(
  FILES
  Action1.action
  Action2.action
)

########################################################


# 设置依赖的消息选项
generate_messages(
  DEPENDENCIES
  std_msgs
)





################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

# 使用dynamic_reconfigure时加载要引用的配置文件
generate_dynamic_reconfigure_options(
  cfg/DynReconf1.cfg
  cfg/DynReconf2.cfg
)

###################################
## catkin specific configuration ##
###################################

# 构建
catkin_package(
 INCLUDE_DIRS include             # 头文件目录
 LIBRARIES test                   # 功能包库
 CATKIN_DEPENDS roscpp std_msgs   # 依赖功能包
 DEPENDS system_lib               # 系统依赖包
)

###########
## Build ##
###########

# 头文件
include_directories(
  ${catkin_INCLUDE_DIRS}
)

# 声明需要创建的库
add_library(${PROJECT_NAME}
  src/${PROJECT_NAME}/test.cpp
)

# 
add_dependencies(
${PROJECT_NAME} 
${${PROJECT_NAME}_EXPORTED_TARGETS} 
${catkin_EXPORTED_TARGETS}
)

# 生成可执行文件的依靠
add_executable(${PROJECT_NAME}_node src/test_node.cpp)

# 
set_target_properties(
${PROJECT_NAME}_node PROPERTIES OUTPUT_NAME node PREFIX "")

#
add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

# 将库和可执行文件链接
target_link_libraries(
  ${PROJECT_NAME}_node
  ${catkin_LIBRARIES}
)

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
# catkin_install_python(PROGRAMS
#   scripts/my_python_script
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark executables for installation
## See http://docs.ros.org/melodic/api/catkin/html/howto/format1/building_executables.html
# install(TARGETS ${PROJECT_NAME}_node
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark libraries for installation
## See http://docs.ros.org/melodic/api/catkin/html/howto/format1/building_libraries.html
# install(TARGETS ${PROJECT_NAME}
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
# )

## Mark cpp header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_test.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
```







### package.xml

```xml
<!-- 定义文档语法-->
<?xml version="1.0"?>

<!--ROS功能包配置部分-->
<package format="2">
  <!--功能包名称-->
  <name>test</name>
  <!--功能包版本-->
  <version>0.0.0</version>
  <!--简要描述-->
  <description>The test package</description>
  <!--功能包管理者信息-->
  <maintainer email="north151@todo.todo">north151</maintainer>
  <!--版权许可证-->
  <license>TODO</license>
  <!--功能包说明-->
  <url type="website">http://wiki.ros.org/test</url>
  <!--开发人员信息(可多条)-->
  <author email="jane.doe@example.com">Jane Doe</author>

  <!--构建系统的依赖关系-->
  <buildtool_depend>catkin</buildtool_depend>
  <!--依赖功能包-->
  <build_depend>roscpp</build_depend>
  <build_depend>std_msgs</build_depend>

  <build_export_depend>roscpp</build_export_depend>
  <build_export_depend>std_msgs</build_export_depend>

  <exec_depend>roscpp</exec_depend>
  <exec_depend>std_msgs</exec_depend>

  <export>
    <!-- Other tools can request additional information be placed here -->
  </export>
    
    
</package>
```



```
std_msgs : 标准消息包 
roscpp   : 客户端库   (为在ROS中使用C++)

```







## 基本命令

```bash
# 打开指定功能包
roscd <package_name>
# 列出功能包目录
```















