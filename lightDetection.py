# -*- coding:utf-8 -*-
import cv2
import time
import RobotApi
import picamera
from picamera.array import PiRGBArray
import datetime

def lightDetection(night):
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 32
        raw_capture = PiRGBArray(camera, size=(640, 480))
        time.sleep(1)
        for frame in camera.capture_continuous(raw_capture, format = "bgr", use_video_port=True):
            cnt = 0
            image = frame.array        
            imageHsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            H, S, V = cv2.split(imageHsv)
            for i in V:
                for j in i:
                    if j > 100:
                        cnt += 1
            print(cnt)
            now_h=datetime.datetime.now().strftime('%H')
            print(now_h)
            if cnt / (640.0 * 480.0) < 0.07:
                if not night:
                    RobotApi.ubtVoiceTTS(1, "主人，天黑啦，早点休息吧，晚安")
                    night = True
                    RobotApi.ubtSetRobotLED("button", "blue", "off")
                    break
            else:
                if night:
                    RobotApi.ubtVoiceTTS(1, "滴滴！滴滴！主人，现在已经"+now_h+"点了，该起床了")
                    RobotApi.ubtSetRobotLED("button", "blue", "breath")
                    night = False
                    break
            key = cv2.waitKey(1) & 0xFF
            raw_capture.truncate(0)
            if key == ord('q'):
                break

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
    lightDetection()

    # Disconnect
    RobotApi.ubtRobotDisconnect("SDK", "1", gIPAddr)
    RobotApi.ubtRobotDeinitialize()
