#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
 
static const std::string OPENCV_WINDOW_COLOR = "彩色相机";
static const std::string OPENCV_WINDOW_DEPTH = "深度相机";
 


class ImageConverter
{
  ros::NodeHandle nh_;
  image_transport::ImageTransport it_;
  image_transport::Subscriber image_sub_color;
  image_transport::Subscriber image_sub_depth;
 
public:
  ImageConverter() : it_(nh_)
  {
    image_sub_color = it_.subscribe("/camera/color/image_raw", 1, &ImageConverter::imageCb, this);
    image_sub_depth = it_.subscribe("camera/depth/image_rect_raw",1,&ImageConverter::depthCb, this);
 
    cv::namedWindow(OPENCV_WINDOW_COLOR);
    cv::namedWindow(OPENCV_WINDOW_DEPTH);
  }
 
  ~ImageConverter()
  {
    cv::destroyWindow(OPENCV_WINDOW_COLOR);
    cv::destroyWindow(OPENCV_WINDOW_DEPTH);
  }
 
  void imageCb(const sensor_msgs::ImageConstPtr& msg)
  {
    cv_bridge::CvImagePtr cv_ptr;
    try
    {
      cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
    }
    catch (cv_bridge::Exception& e)
    {
      ROS_ERROR("cv_bridge exception: %s", e.what());
      return;
    }
    // 刷新窗口
    cv::imshow(OPENCV_WINDOW_COLOR, cv_ptr->image);
    cv::waitKey(3);
    return;
  }

  void depthCb(const sensor_msgs::ImageConstPtr &msg)
  {
    cv_bridge::CvImagePtr cv_ptr;
    try
    {
      cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::TYPE_32FC1);
    }
    catch (cv_bridge::Exception& e)
    {
      ROS_ERROR("cv_bridge exception: %s", e.what());
      return;
    }
    // 刷新窗口
    cv::imshow(OPENCV_WINDOW_DEPTH, cv_ptr->image);
    cv::waitKey(3);
    return;
  }
};

int main(int argc, char** argv)
{
  ros::init(argc, argv, "image_subscriber");
  ImageConverter ic;
  ros::spin();
  return 0;
}
