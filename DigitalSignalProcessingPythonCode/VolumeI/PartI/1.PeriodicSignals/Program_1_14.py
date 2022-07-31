# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 09:52:37 2022

@author: halfghostx
@name: Program_1_14.py
@function: Triangular signal to be analyzed
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sig

# Triangular signal to be analyzed. 
fy = 1# Signal frequency in Hz. 
wy = 2*np.pi*fy# Signal frequency in rad/s. 
Ty = 1/fy# Signal period in seconds. 
N = 256
fs = N*fy# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,3*Ty,tiv)# Time interals set (3 seconds). 
y3 = -sig.sawtooth(wy*t,width=0.5)# Signal data set. 

plt.plot(t,y3,'k')# Plots figure. 
plt.xlabel('seconds')
plt.title('triangular signal (3 period)')
plt.show()