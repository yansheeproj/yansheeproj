#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import time
from picamera.array import PiRGBArray 
from picamera import PiCamera
import numpy as np
import cv2
import RobotApi
import thread
# define HSV color value
red_min = np.array([0, 128, 46]) 
red_max = np.array([5, 255, 255]) 
red2_min = np.array([156, 128, 46]) 
red2_max = np.array([180, 255, 255])

green_min = np.array([35, 128, 46]) 
green_max = np.array([77, 255, 255])
blue_min = np.array([100, 128, 46]) 
blue_max = np.array([124, 255, 255])
yellow_min = np.array([15, 128, 46]) 
yellow_max = np.array([34, 255, 255])

black_min = np.array([0, 0, 0]) 
black_max = np.array([180, 255, 10])
white_min = np.array([0, 0, 70]) 
white_max = np.array([180, 30, 255])
COLOR_ARRAY = [ [ red_min, red_max, 'red'], [ red2_min, red2_max, 'red'], [ green_min, green_max, 'green'], [ blue_min, blue_max, 'blue'],[yellow_min, yellow_max, 'yellow'] ]
#take photo use piCamera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25
rawCapture = PiRGBArray(camera, size=(640, 480)) 
time.sleep(0.1)
global color
color = "red"
def detectColor():
    #read rgb_jpg file for test
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        frame = frame.array
        cv2.imwrite("frame.jpg", frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
        cv2.imwrite("hsv.jpg", hsv)
        for (color_min, color_max, name) in COLOR_ARRAY: 
            mask=cv2.inRange(hsv, color_min, color_max) 
            res=cv2.bitwise_and(frame, frame, mask=mask) #cv2.imshow("res",res)
            cv2.imwrite("2.jpg", res) 
            img = cv2.imread("2.jpg")
            h, w = img.shape[:2]
            blured = cv2.blur(img,(5,5))
            cv2.imwrite("blured.jpg", blured)
            ret, bright = cv2.threshold(blured,10,255,cv2.THRESH_BINARY) 
            gray = cv2.cvtColor(bright,cv2.COLOR_BGR2GRAY) 
            cv2.imwrite("gray.jpg", gray)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50)) 
            opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
            cv2.imwrite("opened.jpg", opened)
            closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel) #cv2.imshow("closed", closed)
            cv2.imwrite("closed.jpg", closed)
            contours, hierarchy =cv2.findContours(closed,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE) 
            cv2.drawContours(img,contours,-1,(0,0,255),3) 
            cv2.imwrite("result.jpg", img )
            #output number and color we find in the photo
            number = len(contours)
            if number >=1:
                print(2)
                total = 0
                for i in range(0, number):
                    total = total + len(contours[i])
                if total > 400:
                    print 'Currrent color is ', name 
                    cv2.destroyAllWindows()
                    rawCapture.truncate(0)
                    return name
        rawCapture.truncate(0)
    return name
def forward(threadName):
    global color
    flag = False
    while(1):
        print(flag)
        if(flag):
            break
        time.sleep(1)
        print(threadName)
        res = RobotApi.ubtSearchExtendSensor()
        infrared_sensor=RobotApi.UBTEDU_ROBOTINFRARED_SENSOR_T()
        while(True):
            time.sleep(1)
            #color = detectColor()
            print("get:" + color)
            if(color == 'green'):
                break

        while(True):
            time.sleep(1)
            ret = RobotApi.ubtReadSensorValue("infrared", infrared_sensor, 4)
            #color = detectColor()
            #print("In distance:"+color)
            if ret!= 0:
                print("InfraredSensor Error!")
                break
            distance = infrared_sensor.iValue

            if(color == 'green' or color == 'yellow' or color == 'red'):
                print("distance: %d mm", distance)
                if(distance < 100):
                    print("distance < 100...")
                    flag = True
                    break
            else:
                while(True):
                    time.sleep(1)
                    ret = RobotApi.ubtReadSensorValue("infrared", infrared_sensor, 4)
                    obstacle = infrared_sensor.iValue
                    print("obstacle: %d mm", obstacle)
                    if(obstacle > 300):
                        print("distance > 300:")
                        break
            print("going")
            RobotApi.ubtSetRobotMotion("walk", "front", 1, 1)

def detect(threadName):
    global color
    while(1):
        print(threadName)
        color = detectColor()
    print("over")

def crossRoad():
    try:
        print("start")
        thread.start_new_thread(forward, ("---------------------------------------", ))
        thread.start_new_thread(detect, ("*********************************", ))
    except:
        print("Thread Error!")
    time.sleep(200)
    #while(1):
       # pass

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
