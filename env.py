# -*- coding: utf-8 -*-
import time
import RobotApi
def getTempAndHumi():
    res = RobotApi.ubtSearchExtendSensor()
    sensorValue = RobotApi.UBTEDU_ROBOTENV_SENSOR_T()   
    ret=-1
    ret=RobotApi.ubtReadSensorValue("environment",sensorValue,12)        
    if(ret!=0):
        print("read sensor error!\n")
        #time.sleep(1)
        # RobotApi.ubtSearchExtendSensor()
    else:   
        print("TemValue:%d\n"%sensorValue.iTempValue)
        print("HumValue:%d\n"%sensorValue.iHumiValue)
        print("PresValue:%d\n"%sensorValue.iPresValue)
        RobotApi.ubtVoiceTTS(0,"温度 %d"%sensorValue.iTempValue)
        RobotApi.ubtVoiceTTS(0,"湿度 %d"%sensorValue.iHumiValue)
        RobotApi.ubtVoiceTTS(0,"压强 %d"%sensorValue.iPresValue)

if __name__ == '__main__':
    RobotApi.ubtRobotInitialize()
    #--------Connect--------------
    gIPAddr="127.0.0.1"
    robotinfo=RobotApi.UBTEDU_ROBOTINFO_T()
    ret=RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
    if(0!=ret):
        print("can not connect to robot %s"%robotinfo.acName)
        exit(1)
    # Test
    getTempAndHumi()
    #-----------Disconnect---------
    RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
    RobotApi.ubtRobotDeinitialize()

