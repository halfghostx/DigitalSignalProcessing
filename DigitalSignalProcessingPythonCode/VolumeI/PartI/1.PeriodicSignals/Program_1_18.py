# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:41:22 2022

@author: halfghostx
@name: Program_1_18.py
@function: Sinc function
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Sinc functon. 
fy = 1# Signal frequency in Hz. 
wy = 2*np.pi*fy# Signal frequency in rad/s. 
Ty = 1/fy# Signal period in seconds. 
N = 256
fs = N*fy# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(-6*Ty,6*Ty,tiv)# Time intervals set (12 seconds). 
y = np.sinc(t)# Signal data set. 

plt.plot(t,y,'k')
plt.xlabel('seconds')
plt.title('sinc function')
plt.show()