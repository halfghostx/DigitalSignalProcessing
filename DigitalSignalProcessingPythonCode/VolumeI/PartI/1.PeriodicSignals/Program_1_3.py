# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:38:39 2022

@author: halfghostx
@name: Program_1_3.py
@function: Sine and cosine signals
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Sine and cosine signal. 
fy = 1# Siganl frequency in Hz. 
wy = 2*(np.pi)*fy# Signal frequency in rad/s. 
fs = 60# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,3,tiv)# Time intervals set. 
ys = np.sin(wy*t)# Signal data set. 
plt.plot(t,ys,'k')# Plots figure. 
yc= np.cos(wy*t)# Signal data set. 
plt.plot(t,yc,'k--')# Plots figure. 
plt.xlim(0,3)
plt.ylim(-1.5,1.5)
plt.xlabel('seconds')
plt.title('sine (solid) and cosine (dashed)')
plt.show()