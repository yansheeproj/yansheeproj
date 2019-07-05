import time
import RobotApi
import picamera
RobotApi.ubtRobotInitialize()
#camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
fps = 0
time.sleep(1)
raw_capture = picamera.array.PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
#--------Connect--------------
gIPAddr="127.0.0.1"
robotinfo=RobotApi.UBTEDU_ROBOTINFO_T()
ret=RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
if(0!=ret):
    print("can not connect to robot %s"%robotinfo.acName)
    exit(1)
#-------Test------------
#-----------Disconnect---------
RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
RobotApi.ubtRobotDeinitialize()
