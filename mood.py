#-*- coding:UTF-8 -*-
import time
import argparse
from subprocess import call
import datetime
import pygame



def mood_judge():
    res = RobotApi.UBTEDU_FACEEXPRE_T()
    net = RobotApi.ubtFaceExpression(10,res)
    if(net!=0):
        print("Fail!")
    list_name=['Happy','Surprise','Anger','Sad','Neutral','Disgust','Fear']
    list_num=[res.fHappinessValue,res.fSurpriseValue,res.fAngerValue,res.fSadnessValue,res.fNeutralValue,res.fDisgustValue,res.fFearValue]
    return list_name[list_num.index(max(list_num))]
