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
RobotApi.ubtRobotInitialize()
#--------Connect--------------
gIPAddr="127.0.0.1"
robotinfo=RobotApi.UBTEDU_ROBOTINFO_T()
ret=RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
if(0!=ret):
    print("can not connect to robot %s"%robotinfo.acName)
    exit(1)
#-------Test------------
# morning
# 光线检测+报时起床
# ...
# 报温度和湿度
#env.getTempAndHumi()
## 添加日程
#time = str(raw_input("请输入时间（yy mm dd hh mm ss）："))
#time = time.split(' ')
#text = str(raw_input("请输入时间日程："))
#text = "主人，要" + text + "啦"
#thread.start_new_thread(clock.clock, (time[0], time[1], time[2], time[3], time[4], time[5], text))
# noon
#cr.crossRoad()
# afternoon
#Monitor.faceRecognition()
# night
mood.mood()
#dialog.dialog()
#while(1):
#    pass
#-----------Disconnect---------
RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
RobotApi.ubtRobotDeinitialize()
