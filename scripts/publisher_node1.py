#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node("publisher_node1", anonymous=True)

pub = rospy.Publisher('msgs_from_node1', String, queue_size = 10)
rospy.loginfo("Publisher Node 1 started , now publishing messages")

def talk_to_node2():
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            msg = raw_input("Enter your message: ")
            pub.publish(msg)
            rate.sleep()

        except rospy.ROSInterruptException:
            pass

def callback(data):
    print("\nMessage from node 2: " + data.data)

rospy.Subscriber("msgs_from_node2", String, callback)

if __name__ == "__main__":
    talk_to_node2()