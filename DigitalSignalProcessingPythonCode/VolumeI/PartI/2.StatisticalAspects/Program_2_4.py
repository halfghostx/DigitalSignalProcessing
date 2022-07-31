# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 13:39:24 2022

@author: halfghostx
@name: Program_2_4.py
@function: Random signal with normal PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Random signal with normal PDF. 
fs = 100# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,2,tiv)# Time intervals set (200 values). 
N = len(t)# Number of data points. 
y = np.random.randn(N,1)# Random signal data set. 

# Plots figure. 
plt.plot(t,y,'k')
plt.xlim(0,2)
plt.ylim(-3,3)
plt.xlable('seconds')
plt.title('random signal with normal PDF')
plt.show()