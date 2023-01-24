#!/usr/bin/env python3

"""
    需求:写出消息数据到磁盘上的bag文件
    流程:
        1.导包:
        2.初始化;
        3.创建 rosbag 对象并且打开文件流; 
        4.写数据;
        5.关闭文件流.
"""
import rospy
import rosbag
from std_msgs.msg import String

if __name__ == "__main__":

    # 2.初始化;
    rospy.init_node("bags_write_p")
    # 3.创建 rosbag 对象并且打开文件流;
    bag = rosbag.Bag("hello_p.bag",'w',)
    # 4.写数据;
    msg = String()
    msg.data = "hello_p bag"
    bag.write("chat",msg)
    bag.write("chat",msg)
    bag.write("chat",msg)
    bag.write("chat",msg)
    bag.write("chat",msg)
    bag.write("chat",msg)

    # 5.关闭文件流.
    bag.close()