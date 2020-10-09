# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:32:51 2020

@author: Mateusz
"""

import socket

data = "Hello world!"
data=str.encode(data)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sent = sock.sendto(data, ('192.168.0.6', 3333))

sock.close()

 
  
      
       

   