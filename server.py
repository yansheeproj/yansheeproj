# -*- coding:utf-8 -*-
import socket
import RobotApi
import time
from dance import dance

def server():
    RobotApi.ubtRobotInitialize()
    #--------Connect--------------
    gIPAddr="127.0.0.1"
    robotinfo=RobotApi.UBTEDU_ROBOTINFO_T()
    ret=RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
    if(0!=ret):
        print("can not connect to robot %s"%robotinfo.acName)
        exit(1)
    #-------Test------------
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = ("0.0.0.0", 8888)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(server_addr)
    data, client_addr = s.recvfrom(1000) # wait until someone sends something to me
    print(data)
    alert_mode = True
    if data == "alert" and alert_mode == True:
        ret = RobotApi.ubtVoiceTTS(0, "主人主人，有一个鬼鬼祟祟的人在靠近我们家！")
    if data == "dance":
        dance()
    s.close()
    #-----------Disconnect---------
    RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
    RobotApi.ubtRobotDeinitialize()
