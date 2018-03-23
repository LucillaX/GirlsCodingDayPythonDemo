# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 21:46:04 2018

@author: Administrator
"""

import turtle
t1 = turtle.Turtle('turtle')


iter = 0
x=25
y=90
s=45

while iter != 4:
          t1.fd(x)
          t1.rt(y)
          iter += 1
         
t1.lt(90-s)
t1.fd(25)
t1.rt(90-s)
t1.fd(25)
t1.rt(90+s)
t1.fd(25)
t1.lt(90-s)
t1.fd(25)
t1.lt(90+s)
t1.fd(25)
t1.lt(90-s)
t1.fd(25)
t1.lt(180)
t1.fd(25)
t1.rt(90-s)
t1.fd(25)
t1.lt(90+s)

def NINI(t):

  t1.fd(12.5)
  t1.lt(s)
  t1.fd(25)
  t1.lt(90+s)
  t1.fd(12.5)
  t1.lt(180)
  t1.fd(12.5)
  t1.rt(90)
  t1.fd(25)
  t1.rt(s)
  t1.fd(25)
  t1.rt(90+s)
  t1.fd(25)
  t1.lt(180)
  t1.fd(25)
  t1.rt(90)
  t1.fd(25*t)
  t1.rt(90)
  t1.fd(25)
  t1.rt(s)
  t1.fd(12.5*1.414)
  t1.lt(180)
  t1.fd(12.5*1.414)
  t1.lt(90+s)
  n=0
  while n !=t:
      t1.fd(25)
      t1.rt(90)
      t1.fd(25)
      t1.lt(180)
      t1.fd(25)
      t1.rt(90)
      n+=1
  t1.rt(90)
  t1.fd(25)
  t1.lt(90)
  
NINI(2)
NINI(3)
NINI(4)
NINI(5)



turtle.mainloop()