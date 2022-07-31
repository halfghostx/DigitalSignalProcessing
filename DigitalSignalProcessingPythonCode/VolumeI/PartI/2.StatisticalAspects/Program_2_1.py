# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 12:51:06 2022

@author: halfghostx
@name: Program_2_1.py
@function: Random signal with uniform PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Random signal with uniform PDF. 
fs = 100# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,2,tiv)# Time intervals set (200 values). 
N = len(t)# Number of data points. 
y = np.random.rand(N,1)# Random signal data set. 

plt.plot(t,y,'k')# Plots figure. 
plt.xlim(0,2)
plt.ylim(0,1.2)
plt.xlabel('seconds')
plt.title('random signal with uniform PDF')
plt.show()