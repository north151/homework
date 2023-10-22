#include <ros/ros.h>
#include <nav_msgs/Odometry.h>

void speedCallback(const nav_msgs::Odometry::ConstPtr &msg)
{
    //读取激光雷达相关的话题/odom，可以获取小车的线速度和角速度

    /*   靠 里程计信息 计算出来的
    位移  (map坐标系，以现实世界 东南西北为准)
    线位移： position.x   
    角位移： orientation.z : 正向0  (左加右减)   (.x/.y 在此无用)
    车朝向： orientation.w : 正向1,反向0 

    速度 （base_link 坐标系，以车朝向为准）
    线速度： linear.x   (前正后负)   (.y/.z 在此无用)
    角速度： angular.z  (左正右负)   (.x/.y 在此无用)
    */

    setlocale(LC_ALL, "");
    ROS_INFO("角速度： wz=%0.2f ", msg->twist.twist.angular.z);
    ROS_INFO("线速度： vx=%0.2f \n", msg->twist.twist.linear.x);

    ROS_INFO("角位移： Wx=%0.2f ", msg->pose.pose.orientation.z);
    ROS_INFO("角偏转： Wz=%0.2f ", msg->pose.pose.orientation.w);
    ROS_INFO("线位移： SX=%0.2f  SY=%0.2f \n\n", msg->pose.pose.position.x, msg->pose.pose.position.y);

    return;
}


int main(int argc, char **argv)
{
    ros::init(argc, argv, "nav_subscriber");
    ros::NodeHandle n;
    //roslaunch scout_bringup open_rslidar.launch 
    ros::Subscriber speed_sub = n.subscribe("/odom", 10, speedCallback);
    ros::spin();
    return 0;
}