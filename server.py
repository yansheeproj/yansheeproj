# -*- coding: utf-8 -*-
import socket
import thread
import time
import RobotApi
import threading
import clock
import env
import re
from dialog import response
import lightDetection as ld
#from crossRoad import crossRoadWithoutThread as cr

RobotApi.ubtRobotInitialize()
#--------Connect--------------
gIPAddr="127.0.0.1"
robotinfo=RobotApi.UBTEDU_ROBOTINFO_T()
ret=RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
if(0!=ret):
    print("can not connect to robot %s"%robotinfo.acName)
    exit(1)

# create
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# listen
s.bind(('0.0.0.0',9999))
s.listen(5)
print('Waiting for connection...')
over = False

def tcplink(sock,addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data=sock.recv(1024)
        print(data)
        sock.send("accept op success")
        if data=='exit' or not data:
            break
        elif data == "alert":
            RA.ubtVoiceTTS("主人主人，有陌生人正在我们家门口转悠！")
        elif data == "dance":
            dance()
        elif data == "crossRoad":
            cr.crossRoad()
        elif re.match('chat', data) != None:
            l = data.split(" ")
            utterance = l[1]
            RobotApi.ubtVoiceTTS(0, utterance)
            token = l[2]
            res = response(utterance, token)
            RobotApi.ubtVoiceTTS(0, res)
        elif data == "morning":
            ld.lightDetection()
            env.getTempAndHumi()
            time = str(raw_input("请输入时间（yy mm dd hh mm ss）："))
            time = time.split(' ')
            text = str(raw_input("请输入日程："))
            text = "主人，要" + text + "啦"
            thread.start_new_thread(clock.clock, (time[0], time[1], time[2], time[3], time[4], time[5], text))
        else:
            pass
    sock.close()
    print 'Connection from %s:%s closed.'%addr
    over = True
    
while not over:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink(sock,addr))
    
#-----------Disconnect---------
RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
RobotApi.ubtRobotDeinitialize()
