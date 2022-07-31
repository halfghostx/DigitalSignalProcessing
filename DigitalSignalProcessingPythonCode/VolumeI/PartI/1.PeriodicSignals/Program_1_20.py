# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:54:52 2022

@author: halfghostx
@name: Program_1_20.py
@function: Sine signal and aliasing
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Sine signal and aliasing. 
fy = 3# Signal frequency in Hz. 
wy = 2*np.pi*fy# Signal frequency in rad/s. 
# Good sampling frequency. 
fs = 100# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,3,tiv)# Time intervals set. 
y = np.sin(wy*t)# Signal data set. 
# Plots figure. 
plt.subplot(2,1,1)
plt.plot(t,y,'-k')
plt.xlim(0,3)
plt.ylim(-1.5,1.5)
plt.ylabel('fs=100')
plt.title('3Hz sine signal')

# Too low sampling frequency. 
fs = 4# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,3,tiv)# Time intervals set. 
y = np.sin(wy*t)# Signal data set. 
# Plots figures. 
plt.subplot(2,1,2)
plt.plot(t,y,'-kd',markerfacecolor='none')
plt.xlim(0,3)
plt.ylim(-1.5,1.5)
plt.xlabel('seconds')
plt.ylabel('fs=4')
plt.tight_layout()
plt.show()