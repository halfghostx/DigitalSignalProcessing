# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:31:31 2022

@author: halfghostx
@name: Program_1_2.py
@function: Sinusoidal signal
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Sinusoidal signal. 

fy = 1# Signal frequency in Hz. 
wy = 2*(np.pi)*fy# Signal frequency in rad/s. 
fs = 60# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,3,tiv)# Time intervals set, 180 values. 
y = np.sin(wy*t)# Signal data set. 
plt.plot(t,y,'k')# Plots figures. 
plt.xlim(0,3)
plt.ylim(-1.5,1.5)
plt.xlabel('seconds')
plt.title('sine signal')