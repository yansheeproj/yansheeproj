# -*- encoding:utf-8 -*-
import time
import RobotApi
import picamera
from picamera.array import PiRGBArray
import os
import cv2
import pyaudio, wave
import os, sys


def Monitor():
    face_detector = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    fps = 0
    time.sleep(1)
    raw_capture = picamera.array.PiRGBArray(camera, size=(640, 480))
    time.sleep(0.1)
    for frame in camera.capture_continuous(raw_capture, format = "bgr", use_video_port=True):
        image = frame.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            fps += 1

            cv2.imwrite("dataset/User." + str(fps) + ".jpg", gray[y:y+h, x:x+w])
            cv2.imshow('image', image)
        k = cv2.waitKey(100) & 0xff
        if k == 27:
            break
        elif fps >= 3:
            break
        raw_capture.truncate(0)
    camera.close()


def faceRecognition():
    # Face Detection
    num = "0"
    ret = RobotApi.ubtVisionDetect("face", num, 5)
    if int(num) != 0:
        name = "0"
        # Face Recognition
        ret = RobotApi.ubtFaceCompare(5, name)
        if name == "1" or name == '2' or name == '3':
            return true
        else:
            return False
    else:
        pass

if __name__ == '__main__': 
    # Init
    RobotApi.ubtRobotInitialize()
    gIPAddr = "127.0.0.1"
    # Connect
    ret = RobotApi.ubtRobotConnect("SDK", "1", gIPAddr)
    if (0 != ret):
        print("Can not connect to robot %s"%robotinfo.acName)
    	exit(1)
    # Do
    faceRecognition()
    # Disconnect
    RobotApi.ubtRobotDisconnect("SDK", "1", gIPAddr)
    RobotApi.ubtRobotDeinitialize()
