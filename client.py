import socket
import sys
stdi, stdo, stde=sys.stdin, sys.stdout, sys.stderr
reload(sys)
sys.stdin, sys.stdout, sys.stderr=stdi, stdo, stde
sys.setdefaultencoding('utf-8')
import time
import pygame
import RobotApi

def dance():
    pygame.mixer.init()
    pygame.mixer.music.load(r"/mnt/1xrobot/res/hts/haicaowu.mp3")
    pygame.mixer.music.play(0,0)
    RobotApi.ubtSetRobotVolume(60)

    ret = RobotApi.ubtStartRobotAction("dance",0)
    time.sleep(3)
    RobotApi.ubtStopRobotAction()



def client(data):
    RobotApi.ubtRobotInitialize()
    gIPAddr = "127.0.0.1"
    robotinfo = RobotApi.UBTEDU_ROBOTINFO_T()
    ret = RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
    if(0!=ret):
        print("Can not connect to reobot %s" % robotinfo.acName);
        exit(1)
    
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    server_1 = ('192.168.43.134', 8888)
    server_2 = ('192.168.43.215', 8888)
    client.sendto(data,server_1)
    client.sendto(data,server_2)
    
    print("client send success.")
    if data == "dance":
        dance()
    
    client.close()
    RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
    RobotApi.ubtRobotDeinitialize()

if __name__ == "__main__":
    client("alert")
