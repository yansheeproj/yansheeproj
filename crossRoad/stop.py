import time
import RobotApi
RobotApi.ubtRobotInitialize()

gIPAddr = "127.0.0.1"
robotinfo = RobotApi.UBTEDU_ROBOTINFO_T()
ret = RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
if(0!=ret):
    print("Can not connect to reobot %s" % robotinfo.acName)
    exit(1)
RobotApi.ubtStopRobotAction()

RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
RobotApi.ubtRobotDeinitialize()
