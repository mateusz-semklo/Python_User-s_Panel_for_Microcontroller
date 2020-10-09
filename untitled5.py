# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:08:48 2020

@author: Mateusz
"""




import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import *

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
x=0
t=0
i=0

window=Tk()
window.geometry("1400x900") 
window.title("controler")

# This function is called periodically from FuncAnimation
def animate(i):

    global t,xs,ys


    t=t+1
    
    xs.append(t)
    ys.append(t)




    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)


def fun():
    global i
    i=i+1
    window.after(100,fun)



# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, interval=1000)






label20=Label(window,text="predkosc obrotowa [obr/min] ")    
label20.grid(row=1,column=0,sticky=N)

plt.show()
fun()
window.mainloop()