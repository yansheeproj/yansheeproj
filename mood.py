#-*- coding:UTF-8 -*-
import time
import RobotApi
import dance
def mood_judge():
    res = RobotApi.UBTEDU_FACEEXPRE_T()
    net = RobotApi.ubtFaceExpression(10,res)
    if(net!=0):
        print("Fail!")
    list_name=['Happy','Surprise','Anger','Sad','Neutral','Disgust','Fear']
    list_num=[res.fHappinessValue,res.fSurpriseValue,res.fAngerValue,res.fSadnessValue,res.fNeutralValue,res.fDisgustValue,res.fFearValue]
    return list_name[list_num.index(max(list_num))]

if __name__ == '__main__':
    RobotApi.ubtRobotInitialize()
    #--------Connect--------------
    gIPAddr="127.0.0.1"
    robotinfo=RobotApi.UBTEDU_ROBOTINFO_T()
    ret=RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
    if(0!=ret):
        print("can not connect to robot %s"%robotinfo.acName)
        exit(1)
    #-------Test-----------:
    print(mood_judge)


    if  mood_judge() == "Happy":
        RobotApi.ubtVoiceTTS(0,"儿子你看起来很开心给你爹跳支舞吧算了还是我跳吧")
        time.sleep(4)
    if  mood_judge() == "Sad":
        RobotApi.ubtVoiceTTS(0,"别伤心了我老给你跳支舞吧")
        time.sleep(2)
    
    if  mood_judge() == "Disgust":
        RobotApi.ubtVoiceTTS(0," my son you look so Disgust why do not show a dance to your father Lei")
        time.sleep(4)
    if  mood_judge() == "Fear":
        RobotApi.ubtVoiceTTS(0,"你看起来特别害怕 是不是你雷爸爸又揍你了没事我来跳支舞安慰一下啊你")
        time.sleep(5)
    dance.dance()
    #-----------Disconnect---------
    RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
    RobotApi.ubtRobotDeinitialize()
