# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 01:58:41 2018

@author: Administrator
"""

from turtle import *
from random import randint

speed(10)
penup()
goto(-140, 140)
for step in range(16):
    write(step,align='center')
    right(90)
    forward(10)
    n=8
    while n!=0:
     pendown()
     forward(10)
     penup()
     forward(10)
     n-=1
    backward(170)
    left(90)
    forward(20)

ada=Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()


    

bob=Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()


cuc=Turtle()
cuc.color('yellow')
cuc.shape('turtle')
cuc.penup()
cuc.goto(-160,40)
cuc.pendown()



ded=Turtle()
ded.color('green')
ded.shape('turtle')
ded.penup()
ded.goto(-160,10)
ded.pendown()




for turn in range(100):
    ada.forward(randint(1,5))
   
    bob.forward(randint(1,5))
  
    cuc.forward(randint(1,5))
 
    ded.forward(randint(1,5))
