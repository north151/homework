// Generated by gencpp from file autoware_msgs/CloudCluster.msg
// DO NOT EDIT!


#ifndef AUTOWARE_MSGS_MESSAGE_CLOUDCLUSTER_H
#define AUTOWARE_MSGS_MESSAGE_CLOUDCLUSTER_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <sensor_msgs/PointCloud2.h>
#include <geometry_msgs/PointStamped.h>
#include <geometry_msgs/PointStamped.h>
#include <geometry_msgs/PointStamped.h>
#include <geometry_msgs/PointStamped.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Vector3.h>
#include <std_msgs/Float32MultiArray.h>
#include <jsk_recognition_msgs/BoundingBox.h>
#include <geometry_msgs/PolygonStamped.h>

namespace autoware_msgs
{
template <class ContainerAllocator>
struct CloudCluster_
{
  typedef CloudCluster_<ContainerAllocator> Type;

  CloudCluster_()
    : header()
    , id(0)
    , label()
    , score(0.0)
    , cloud()
    , min_point()
    , max_point()
    , avg_point()
    , centroid_point()
    , estimated_angle(0.0)
    , dimensions()
    , eigen_values()
    , eigen_vectors()
    , fpfh_descriptor()
    , bounding_box()
    , convex_hull()
    , indicator_state(0)  {
    }
  CloudCluster_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , id(0)
    , label(_alloc)
    , score(0.0)
    , cloud(_alloc)
    , min_point(_alloc)
    , max_point(_alloc)
    , avg_point(_alloc)
    , centroid_point(_alloc)
    , estimated_angle(0.0)
    , dimensions(_alloc)
    , eigen_values(_alloc)
    , eigen_vectors(_alloc)
    , fpfh_descriptor(_alloc)
    , bounding_box(_alloc)
    , convex_hull(_alloc)
    , indicator_state(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint32_t _id_type;
  _id_type id;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _label_type;
  _label_type label;

   typedef double _score_type;
  _score_type score;

   typedef  ::sensor_msgs::PointCloud2_<ContainerAllocator>  _cloud_type;
  _cloud_type cloud;

   typedef  ::geometry_msgs::PointStamped_<ContainerAllocator>  _min_point_type;
  _min_point_type min_point;

   typedef  ::geometry_msgs::PointStamped_<ContainerAllocator>  _max_point_type;
  _max_point_type max_point;

   typedef  ::geometry_msgs::PointStamped_<ContainerAllocator>  _avg_point_type;
  _avg_point_type avg_point;

   typedef  ::geometry_msgs::PointStamped_<ContainerAllocator>  _centroid_point_type;
  _centroid_point_type centroid_point;

   typedef double _estimated_angle_type;
  _estimated_angle_type estimated_angle;

   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _dimensions_type;
  _dimensions_type dimensions;

   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _eigen_values_type;
  _eigen_values_type eigen_values;

   typedef std::vector< ::geometry_msgs::Vector3_<ContainerAllocator> , typename std::allocator_traits<ContainerAllocator>::template rebind_alloc< ::geometry_msgs::Vector3_<ContainerAllocator> >> _eigen_vectors_type;
  _eigen_vectors_type eigen_vectors;

   typedef  ::std_msgs::Float32MultiArray_<ContainerAllocator>  _fpfh_descriptor_type;
  _fpfh_descriptor_type fpfh_descriptor;

   typedef  ::jsk_recognition_msgs::BoundingBox_<ContainerAllocator>  _bounding_box_type;
  _bounding_box_type bounding_box;

   typedef  ::geometry_msgs::PolygonStamped_<ContainerAllocator>  _convex_hull_type;
  _convex_hull_type convex_hull;

   typedef uint32_t _indicator_state_type;
  _indicator_state_type indicator_state;





  typedef boost::shared_ptr< ::autoware_msgs::CloudCluster_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::autoware_msgs::CloudCluster_<ContainerAllocator> const> ConstPtr;

}; // struct CloudCluster_

typedef ::autoware_msgs::CloudCluster_<std::allocator<void> > CloudCluster;

typedef boost::shared_ptr< ::autoware_msgs::CloudCluster > CloudClusterPtr;
typedef boost::shared_ptr< ::autoware_msgs::CloudCluster const> CloudClusterConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::autoware_msgs::CloudCluster_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::autoware_msgs::CloudCluster_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::autoware_msgs::CloudCluster_<ContainerAllocator1> & lhs, const ::autoware_msgs::CloudCluster_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.id == rhs.id &&
    lhs.label == rhs.label &&
    lhs.score == rhs.score &&
    lhs.cloud == rhs.cloud &&
    lhs.min_point == rhs.min_point &&
    lhs.max_point == rhs.max_point &&
    lhs.avg_point == rhs.avg_point &&
    lhs.centroid_point == rhs.centroid_point &&
    lhs.estimated_angle == rhs.estimated_angle &&
    lhs.dimensions == rhs.dimensions &&
    lhs.eigen_values == rhs.eigen_values &&
    lhs.eigen_vectors == rhs.eigen_vectors &&
    lhs.fpfh_descriptor == rhs.fpfh_descriptor &&
    lhs.bounding_box == rhs.bounding_box &&
    lhs.convex_hull == rhs.convex_hull &&
    lhs.indicator_state == rhs.indicator_state;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::autoware_msgs::CloudCluster_<ContainerAllocator1> & lhs, const ::autoware_msgs::CloudCluster_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace autoware_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::autoware_msgs::CloudCluster_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::autoware_msgs::CloudCluster_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::autoware_msgs::CloudCluster_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::autoware_msgs::CloudCluster_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::autoware_msgs::CloudCluster_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::autoware_msgs::CloudCluster_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::autoware_msgs::CloudCluster_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ee7b21b447ceefba70710356a4b6162b";
  }

