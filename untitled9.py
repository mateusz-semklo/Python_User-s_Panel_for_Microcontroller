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

g=0
id_loop=0
encoder=0
speed=0
t=0
ts=[0]
xs=[0]
y_speed=[0]
y_angle=[0]
y_rms_Ia=[0]
y_rms_Ib=[0]
y_rms_Ic=[0]
var1='n'


fig = plt.figure(figsize=(10,8))
grid = plt.GridSpec(6, 6, wspace=1, hspace=0.3)


ax1=fig.add_subplot(grid[0:3, :3])
ax2=fig.add_subplot(grid[3:, :3])
ax3=fig.add_subplot(grid[0:2, 3:])
ax4=fig.add_subplot(grid[2:4, 3:])
ax5=fig.add_subplot(grid[4:6, 3:])

window=Tk()
window.geometry("800x500") 
window.title("controler")

def animate(i):

    global t,ts,y_speed,y_angle,y_rms_Ia,y_rms_Ib,y_rms_Ic

    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    ax5.clear()
    
    ax1.plot(ts, y_speed)
    ax1.set_ylabel('predkosc obrotowa [obr/min]')
    
    ax2.plot(ts, y_angle)
    ax2.set_ylabel('położenie wirnika [stopnie]')
    
    ax3.plot(ts, y_rms_Ia)
    ax3.set_ylabel('Ia [A]')
    
    ax4.plot(ts, y_rms_Ib)
    ax4.set_ylabel('Ib [A]')
    
    ax5.plot(ts, y_rms_Ic)
    ax5.set_ylabel('Ic [A]')
    



def myClick():
    global g   
    jstring = '{"settings":"t","set":"1","current":"0.5","speed":"2200","speed_Kp":"5","speed_Ki":"5","speed_Kd":"0","id_Kp":"1","id_Ki":"1","id_Kd":"0","iq_Kp":"4","iq_Ki":"1","iq_Kd":"0","a_set":"1","angle":"1000","a_Kp":"5", "a_Ki":"1", "a_Kd":"0"}'
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
    js["a_set"]=var1.get()
    js["angle"]=e15.get()
    js["a_Kp"]=e12.get()
    js["a_Ki"]=e13.get()
    js["a_Kd"]=e14.get()

    
    
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
    y_speed.clear()
    y_angle.clear()
    y_rms_Ia.clear()
    y_rms_Ib.clear()
    y_rms_Ic.clear()
    window.after_cancel(id_loop)
    
   
    
        


    
def update():
    global id_loop,flag,speed,encoder,t,ts,xs,j,y_speed,y_angle,y_rms_Ia,y_rms_Ib,y_rms_Ic
    message = '{"settings":"n"}'
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
        datax = sock.recv(200)
        #amount_received += len(datax)
        
        data=datax.decode()    
        #print('received "%s"' % data)
       
    
        j=json.loads(data)
        speed=float(j["speed"])
        encoder=int(j["encoder"])
        rms_Ia=float(j["rms_Ia"])
        rms_Ib=float(j["rms_Ib"])
        rms_Ic=float(j["rms_Ic"])
        ts.append(t)
        t=t+0.01
        y_speed.append(speed)
        y_angle.append(encoder)
        y_rms_Ia.append(rms_Ia)
        y_rms_Ib.append(rms_Ib)
        y_rms_Ic.append(rms_Ic)
        ts=ts[-200:]
        y_speed=y_speed[-200:]
        y_angle=y_angle[-200:]
        y_rms_Ia=y_rms_Ia[-200:]
        y_rms_Ib=y_rms_Ib[-200:]
        y_rms_Ic=y_rms_Ic[-200:]

        
        

    finally:
        #print('transmit and recive complete')
        sock.close()      
        id_loop = window.after(50,update)


  
i=0
label0=Label(window,text="UKŁAD NAPĘDOWY SILNIKA BLDC")    
label0.grid(row=i,column=0)
i=i+1
label2=Label(window,text="")    
label2.grid(row=i,column=0)

i=i+1
label1=Label(window,text="zadana prędkosc [obr/min]")    
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
label2=Label(window,text="ograniczenie wartosci prądu [A]")    
label2.grid(row=i,column=0)
e2=Entry(window)
e2.insert(0,"0.5");
e2.grid(row=i,column=1)


i=i+1
label2=Label(window,text="zadane położenie wirnika [stopnie]")    
label2.grid(row=i,column=0)
e15=Entry(window)
e15.insert(0,"20000");
e15.grid(row=i,column=1)


var1= StringVar()

ch1=Checkbutton(window, text="sdsds", variable=var1, onvalue="y", offvalue="n")
ch1.grid(row=i,column=2)



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
label5=Label(window,text="")    
label5.grid(row=i,column=0)

i=i+1
label5=Label(window,text="NASTAWY DLA REGULATORA POŁOŻENIA")    
label5.grid(row=i,column=0)

i=i+1
label6=Label(window,text="Kp")    
label6.grid(row=i,column=0,sticky=E)
e12=Entry(window)
e12.insert(0,"5");
e12.grid(row=i,column=1)

label3=Label(window,text="Ki")    
label3.grid(row=i,column=2)
e13=Entry(window)
e13.insert(0,"0");
e13.grid(row=i,column=3)

label3=Label(window,text="Kd")    
label3.grid(row=i,column=4)
e14=Entry(window)
e14.insert(0,"0");
e14.grid(row=i,column=5)

i=i+1
label5=Label(window,text="")    
label5.grid(row=i,column=0)

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

i=i+1
label2=Label(window,text="")    
label2.grid(row=i,column=0)

i=i+1



ani = animation.FuncAnimation(fig, animate, interval=50)




window.mainloop()


