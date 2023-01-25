#include "ros/ros.h"

/*  
    ROS 节点:输出各种级别的日志信息
*/

int main(int argc, char *argv[])
{
    ros::init(argc,argv,"rqt_log");
    ros::NodeHandle nh;

    ros::Rate rate(0.3);
    while (ros::ok())
    {
        ROS_DEBUG("Debug message d");
        ROS_INFO("Info message oooooooooooooo");
        ROS_WARN("Warn message wwwww");
        ROS_ERROR("Error message EEEEEEEEEEEEEEEEEEEE");
        ROS_FATAL("Fatal message FFFFFFFFFFFFFFFFFFFFFFFFFFFFF");
        rate.sleep();
    }

    return 0;
}