  static const char* value(const ::autoware_msgs::CloudCluster_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xee7b21b447ceefbaULL;
  static const uint64_t static_value2 = 0x70710356a4b6162bULL;
};

template<class ContainerAllocator>
struct DataType< ::autoware_msgs::CloudCluster_<ContainerAllocator> >
{
  static const char* value()
  {
    return "autoware_msgs/CloudCluster";
  }

  static const char* value(const ::autoware_msgs::CloudCluster_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::autoware_msgs::CloudCluster_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/Header header\n"
"\n"
"uint32 id\n"
"string label\n"
"float64 score\n"
"\n"
"sensor_msgs/PointCloud2 cloud\n"
"\n"
"geometry_msgs/PointStamped min_point\n"
"geometry_msgs/PointStamped max_point\n"
"geometry_msgs/PointStamped avg_point\n"
"geometry_msgs/PointStamped centroid_point\n"
"\n"
"float64 estimated_angle\n"
"\n"
"geometry_msgs/Vector3 dimensions\n"
"geometry_msgs/Vector3 eigen_values\n"
"geometry_msgs/Vector3[] eigen_vectors\n"
"\n"
"#Array of 33 floats containing the FPFH descriptor\n"
"std_msgs/Float32MultiArray fpfh_descriptor \n"
"\n"
"jsk_recognition_msgs/BoundingBox bounding_box\n"
"geometry_msgs/PolygonStamped convex_hull\n"
"\n"
"# Indicator information\n"
"# INDICATOR_LEFT 0\n"
"# INDICATOR_RIGHT 1\n"
"# INDICATOR_BOTH 2\n"
"# INDICATOR_NONE 3\n"
"uint32 indicator_state\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: sensor_msgs/PointCloud2\n"
"# This message holds a collection of N-dimensional points, which may\n"
"# contain additional information such as normals, intensity, etc. The\n"
"# point data is stored as a binary blob, its layout described by the\n"
"# contents of the \"fields\" array.\n"
"\n"
"# The point cloud data may be organized 2d (image-like) or 1d\n"
"# (unordered). Point clouds organized as 2d images may be produced by\n"
"# camera depth sensors such as stereo or time-of-flight.\n"
"\n"
"# Time of sensor data acquisition, and the coordinate frame ID (for 3d\n"
"# points).\n"
"Header header\n"
"\n"
"# 2D structure of the point cloud. If the cloud is unordered, height is\n"
"# 1 and width is the length of the point cloud.\n"
"uint32 height\n"
"uint32 width\n"
"\n"
"# Describes the channels and their layout in the binary data blob.\n"
"PointField[] fields\n"
"\n"
"bool    is_bigendian # Is this data bigendian?\n"
"uint32  point_step   # Length of a point in bytes\n"
"uint32  row_step     # Length of a row in bytes\n"
"uint8[] data         # Actual point data, size is (row_step*height)\n"
"\n"
"bool is_dense        # True if there are no invalid points\n"
"\n"
"================================================================================\n"
"MSG: sensor_msgs/PointField\n"
"# This message holds the description of one point entry in the\n"
"# PointCloud2 message format.\n"
"uint8 INT8    = 1\n"
"uint8 UINT8   = 2\n"
"uint8 INT16   = 3\n"
"uint8 UINT16  = 4\n"
"uint8 INT32   = 5\n"
"uint8 UINT32  = 6\n"
"uint8 FLOAT32 = 7\n"
"uint8 FLOAT64 = 8\n"
"\n"
"string name      # Name of field\n"
"uint32 offset    # Offset from start of point struct\n"
"uint8  datatype  # Datatype enumeration, see above\n"
"uint32 count     # How many elements in the field\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/PointStamped\n"
"# This represents a Point with reference coordinate frame and timestamp\n"
"Header header\n"
"Point point\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"================================================================================\n"
"MSG: std_msgs/Float32MultiArray\n"
"# Please look at the MultiArrayLayout message definition for\n"
"# documentation on all multiarrays.\n"
"\n"
"MultiArrayLayout  layout        # specification of data layout\n"
"float32[]         data          # array of data\n"
"\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/MultiArrayLayout\n"
"# The multiarray declares a generic multi-dimensional array of a\n"
"# particular data type.  Dimensions are ordered from outer most\n"
"# to inner most.\n"
"\n"
"MultiArrayDimension[] dim # Array of dimension properties\n"
"uint32 data_offset        # padding elements at front of data\n"
"\n"
"# Accessors should ALWAYS be written in terms of dimension stride\n"
"# and specified outer-most dimension first.\n"
"# \n"
"# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n"
"#\n"
"# A standard, 3-channel 640x480 image with interleaved color channels\n"
"# would be specified as:\n"
"#\n"
"# dim[0].label  = \"height\"\n"
"# dim[0].size   = 480\n"
"# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n"
"# dim[1].label  = \"width\"\n"
"# dim[1].size   = 640\n"
"# dim[1].stride = 3*640 = 1920\n"
"# dim[2].label  = \"channel\"\n"
"# dim[2].size   = 3\n"
"# dim[2].stride = 3\n"
"#\n"
"# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/MultiArrayDimension\n"
"string label   # label of given dimension\n"
"uint32 size    # size of given dimension (in type units)\n"
"uint32 stride  # stride of given dimension\n"
"================================================================================\n"
"MSG: jsk_recognition_msgs/BoundingBox\n"
"# BoundingBox represents a oriented bounding box.\n"
"Header header\n"
"geometry_msgs/Pose pose\n"
"geometry_msgs/Vector3 dimensions  # size of bounding box (x, y, z)\n"
"# You can use this field to hold value such as likelihood\n"
"float32 value\n"
"uint32 label\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/PolygonStamped\n"
"# This represents a Polygon with reference coordinate frame and timestamp\n"
"Header header\n"
"Polygon polygon\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Polygon\n"
"#A specification of a polygon where the first and last points are assumed to be connected\n"
"Point32[] points\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point32\n"
"# This contains the position of a point in free space(with 32 bits of precision).\n"
"# It is recommeded to use Point wherever possible instead of Point32.  \n"
"# \n"
"# This recommendation is to promote interoperability.  \n"
"#\n"
"# This message is designed to take up less space when sending\n"
"# lots of points at once, as in the case of a PointCloud.  \n"
"\n"
"float32 x\n"
"float32 y\n"
"float32 z\n"
;
  }

