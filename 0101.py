# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 20:16:47 2018

@author: Administrator
"""

import turtle
t1 = turtle.Turtle('turtle')


iter = 0
x=50
y=90

while iter != 5:
          t1.fd(x)
          t1.rt(y)
          t1.fd(x)
          t1.rt(y)
          t1.fd(x)
          t1.rt(y)
          t1.fd(x)
          t1.rt(y)
          x =x+50
          iter += 1

turtle.mainloop()