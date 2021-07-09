"""
Author : Gülşah Büyük
Date : 18.03.2021
"""
from tkinter import *
from random import random

def montecarlo():
    all = int(E1.get())
    inside=0
    for i in range(all):
        x,y=random(),random()
        if(x**2+y**2)**(0.5)<1: inside=inside+1
    mypi=4.0*(inside/all)
    mytext= "My pi value ="+str(mypi)
    label.config(text=mytext)

top = Tk()
L1= Label(top,text="Number of points")
L1.pack()
E1=Entry(top)
E1.pack()
B1= Button(top,text="Find my pi",width =10, command=montecarlo)
B1.pack()
label= Label(top)
label.pack()
mainloop()
