#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
import time
import speech_recognition as sr
from datetime import datetime
import random



def SpeechToText(x):
    if x==1:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # print(source)
            print("start")
            # playsound("signal.mp3")
            audio = r.record(source, duration=5)  # บันทึกเสียง 5 วินาท
            # print(type(audio))# ี
            print("finish")

            # playsound("signal.mp3")
        # print(audio)
        try:
            text = r.recognize_google(audio, language = 'en')
            # print("None")
        except:
            text = "Try again please"
        return text
# this method will make the robot move to the goal location
def move_to_goal(xGoal, yGoal,angle):
    # define a client for to send goal requests to the move_base server through a SimpleActionClient
    ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

    # wait for the action server to come up
    while (not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
        rospy.loginfo("Waiting for the move_base action server to come up")

    goal = MoveBaseGoal()

    # set up the frame parameters
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # moving towards the goal*/

    goal.target_pose.pose.position = Point(xGoal, yGoal, 0)
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = angle
    goal.target_pose.pose.orientation.w = 1.0

    rospy.loginfo("Sending goal location ...")
    ac.send_goal(goal)

    ac.wait_for_result(rospy.Duration(120))

    if (ac.get_state() == GoalStatus.SUCCEEDED):
        rospy.loginfo("You have reached the destination")
        return True

    else:
        rospy.loginfo("The robot failed to reach the destination")
        return False


if __name__ == '__main__':
    rospy.init_node('map_navigation', anonymous=False)
    x_goal1 = -0.534
    y_goal1 = 3.788
    angle1 = 2.032
    x_goal2 = -0.037
    y_goal2 = 0.071
    angle2 = -0.264
    x_goalb2 = -2.052
    y_goalb2 = 2.754
    angleb2 = -1.292
    x_goal3 = 4.619
    y_goal3 = 0.901
    angle3 = 1.54
    x_goalb4 = -1.209
    y_goalb4 = 0.453
    angleb4 = -1.77
    x_goal4= -2.167
    y_goal4 = -4.06
    angle4 = 0.052
    x_goalbase = 0.845
    y_goalbase = 2.789
    anglebase = 3.134
    move_to_goal(x_goalbase, y_goalbase, anglebase)
    a = SpeechToText(1)
    print(a)

    if "1" in a or "one" in a :
        print('start go to goal')
        move_to_goal(x_goal1, y_goal1, angle1)
        print('Thank you')
        time.sleep(5)
        move_to_goal(x_goalbase, y_goalbase, anglebase)
        print('base')
        time.sleep(5)

    if "2" in a or "two" in a :
        print('start go to goal')
        # move_to_goal(x_goalb2, y_goalb2, angleb2)
        move_to_goal(x_goal2, y_goal2, angle2)
        print('two')
        time.sleep(5)
        move_to_goal(x_goalb2, y_goalb2, angleb2)
        move_to_goal(x_goalbase, y_goalbase, anglebase)
        print('base')
        time.sleep(5)
    if "3" in a or "three" in a :
        print('start go to goal')
        move_to_goal(x_goalb2, y_goalb2, angleb2)
        move_to_goal(x_goal2, y_goal2, angle2)
        move_to_goal(x_goal3, y_goal3, angle3)
        print('three')
        time.sleep(5)
        move_to_goal(x_goal2, y_goal2, angle2)
        move_to_goal(x_goalb2, y_goalb2, angleb2)
        move_to_goal(x_goalbase, y_goalbase, anglebase)
        print('base')
        time.sleep(5)
    if "4" in a or "four" in a :
        print('start go to goal')
        move_to_goal(x_goalb2, y_goalb2, angleb2)
        move_to_goal(x_goalb4, y_goalb4, angleb4)
        move_to_goal(x_goal4, y_goal4, angle4)
        print('four')
        time.sleep(5)
        move_to_goal(x_goalb4, y_goalb4, angleb4)
        move_to_goal(x_goalb2, y_goalb2, angleb2)
        move_to_goal(x_goalbase, y_goalbase, anglebase)
        print('base')
        time.sleep(5)
    else :
        move_to_goal(x_goalbase, y_goalbase, anglebase)
        print('base')
    # move_to_goal(x_goal2, y_goal2, angle2)
    # print('two')
    # time.sleep(5)
    # move_to_goal(x_goal3, y_goal3, angle3)
    # print('three')
    # time.sleep(5)
    #
    #
    # move_to_goal(x_goal4, y_goal4, angle4)
    # print('four')
    # time.sleep(5)
    # move_to_goal(x_goalbase, y_goalbase, anglebase)
    # print('base')

    rospy.spin()


