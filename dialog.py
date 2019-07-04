# -*- coding: utf-8 -*-
import sys
stdi, stdo, stde=sys.stdin, sys.stdout, sys.stderr
reload(sys)
sys.stdin, sys.stdout, sys.stderr=stdi, stdo, stde
sys.setdefaultencoding('utf-8')
import requests
import random
import string
import json
import time
import RobotApi


def gen_token():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt
    
def response(text, token):
    post_data = json.dumps({'utterance':text,'token':token})
    requrl = "http://118.192.65.44:9999/chat"
    r = requests.post(requrl, data = post_data)
    res = json.loads(r.text)
    return str(res['utterance'])
    
if __name__ == "__main__":
    RobotApi.ubtRobotInitialize()
    #--------Connect--------------
    gIPAddr="127.0.0.1"
    robotinfo=RobotApi.UBTEDU_ROBOTINFO_T()
    ret=RobotApi.ubtRobotConnect("SDK","1",gIPAddr)
    if(0!=ret):
        print("can not connect to robot %s"%robotinfo.acName)
        exit(1)
    utterance = raw_input("utterance: ")
    token = gen_token()
    while utterance != "exit":
        res = response(utterance, token)
        print res
        RobotApi.ubtVoiceTTS(0, res)
        utterance = raw_input("utterance: ")
