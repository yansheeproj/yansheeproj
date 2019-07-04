# -*- coding:utf-8 -*-
import pygame
import RobotApi
import time
import datetime
#pygame.mixer.init()
#pygame.mixer.music.load('/////Happy_Borthday')
#print(datetime.datetime.now())
def clock(year,month,date,hour,minu,sec, text):
    while True:
        time.sleep(1)
        now_y=datetime.datetime.now().strftime('%Y')
        now_m=datetime.datetime.now().strftime('%m')
        now_d=datetime.datetime.now().strftime('%d')
        now_h=datetime.datetime.now().strftime('%H')
        now_M=datetime.datetime.now().strftime('%M')
        now_s=datetime.datetime.now().strftime('%S')
        #print(datetime.datetime.now())
        #print(sec)
        #print(now_s)
        if year == now_y and month == now_m and date == now_d and  hour == now_h and minu == now_M and sec == now_s:
 #       pygame.mixer.music.play()
    #    time.sleep(60)
            RobotApi.ubtStartRobotAction("hand",1)
            RobotApi.ubtVoiceTTS(0, text)
#print("hahahahhhhhh")
            exit(1)
        #else:
            # print("No!")
#clock(str(input("Year:")),str(raw_input("Month:")),str(raw_input("Date:")),str(input("Hour:")),str(input("Min:")),str(raw_input("Sec:")))
if __name__ == '__main__':
    RobotApi.ubtRobotInitialize()
    gIPAddr="127.0.0.1"
    robotinfo=RobotApi.UBTEDU_ROBOTINFO_T()
    ret=RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
    if(0!=ret):
        print("can not connect to robot %s"%robotinfo.acName)
        exit(1)
    clock('2019','07','04','14','19','59', "起床啦")
    RobotApi.ubtRobotDisconnect("SDK","1",gIPAdrr)
    RobotApi.ubtRobotDeinitialize()

