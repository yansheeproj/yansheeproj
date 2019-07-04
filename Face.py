#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import picamera
import time
import RobotApi

# Init
RobotApi.ubtRobotInitialize()
gIPAddr = "127.0.0.1"

# Connect
ret = RobotApi.ubtRobotConnect("SDK", "1", gIPAddr)
if (0 != ret):
	print("Can not connect to robot %s"%robotinfo.acName)
	exit(1)

# numbers
num = "0"
RobotApi.ubtVisionDetect("face", num, 5)
time.sleep(0.5)
print(num)
# TakeAPhoto
ss = "0"
ret = RobotApi.ubtFaceCompare(10, ss)
print(ss)
# Expression
ss2 = RobotApi.UBTEDU_FACEEXPRE_T()
RobotApi.ubtFaceExpression(5, ss2)
max0 = max(ss2.fHappinessValue, ss2.fSurpriseValue, ss2.fAngerValue, ss2.fSadnessValue, ss2.fNeutralValue, ss2.fDisgustValue, ss2.fFearValue)
result=0
if max0==ss2.fHappinessValue:
	result="fHappinessValue"
if max0==ss2.fSurpriseValue:
	result="fSurpriseValue"
if max0==ss2.fAngerValue:
	result="fAngerValue"
if max0==ss2.fSadnessValue:
	result="fSadnessValue"
if max0==ss2.fNeutralValue:
	result="fNeutralValue"
if max0==ss2.fDisgustValue:
	result="fDisgustValue"
if max0==ss2.fFearValue:
	result="fFearValue"
print(result)
# Gender And Age
gender = "0"
age = "0"
ret = RobotApi.ubtFaceAgeGender(5, gender, age)
print(gender, age)


# Disconnect
RobotApi.ubtRobotDisconnect("SDK", "1", gIPAddr)
RobotApi.ubtRobotDeinitialize()
