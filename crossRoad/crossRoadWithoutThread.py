#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import time
from picamera.array import PiRGBArray 
from picamera import PiCamera
import numpy as np
import cv2
import RobotApi
import detectColor as dc
import onefoot
def crossRoad():
   #take photo use piCamera
    res = RobotApi.ubtSearchExtendSensor()
    infrared_sensor=RobotApi.UBTEDU_ROBOTINFRARED_SENSOR_T()
    while(True):
        color = dc.detectColor()
        print("get:" + color)
        if(color == 'green'):
            RobotApi.ubtVoiceTTS(0, "绿灯了，主人，我们走吧")
            break
    while(True):
        hurry = False
        ret = RobotApi.ubtReadSensorValue("infrared", infrared_sensor, 4)
        color = dc.detectColor()
        if ret!= 0:
            print("InfraredSensor Error!")
            break
        distance = infrared_sensor.iValue

        if(color == 'green' or color == 'yellow' or color == 'red'):
            print("distance: %d mm", distance)
            if(distance < 100):
                RobotApi.ubtVoiceTTS(0, "我们到了，主人")
                RobotApi.ubtSetRobotMotion("wave", "left", 2, 1)
                onefoot.onefoot()
                break
            elif(color == 'yellow'):
                RobotApi.ubtVoiceTTS(0, "黄灯了，我们快一点，小心")
                hurry = True
            elif(color == 'red'):
                RobotApi.ubtVoiceTTS(0, "红灯了，我们快一点，小心")
                hurry = True

        else:
            flag = False
            while(True):
                ret = RobotApi.ubtReadSensorValue("infrared", infrared_sensor, 4)
                obstacle = infrared_sensor.iValue
                print("obstacle: %d mm", obstacle)
                if(obstacle > 300):
                    if(flag):
                        RobotApi.ubtVoiceTTS(0, "我们继续走吧")
                    flag = False
                    print("obstacle > 300")
                    break
                if not flag:
                    RobotApi.ubtVoiceTTS(0, "有车辆经过，我们等一下")
                    flag = True
                #cnt += 1
                #print(cnt)
        print(hurry)
        if(hurry):
            speed = 3
        else:
            speed = 2
        RobotApi.ubtSetRobotMotion("walk", "front", speed, 1)

    
if __name__ == '__main__':
    RobotApi.ubtRobotInitialize()
    #--------Connect--------------
    gIPAddr="127.0.0.1"
    robotinfo=RobotApi.UBTEDU_ROBOTINFO_T()
    ret=RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
    if(0!=ret):
        print("can not connect to robot %s"%robotinfo.acName)
        exit(1)
    #-------Test------------
    crossRoad()
    #print(cnt)
    #-----------Disconnect---------
    RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
    RobotApi.ubtRobotDeinitialize()