  static const char* value(const ::autoware_msgs::CloudCluster_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::autoware_msgs::CloudCluster_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.id);
      stream.next(m.label);
      stream.next(m.score);
      stream.next(m.cloud);
      stream.next(m.min_point);
      stream.next(m.max_point);
      stream.next(m.avg_point);
      stream.next(m.centroid_point);
      stream.next(m.estimated_angle);
      stream.next(m.dimensions);
      stream.next(m.eigen_values);
      stream.next(m.eigen_vectors);
      stream.next(m.fpfh_descriptor);
      stream.next(m.bounding_box);
      stream.next(m.convex_hull);
      stream.next(m.indicator_state);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CloudCluster_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::autoware_msgs::CloudCluster_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::autoware_msgs::CloudCluster_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "id: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.id);
    s << indent << "label: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.label);
    s << indent << "score: ";
    Printer<double>::stream(s, indent + "  ", v.score);
    s << indent << "cloud: ";
    s << std::endl;
    Printer< ::sensor_msgs::PointCloud2_<ContainerAllocator> >::stream(s, indent + "  ", v.cloud);
    s << indent << "min_point: ";
    s << std::endl;
    Printer< ::geometry_msgs::PointStamped_<ContainerAllocator> >::stream(s, indent + "  ", v.min_point);
    s << indent << "max_point: ";
    s << std::endl;
    Printer< ::geometry_msgs::PointStamped_<ContainerAllocator> >::stream(s, indent + "  ", v.max_point);
    s << indent << "avg_point: ";
    s << std::endl;
    Printer< ::geometry_msgs::PointStamped_<ContainerAllocator> >::stream(s, indent + "  ", v.avg_point);
    s << indent << "centroid_point: ";
    s << std::endl;
    Printer< ::geometry_msgs::PointStamped_<ContainerAllocator> >::stream(s, indent + "  ", v.centroid_point);
    s << indent << "estimated_angle: ";
    Printer<double>::stream(s, indent + "  ", v.estimated_angle);
    s << indent << "dimensions: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.dimensions);
    s << indent << "eigen_values: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.eigen_values);
    s << indent << "eigen_vectors[]" << std::endl;
    for (size_t i = 0; i < v.eigen_vectors.size(); ++i)
    {
      s << indent << "  eigen_vectors[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "    ", v.eigen_vectors[i]);
    }
    s << indent << "fpfh_descriptor: ";
    s << std::endl;
    Printer< ::std_msgs::Float32MultiArray_<ContainerAllocator> >::stream(s, indent + "  ", v.fpfh_descriptor);
    s << indent << "bounding_box: ";
    s << std::endl;
    Printer< ::jsk_recognition_msgs::BoundingBox_<ContainerAllocator> >::stream(s, indent + "  ", v.bounding_box);
    s << indent << "convex_hull: ";
    s << std::endl;
    Printer< ::geometry_msgs::PolygonStamped_<ContainerAllocator> >::stream(s, indent + "  ", v.convex_hull);
    s << indent << "indicator_state: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.indicator_state);
  }
};

} // namespace message_operations
} // namespace ros

#endif // AUTOWARE_MSGS_MESSAGE_CLOUDCLUSTER_H
