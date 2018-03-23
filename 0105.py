# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 21:19:32 2018

@author: Administrator
"""

import turtle
t1 = turtle.Turtle('turtle')
x = 20
y=25
n=0

iter = 0
while iter != 10:
        t1.fd(y)
        t1.lt(90)
        t1.fd(y)
        t1.lt(90)
        t1.fd(y)
        t1.lt(90)
        t1.fd(y)
        t1.lt(90)
        t1.rt(x)
        iter += 1
        y +=25

turtle.mainloop()


