#-*- coding: UTF-8 -*-
import time
import RobotApi as RA
import argparse
from subprocess import call
import datetime
import pygame


def dance():
    pygame.mixer.init()
    pygame.mixer.music.load(r"/mnt/1xrobot/res/hts/haicaowu.mp3")
    pygame.mixer.music.play(0,0)
    RA.ubtSetRobotVolume(60)

    ret = RA.ubtStartRobotAction("dance",0)

    time.sleep(35)

    RA.ubtStopRobotAction()





                                        

