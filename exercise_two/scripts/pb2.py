#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('/raw_data', String, queue_size=10)
	rospy.init_node('user_info_driver', anonymous=True)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
  		name = input("please enter the name:\n")
  		age = input("Please enter age:\n")
  		height = input("please enter the height:\n")
  		hello_str = "name: %s ,age: %s ,height: %s" % (name,age,height)
  		rospy.loginfo(hello_str)
  		pub.publish(hello_str)
  		rate.sleep()
  
if __name__ == '__main__':
     try:
          talker()
     except rospy.ROSInterruptException:
         pass
