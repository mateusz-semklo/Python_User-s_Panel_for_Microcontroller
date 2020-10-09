# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:53:16 2020

@author: Mateusz
"""

import socket

UDP_IP = "192.168.0.6"
UDP_PORT = 3333
MESSAGE  = "Hello UDP Server\n/n"

bytesToSend  = str.encode(MESSAGE)

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(bytesToSend, (UDP_IP, UDP_PORT))

