#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
   
def callback(data):
       x,name,y,age,z,height = data.data.split(' ')
       cage = int(age)
       cheight = int(height)
       cheight = cheight + 6
       rospy.loginfo("name is %s, age is %d, height is %d", name,cage,cheight)
       rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
       pub1.publish(name)
       pub2.publish(age)
       pub3.publish(height)
       
def listener():
   

       rospy.init_node('data_processing', anonymous=True)
   
       rospy.Subscriber("/raw_data", String, callback)
       
       pub1 = rospy.Publisher('/name', string, queue_size=10)
       pub2 = rospy.publisher('/age', int, queue_size=10)
       pub3 = rospy.publisher('/height', int, queue_size=10)
   
      # spin() simply keeps python from exiting until this node is stopped
       rospy.spin()
   
if __name__ == '__main__':
       listener()
