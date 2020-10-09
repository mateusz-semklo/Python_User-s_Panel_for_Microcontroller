# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:35:00 2020

@author: Mateusz
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import serial
import numpy as np
import matplotlib.pyplot as plt
import decimal

ser=serial.Serial(
port='COM11',
baudrate=230400,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=None
)
size=2000
x=0
m=[]
n=[]
z=[]


while x<size :
    t=ser.readline(size)
    x+=1
    m.append(t)
    
    
ser.close()
c=0
i=0
for c in m:
    c=c.rstrip() 
    c=float(c)             
    n.append(c)
    
    

t=np.linspace(0,(size-1),size)

        

plt.clf()
plt.plot(t,n)
plt.grid()

plt.savefig('filename1.png', dpi=300)

    