# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:18:09 2020

@author: Mateusz
"""

import socket

UDP_IP = "192.168.0.2"
UDP_PORT = 3333

start=1

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while start==1:
    data, addr = sock.recvfrom(150) # buffer size is 1024 bytes
    data=data.decode()
    print("   %s" % data)
    if (data[1]=='b'):
        start=0
        
    
    
    

