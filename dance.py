#-*- coding: UTF-8 -*-
import RobotApi
import pygame


def dance():
    pygame.mixer.init()
    pygame.mixer.music.load(r"/mnt/1xrobot/res/hts/haicaowu.mp3")
    pygame.mixer.music.play(0,0)
    RobotApi.ubtSetRobotVolume(60)

    ret = RobotApi.ubtStartRobotAction("dance",0)

    time.sleep(35)

    RobotApi.ubtStopRobotAction()