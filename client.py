# -*- coding: utf-8 -*-
import socket

def send_op(op, ip):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip, 9999))
    
    print s.recv(1024)
    s.send(op)
    print s.recv(1024)
    
    s.send('exit')
    s.close()
