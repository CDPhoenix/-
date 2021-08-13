# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 16:57:21 2021

@author: WANG Dapeng Phoenix
"""

import turtle as tl
tl.pencolor('red')
for i in range(20):
    tl.right(-45+i*15)
    tl.circle(-50,180)
    tl.fd(100)
    tl.right(90)
    tl.fd(100)
    tl.circle(-50,180)
tl.done()
