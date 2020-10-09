# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 14:47:54 2020

@author: Mateusz
"""
from tkinter import *
import json
import time
import socket
import sys
import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import time

id_loop=0
encoder=0
speed=0
t=0
ts=[0]
xs=[0]
ys=[0]

fig = plt.figure(figsize=(5, 4), dpi=100)
ax1 = fig.add_subplot(1,1,1)

window=Tk()
window.geometry("1400x900") 
window.title("controler")

def animate(i):

    global t,ts,ys

    ax1.clear()
    ax1.plot(ts, ys)


def myClick():
       
    jstring = '{"settings":"t","set":"1","current":"0.5","speed":"2200","speed_Kp":"5","speed_Ki":"5","speed_Kd":"0","id_Kp":"1","id_Ki":"1","id_Kd":"0","iq_Kp":"4","iq_Ki":"1","iq_Kd":"0"}'
    js=json.loads(jstring)
    js["settings"]='t'
    js["set"]='1'
    js["current"]=e2.get()
    js["speed"]=e1.get()
    js["speed_Kp"]=e9.get()
    js["speed_Ki"]=e10.get()
    js["speed_Kd"]=e11.get()
    js["id_Kp"]=e6.get()
    js["id_Ki"]=e7.get()
    js["id_Kd"]=e8.get()
    js["iq_Kp"]=e3.get()
    js["iq_Ki"]=e4.get()
    js["iq_Kd"]=e5.get()
    
    
    message = json.dumps(js)
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.0.6', 3333)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    
    
    try:
    
        # Send data
        
        #print('sending "%s"' % message)
        message=str.encode(message)
        sock.sendall(message)



    finally:
        print('transmit and recive complete')
        sock.close()
        
def myClick3():
       
    jstring = '{"settings":"t","set":"0","start_stop":"0"}'
    js=json.loads(jstring)
    js["settings"]='t'
    js["set"]='0'
    js["start_stop"]='1'

        
    message = json.dumps(js)
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.0.6', 3333)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    
    
    
    try:
    
        # Send data
    
        print('sending "%s"' % message)
        message=str.encode(message)
        sock.sendall(message)





    finally:
        print('transmit  complete')
        sock.close()
        
def myClick4():
       
    jstring = '{"settings":"t","set":"0","start_stop":"0"}'
    js=json.loads(jstring)
    js["settings"]='t'
    js["set"]='0'
    js["start_stop"]='0'

        
    message = json.dumps(js)
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.0.6', 3333)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    
    
    
    try:
    
        # Send data
    
        print('sending "%s"' % message)
        message=str.encode(message)
        sock.sendall(message)
  


    finally:
        print('transmit  complete')
        sock.close()
   
    
        
def myClick1():
    update()
    
def myClick2():
    global flag
    #flag=1
    t=0
    ts.clear()
    ys.clear()
    xs.clear()
    window.after_cancel(id_loop)
    
   
    
        
        
        

    
def update():
    global id_loop,flag,speed,encoder,t,ts,xs,ys,j
    message = '{"settings":"n","speed_en":"0","angle_en":"0"}'
    #js=json.loads(jstring)
    #js["settings"]='n'

       
   #message = json.dumps(js)
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.0.6', 3333)
    #print('connecting to %s port %s' % server_address)
    sock.connect(server_address)
      
    
    try:
    
        # Send data
    
        #print('sending "%s"' % message)
        message=str.encode(message)
        sock.sendall(message)

        # Look for the response
        #amount_received = 0
        #amount_expected = len(message)
    
        #while amount_received < amount_expected:
        #datax = sock.recv(70)
        #amount_received += len(datax)
        
        #data=datax.decode()   
        #print('received "%s"' % data)
       
    
        #j=json.loads(data)
        #speed=float(j["speed_en"])
        #encoder=int(j["angle_en"])
        ts.append(t)
        t=t+0.01
        ys.append(speed)
        ts=ts[-50:]
        ys=ys[-50:]

        
        

    finally:
        #print('transmit and recive complete')
        sock.close()
     
        
        id_loop = window.after(50,update)
        #label21=Label(window,text=j["speed"])    
        #label21.grid(row=1,column=0,sticky=W)





   
   
    
i=0
label0=Label(window,text="UKŁAD NAPĘDOWY SILNIKA BLDC")    
label0.grid(row=i,column=0)
i=i+1
label2=Label(window,text="")    
label2.grid(row=i,column=0)

i=i+1
label1=Label(window,text="zadana prędkosc")    
label1.grid(row=i,column=0)
e1=Entry(window)
e1.insert(0,"2500");
e1.grid(row=i,column=1)

button1 = Button(window, text = "Wyslij ustawienia",height=2 ,command=myClick)
button1.grid(row=i,column=2,rowspan=2,columnspan=2)
button5 = Button(window, text = "Start", height=2,width=10 ,command=myClick3)
button5.grid(row=i,column=3,columnspan=3,rowspan=2)

button6 = Button(window, text = "Stop",height=2,width=10 ,command=myClick4)
button6.grid(row=i,column=4,rowspan=2,columnspan=4)

i=i+1
label2=Label(window,text="zadany prąd")    
label2.grid(row=i,column=0)
e2=Entry(window)
e2.insert(0,"0.5");
e2.grid(row=i,column=1)

i=i+1
label2=Label(window,text="")    
label2.grid(row=i,column=0)


i=i+1
label5=Label(window,text="NASTAWY DLA REGULATORA PRADU Iq")    
label5.grid(row=i,column=0)

i=i+1
label6=Label(window,text="Kp")    
label6.grid(row=i,column=0,sticky=E)
e3=Entry(window)
e3.insert(0,"4");
e3.grid(row=i,column=1)

label3=Label(window,text="Ki")    
label3.grid(row=i,column=2)
e4=Entry(window)
e4.insert(0,"1");
e4.grid(row=i,column=3)

label3=Label(window,text="Kd")    
label3.grid(row=i,column=4)
e5=Entry(window)
e5.insert(0,"0");
e5.grid(row=i,column=5)

i=i+1
label2=Label(window,text="")    
label2.grid(row=i,column=0)

i=i+1
label7=Label(window,text="NASTAWY DLA REGULATORA PRADU Id")    
label7.grid(row=i,column=0)

i=i+1
label8=Label(window,text="Kp")    
label8.grid(row=i,column=0,sticky=E)
e6=Entry(window)
e6.insert(0,"1");
e6.grid(row=i,column=1)

label3=Label(window,text="Ki")    
label3.grid(row=i,column=2)
e7=Entry(window)
e7.insert(0,"1");
e7.grid(row=i,column=3)

label3=Label(window,text="Kd")    
label3.grid(row=i,column=4)
e8=Entry(window)
e8.insert(0,"0");
e8.grid(row=i,column=5)

i=i+1
label2=Label(window,text="")    
label2.grid(row=i,column=0)

i=i+1
label5=Label(window,text="NASTAWY DLA REGULATORA PRĘDKOSCI")    
label5.grid(row=i,column=0)

i=i+1
label6=Label(window,text="Kp")    
label6.grid(row=i,column=0,sticky=E)
e9=Entry(window)
e9.insert(0,"5");
e9.grid(row=i,column=1)

label3=Label(window,text="Ki")    
label3.grid(row=i,column=2)
e10=Entry(window)
e10.insert(0,"5");
e10.grid(row=i,column=3)

label3=Label(window,text="Kd")    
label3.grid(row=i,column=4)
e11=Entry(window)
e11.insert(0,"0");
e11.grid(row=i,column=5)

i=i+1
label2=Label(window,text="------------------------------------------------------------------------------------------------------------------------------------------------------")    
label2.grid(row=i,column=0,columnspan=6)

i=i+1
label2=Label(window,text="")    
label2.grid(row=i,column=0)


i=i+1
button2 = Button(window,height=2, text = "Rysuj wykres", command=myClick1)
button2.grid(row=i,column=0)
button3 = Button(window,height=2, text = "Stop wykres", command=myClick2)
button3.grid(row=i,column=1)
Label
i=i+1
label2=Label(window,text="")    
label2.grid(row=i,column=0)

i=i+1

label20=Label(window,text="predkosc obrotowa [obr/min] ")    
label20.grid(row=i,column=0,sticky=E)

ani = animation.FuncAnimation(fig, animate, interval=50)

label20=Label(window,text="predkosc obrotowa [obr/min] ")    
label20.grid(row=i,column=0,sticky=N)


window.mainloop()


