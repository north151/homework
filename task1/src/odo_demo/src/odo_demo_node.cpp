#include <ros/ros.h>
#include <nav_msgs/Odometry.h>
#include <math.h>
#include <ctime>

float displacement = 0.0;   // base_link位移
float distance = 0.0;       // 起始点开始，行进的路程

// 相对原点
float pre_x = 0.0;              
float pre_y = 0.0;
float now_x = 0.0;
float now_y = 0.0;

float dxy = 0.0;   
float dist_xy = 0.0;
float fit_dist_xy = 0.0;
float loss = 0.03;       

// 时间
time_t pre_time = time(nullptr);
time_t now_time = time(nullptr);

bool flag = true;

void doMsg(const nav_msgs::Odometry::ConstPtr& msg)
{

    float wz = msg->twist.twist.angular.z;    // 角速度 wz
    if(wz<0.02 && wz>-0.02) 
    {
        wz = 0.0;
    }

    float wx = msg->pose.pose.orientation.z;  // 角位移 wx
    float ww = msg->pose.pose.orientation.w;  // 角偏转 ww

    float vx = msg->twist.twist.linear.x;     // 线速度 vx
    if(vx<0.01 && vx>-0.01) 
    {
        vx = 0.0;
    }
    now_time = time(nullptr);;
    float dt = difftime(now_time, pre_time);

    float dx = dt*vx;                        // 位移
    float ds = (dx>0 ? dx:0.0-dx);            // 距离

    displacement += dx;                       // base_link 坐标系下正反向行进路程
    distance += (dx>0 ? dx:0.0-dx);           // 起始点开始，行进的路程

    now_x = msg->pose.pose.position.x;
    now_y = msg->pose.pose.position.y;
    dxy =  sqrt(pow(now_x-pre_x,2) + pow(now_y-pre_y,2));

    if(dxy > loss)
    {
        pre_x = now_x;
        pre_y = now_y;
        if(flag == true)
        {
            dist_xy = 0.0;
            fit_dist_xy = 0.0;
        }
        else
        {
            dist_xy += dxy;
            fit_dist_xy = 1.0183 * dist_xy + 0.0059;
        }
        flag = false;
    }

    ROS_INFO("角速度： wz=%0.3f   角位移： wx=%0.3f   角偏转ww=%0.3f  ", wz, wx, ww);
    ROS_INFO("线速度： vx=%0.3f", vx);
    ROS_INFO("base_link 位移：  disp=%0.3f  ", displacement);
    ROS_INFO("积分vx 移动距离:  Sadd=%0.3f  ", distance);
    ROS_INFO("Map坐标移动距离:  Smap=%0.3f  \n\n\n", fit_dist_xy);

    pre_time = time(nullptr);
    return;

}


int main(int argc, char  *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc, argv, "odom_sub");
    ros::NodeHandle nh;
    pre_time = time(nullptr);
    ros::Subscriber sub = nh.subscribe("/odom",1000,doMsg);
    ros::spin();
    return 0;
}
 
