# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 00:06:26 2018

@author: Administrator
"""

import turtle
t1 = turtle.Turtle('turtle')
x=100

iter = 0

def NINI(T):
  m=0
  while m!=T:
    n=(-1)**(m+1)
   
    if m==0:
       t1.circle(10,240)
    t1.circle(n*10,360)
    t1.circle(n*10,180)
    m+=1
    

 

t1.lt(30)

while iter!=6:
 t1.fd(x)
 t1.circle(-10,180)
 t1.fd(x)
 t1.circle(-10,360)
 t1.lt(180)
 

 iter+=1
 
def VAVA(T):
    m=T
    
    while m!=0:
        n=(-1)**m
        t1.circle(n*10,180)
        m-=1
    t1.circle(10,300)
    t1.lt(180)
 
NINI(5)
t1.circle(-10,180)
t1.circle(10,180)
t1.circle(-10,180)
t1.circle(10,180)
t1.circle(-10,180)
t1.circle(10,300)
t1.lt(180)
NINI(4)
VAVA(4)
NINI(3)
VAVA(3)
NINI(2)
VAVA(2)
NINI(1)
VAVA(1)



 




