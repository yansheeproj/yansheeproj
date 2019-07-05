#-*- coding:UTF-8 -*-
import time
import RobotApi
import dance#-*- coding: UTF-8 -*-
import argparse
from subprocess import call
import datetime
import pygame


def dance():
    pygame.mixer.init()
    pygame.mixer.music.load(r"/mnt/1xrobot/res/hts/haicaowu.mp3")
    pygame.mixer.music.play(0,0)
    RobotApi.ubtSetRobotVolume(60)

    ret = RobotApi.ubtStartRobotAction("dance",0)

    time.sleep(35)

    RobotApi.ubtStopRobotAction()


def mood_judge():
    res = RobotApi.UBTEDU_FACEEXPRE_T()
    net = RobotApi.ubtFaceExpression(10,res)
    if(net!=0):
        print("Fail!")
    list_name=['Happy','Surprise','Anger','Sad','Neutral','Disgust','Fear']
    list_num=[res.fHappinessValue,res.fSurpriseValue,res.fAngerValue,res.fSadnessValue,res.fNeutralValue,res.fDisgustValue,res.fFearValue]
    return list_name[list_num.index(max(list_num))]
def mood():
    m = mood_judge()
    if  m == "Happy":
        RobotApi.ubtVoiceTTS(0,"儿子你看起来很开心给你爹跳支舞吧算了还是我跳吧")
        time.sleep(4)
    if  m == "Sad":
        RobotApi.ubtVoiceTTS(0,"别伤心了我老给你跳支舞吧")
        time.sleep(2)
    if  m == "Disgust":
        RobotApi.ubtVoiceTTS(0," my son you look so Disgust why do not show a dance to your father Lei")
        time.sleep(4)
    if  m == "Fear":
        RobotApi.ubtVoiceTTS(0,"你看起来特别害怕 是不是你雷爸爸又揍你了没事我来跳支舞安慰一下啊你")
        time.sleep(5)
    dance.dance()
