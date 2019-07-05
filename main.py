# -*- coding: utf-8 -*-
import time
import RobotApi
import thread
import Monitor
import mood
from picamera.array import PiRGBArray 
from picamera import PiCamera
from client import send_op
from dance import dance
from dialog import gen_token

RobotApi.ubtRobotInitialize()
#--------Connect--------------
gIPAddr="127.0.0.1"
robotinfo=RobotApi.UBTEDU_ROBOTINFO_T()
ret=RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
if(0!=ret):
    print("can not connect to robot %s"%robotinfo.acName)
    exit(1)


#-------Test------------
A_ip = "192.168.43.215"
B_ip = "192.168.43.117"
C_ip = "192.168.43.134"

op = ""
print("options: morning, crossRoad, Monitor, chat, mood")
op = str(raw_input("please enter op: "))
while op != "exit":
    if op == "morning":
        send_op(op, C_ip)
    elif op == "crossRoad":
        send_op(op, B_ip)
    elif op == "Monitor":
        det = Monitor.faceRecognition()
        if det == False:
            send_op("alter", B_ip)
    elif op == "chat":
        utterance = raw_input("utterance: ")
        token = gen_token()
        while utterance != "exit":
            data = "chat " + utterance + " token"
            send_op(data, C_ip)
            utterance = raw_input("utterance: ")
    elif op == "mood":
        cur_mood = mood.mood_judge()
        if  mood_judge() == "Sad":
            RobotApi.ubtVoiceTTS(0,"主人别伤心辣，我给你跳支舞吧")
            send_op(op, B_ip)
            send_op(op, C_ip)
            dance()
        else:
            print("你看起来一点儿也不悲伤呀~")
    else:
        print("invalid options!")
    print("options: morning, crossRoad, Monitor, chat, mood")
    op = str(raw_input("please enter op: "))

#-----------Disconnect---------
RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
RobotApi.ubtRobotDeinitialize()
