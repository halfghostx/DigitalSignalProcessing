# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:43:50 2022

@author: halfghostx
@name: Program_2_32.py
@function: Curve and area
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Curve and area. 
# The curve. 
x = np.arange(0,10+0.1,0.1)
y = 0.5+(0.3*np.sin(0.8*x))
plt.plot(x,y,'k')
plt.xlim(0,10)
plt.ylim(0,1)
for vx in range(1,11):
    nx = vx*10
    plt.plot([vx,vx],[0,y[nx]],'g',linewidth=2)

plt.xlabel('x')
plt.ylabel('y')
plt.title('area covered by a curve')