# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:25:47 2022

@author: halfghostx
@name: Program_2_37.py
@function: Numerical inversion of a function
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Numerical inversion of a function. 
# Example of F = sin(x), in the growing interval. 
M = 1001
y = np.arange(0,1+0.001,0.001)# F between 0 and 1. 
x = np.zeros(M)
# Incremental inversion. 
aux = 0
dax = 0.001*np.pi
for ni in range(M):
    while y[ni] > np.sin(aux):
        aux = aux+dax
    x[ni] = aux

# Display. 
plt.plot(y,np.arcsin(y),'gx')# Analytical inversion. 
plt.plot(y,x,'k')# Result of numerical inversion. 
plt.xlabel('y')
plt.ylabel('x')
plt.title('numerical and analytical inversion of F')
plt.show()