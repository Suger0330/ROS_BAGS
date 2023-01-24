#!/usr/bin/env python3

"""
    需求:读出磁盘上的bag文件的消息
    流程:
        1.导包:
        2.初始化;
        3.创建 rosbag 对象并且打开文件流; 
        4.读数据;
        5.关闭文件流.
"""
import rospy
import rosbag
from std_msgs.msg import String

if __name__ == "__main__":

    # 2.初始化;
    rospy.init_node("bags_read_p")
    # 3.创建 rosbag 对象并且打开文件流;
    bag = rosbag.Bag("hello_p.bag",'r')
    # 4.读数据;
    msgs = bag.read_messages("chat")
    for topic,msg,time in msgs:
        rospy.loginfo("话题:%s,消息:%s,时间:%s",topic,msg,time)
    # 5.关闭文件流.
    bag.close()