#! /usr/bin/env python

from operator import le
import sys
#import imp
import os
from tkinter import N
import turtle
#from typing_extensions import Self
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import std_msgs
from math import sqrt
#from typing_extensions import Self


def my_atoi(string):
    res = 0

    for i in range(len(string)):
        res = res * 10 + (ord(string[i]) - ord('0'))
    return res

def talker():
    rospy.init_node('turtlesim',anonymous=True)
    #rospy.init_node('draw_triangle',anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    sbc = rospy.Subscriber('/turtle1/pose',Pose)
    turtle_speed = 2.0
    #turtle_speed = rospy.get_param('/turtle1/turtle_speed')
    #turtle_speed = rospy.get_param('speed/',)
    print ("turtle speed:")
    print(turtle_speed)
    print('\n')
    rate = rospy.Rate(10)
    vel = Twist()

    dir = -1
    #len = float(input("uzunluk gir"))
    ctr = 0

    strr = str(input("q to quit or Set lenght: "))
    while strr != 'q':
        len = my_atoi(strr)
        #print(len)
        while (dir < 2):
            print("girdi dir :")
            print(dir)
            #posing = Pose()

            vel.linear.z = 0
            vel.angular.x = 0 
            vel.angular.y = 0 
            vel.angular.z = 0 
            if(dir == -1):
                posing = Pose()
                vel.linear.x = (len/2.0)
                vel.linear.y = float((-len * ((sqrt(3))/2)).real)
                print("\n now loc x = ")
                print(posing.x)
                print("\n hedef loc x = ")
                print(posing.x + len/2)
                print("\n now loc y = ")
                print(posing.y)
                print("\n hedef loc y = ")
                print(posing.y - len * ((sqrt(3))/2).real)
#                vel.angular.z = 2.09
            if(dir == 0):
                posing = Pose()
                vel.linear.x = float(-len)
                vel.linear.y = 0
#                vel.angular.z = 2.09
                print("\n now loc x = ")
                print(posing.x)
                print("\n hedef loc x = ")
                print(posing.x + len/2)
                print("\n now loc y = ")
                print(posing.y)
                print("\n hedef loc y = ")
                print(posing.y - len * ((sqrt(3))/2).real)
            if(dir == 1):
                posing = Pose()
                vel.linear.x = (len/2.0)
                vel.linear.y = float((len * ((sqrt(3))/2)).real  )
#                vel.angular.z = 2.09
                print("\n now loc x = ")
                print(posing.x)
                print("\n hedef loc x = ")
                print(posing.x + len/2)
                print("\n now loc y = ")
                print(posing.y)
                print("\n hedef loc y = ")
                print(posing.y - len * ((sqrt(3))/2).real)
            dir = dir + 1
#            if(dir == 2):
                #dir = -1
#                ctr = 1
            pub.publish(vel)
            rate.sleep()
        strr = str(input("q to quit or Set lenght:"))
        if (strr != 'q'):
            dir = -1
        # vel.linear.x = 0
        # vel.linear.y = 0
        # if(dir == -1):
        #     vel.angular.z=2.09
        # if(dir == 0):
        #     vel.angular.z=2.09
        # if(dir == 1):
        #     vel.angular.z=2.09
        # pub.publish(vel)
        # rate.sleep()

if __name__ == '__main__':
    try:
        talker()
        #talker(float(sys.argv[1]))
    except rospy.ROSInterruptException:
        pass
