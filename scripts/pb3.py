#!/usr/bin/env python3
# license removed for brevity
import rospy
from exercise_three.msg import custom
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('/raw_data', String, queue_size=10)
	rospy.init_node('user_info_driver', anonymous=True)
	rate = rospy.Rate(1)
	message_to_publish = custom()
	while not rospy.is_shutdown():
  		message_to_publish.name = input("please enter the name:\n")
  		message_to_publish.age = input("Please enter age:\n")
  		message_to_publish.height = input("please enter the height:\n")
  		hello_str = "name: %s ,age: %d ,height: %d" % (message_to_publish.name,message_to_publish.age,message_to_publish.height)
  		rospy.loginfo(hello_str)
  		pub.publish(hello_str)
  		rate.sleep()
  
if __name__ == '__main__':
     try:
          talker()
     except rospy.ROSInterruptException:
         pass
