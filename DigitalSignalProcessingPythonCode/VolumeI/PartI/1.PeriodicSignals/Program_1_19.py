# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:49:32 2022

@author: halfghostx
@name: Program_1_19.py
@function: Sine signal and low sampling frequency
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Sine signal and low sampling frequency. 
fy = 1# Signal frequency in Hz. 
wy = 2*np.pi*fy# Signal frequency in rad/s. 
fs = 7# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,3,tiv)# Time intervals set. 
y = np.sin(wy*t)# Signal data set. 
plt.plot(t,y,'-kd',markerfacecolor='none')# Plots figure. 
plt.xlim(0,3)
plt.ylim(-1.5,1.5)
plt.xlabel('seconds')
plt.title('sine signal')
plt.show()