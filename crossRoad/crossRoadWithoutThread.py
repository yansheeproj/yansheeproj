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
def crossRoad():
    res = RobotApi.ubtSearchExtendSensor()
    infrared_sensor=RobotApi.UBTEDU_ROBOTINFRARED_SENSOR_T()
    while(True):
        color = dc.detectColor()
        print("get:" + color)
        if(color == 'green'):
            break
    while(True):
        ret = RobotApi.ubtReadSensorValue("infrared", infrared_sensor, 4)
        color = dc.detectColor()
        if ret!= 0:
            print("InfraredSensor Error!")
            break
        distance = infrared_sensor.iValue

        if(color == 'green' or color == 'yellow' or color == 'red'):
            print("distance: %d mm", distance)
            if(distance < 100):
                break
        else:
            while(True):
                ret = RobotApi.ubtReadSensorValue("infrared", infrared_sensor, 4)
                obstacle = infrared_sensor.iValue
                print("obstacle: %d mm", obstacle)
                if(obstacle > 300):
                    break


        RobotApi.ubtSetRobotMotion("walk", "front", 2, 1)

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
    #-----------Disconnect---------
    RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
    RobotApi.ubtRobotDeinitialize()
