# -*- coding: utf-8 -*-
import time
import RobotApi
import env
import clock
import thread
from crossRoad import crossRoadWithoutThread as cr
import dialog
import Monitor
import mood
import lightDetection as ld
from picamera.array import PiRGBArray 
from picamera import PiCamera
RobotApi.ubtRobotInitialize()
#--------Connect--------------
gIPAddr="127.0.0.1"
robotinfo=RobotApi.UBTEDU_ROBOTINFO_T()
ret=RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
if(0!=ret):
    print("can not connect to robot %s"%robotinfo.acName)
    exit(1)


#-------Test------------
while(True):
    print("我有四个小秘密，你选哪一个？")
    print("1 早晨\n2 中午\n3 下午\n4 晚上")
    option = input()
    if(option == 1):
        ld.lightDetection()
        env.getTempAndHumi()
        time = str(raw_input("请输入时间（yy mm dd hh mm ss）："))
        time = time.split(' ')
        text = str(raw_input("请输入日程："))
        text = "主人，要" + text + "啦"
        thread.start_new_thread(clock.clock, (time[0], time[1], time[2], time[3], time[4], time[5], text))
    elif(option == 2):
        cr.crossRoad()
    elif(option == 3):
        Monitor.faceRecognition()
    elif(option == 4):
        mood.mood()
        dialog.dialog()
    else:
        print("我没有那么多小秘密了~只有4个哦！")

# morning
# 光线检测+报时起床
# ...
# 报温度和湿度

## 添加日程
#cr.crossRoad()
# afternoon
#Monitor.faceRecognition()
# night
#dialog.dialog()
#while(1):
#    pass
#-----------Disconnect---------
RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
RobotApi.ubtRobotDeinitialize()
