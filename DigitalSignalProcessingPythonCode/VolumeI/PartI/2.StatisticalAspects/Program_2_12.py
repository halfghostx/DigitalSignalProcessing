# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 17:47:55 2022

@author: halfghostx
@name: Program_2_12.py
@function: The sine+noise signal
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# The noise+sine signal. 
fs = 100# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,2,tiv)# Time intervals set (200 values). 
N = len(t)# Number of data points. 
yr = np.random.normal(0,1,(N,))# Random signal data set. 
ys = np.sin(15*2*np.pi*t)# Sinusoidal signal (15 Hz). 
y = yr+ys# The signal+noise. 

# Plots figure. 
plt.plot(t,y,'k')
plt.xlim(0,2)
plt.ylim(-3,3)
plt.xlabel('seconds')
plt.title('sine+noise signal')
plt.show()