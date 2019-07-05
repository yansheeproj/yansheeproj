import time
import RobotApi

def onefoot():
    servoinfo = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoinfo.SERVO17_ANGLE = 60
    
    #x = input()
    #servoinfo.SERVO5_ANGLE = 40
    
    #s={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
    #x = input()
    servoinfo.SERVO7_ANGLE = 85
    servoinfo.SERVO12_ANGLE = 95
    servoinfo.SERVO11_ANGLE = 75
    servoinfo.SERVO16_ANGLE = 100
    ret = RobotApi.ubtSetRobotServo(servoinfo,5)
    time.sleep(1)
    
    servoinfo.SERVO1_ANGLE = 1
    servoinfo.SERVO2_ANGLE = 179
    servoinfo.SERVO3_ANGLE = 179
    servoinfo.SERVO4_ANGLE = 0
    servoinfo.SERVO5_ANGLE = 91
    servoinfo.SERVO6_ANGLE = 91
    servoinfo.SERVO8_ANGLE = 0
    servoinfo.SERVO9_ANGLE = 0
    servoinfo.SERVO10_ANGLE = 0
    #servoinfo.SERVO12_ANGLE = 0
    servoinfo.SERVO13_ANGLE = 160#max = 160
    servoinfo.SERVO14_ANGLE = 90
    servoinfo.SERVO15_ANGLE = 110
    servoinfo.SERVO16_ANGLE = 0
    servoinfo.SERVO17_ANGLE = 140
    
    servoinfo.SERVO11_ANGLE = 75# max = 80
    servoinfo.SERVO7_ANGLE = 80#max = 110
    
    ret = RobotApi.ubtSetRobotServo(servoinfo,5)
    
    
    time.sleep(2)
    
    
    '''
    print(servoinfo.SERVO1_ANGLE)
    print(servoinfo.SERVO2_ANGLE)
    print(servoinfo.SERVO3_ANGLE)
    print(servoinfo.SERVO4_ANGLE)
    print(servoinfo.SERVO5_ANGLE)
    print(servoinfo.SERVO6_ANGLE)
    print(servoinfo.SERVO7_ANGLE)
    print(servoinfo.SERVO8_ANGLE)
    print(servoinfo.SERVO9_ANGLE)
    print(servoinfo.SERVO10_ANGLE)
    print(servoinfo.SERVO11_ANGLE)
    print(servoinfo.SERVO12_ANGLE)
    print(servoinfo.SERVO13_ANGLE)
    print(servoinfo.SERVO14_ANGLE)
    print(servoinfo.SERVO15_ANGLE)
    print(servoinfo.SERVO16_ANGLE)
    print(servoinfo.SERVO17_ANGLE)
    '''
    
    servoinfo.SERVO1_ANGLE = 90
    servoinfo.SERVO2_ANGLE = 90
    servoinfo.SERVO3_ANGLE = 90
    servoinfo.SERVO4_ANGLE = 90
    servoinfo.SERVO5_ANGLE = 90
    servoinfo.SERVO6_ANGLE = 90
    servoinfo.SERVO7_ANGLE = 90#max = 110
    servoinfo.SERVO8_ANGLE = 59
    servoinfo.SERVO9_ANGLE = 75
    servoinfo.SERVO10_ANGLE = 109
    servoinfo.SERVO11_ANGLE = 89# max = 80
    servoinfo.SERVO12_ANGLE = 86
    servoinfo.SERVO13_ANGLE = 119#max = 160
    servoinfo.SERVO14_ANGLE = 104
    servoinfo.SERVO15_ANGLE = 69
    servoinfo.SERVO16_ANGLE = 91
    
    servoinfo.SERVO17_ANGLE = 90
    ret = RobotApi.ubtSetRobotServo(servoinfo,5)
