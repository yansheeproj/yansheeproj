#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import time
from picamera.array import PiRGBArray 
from picamera import PiCamera
import numpy as np
import cv2
import RobotApi
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

