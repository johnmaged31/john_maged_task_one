#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
from exercise_three.msg import custom
   
def callback(data):
       x,name,y,age,z,height = data.data.split(' ')
       cage = int(age)
       cheight = int(height)
       cheight = cheight + 6
       rospy.loginfo("name is %s, age is %d, height is %d", name,cage,cheight)
       rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
       pub1 = rospy.Publisher('/user_info', custom, queue_size=10)
       msg_to_publish = custom()
       msg_to_publish.name = name
       msg_to_publish.age = cage
       msg_to_publish.height = cheight
       pub1.publish(msg_to_publish)
       
def listener():
   

       rospy.init_node('data_processing', anonymous=True)
   
       rospy.Subscriber("/raw_data", String, callback)
       

   
      # spin() simply keeps python from exiting until this node is stopped
       rospy.spin()
   
if __name__ == '__main__':
       listener()
