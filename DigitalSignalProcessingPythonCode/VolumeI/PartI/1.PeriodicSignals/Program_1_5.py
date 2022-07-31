# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:54:59 2022

@author: halfghostx
@name: Program_1_5.py
@function: Sawtooth signal
@Python version: Python 3.8
"""

import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt

# Sawtooth signal. 
fy = 100# Signal frequency in Hz. 
wy = 2*(np.pi)*fy# Signal frequency in rad/s. 
duy = 0.03# Signal duration in seconds. 
fs = 20000# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,duy,tiv)# Time intervals set. 
y = sig.sawtooth(wy*t)# Signal data set. 
plt.plot(t,y,'k')# Plots figure. 
plt.xlim(0,duy)
plt.ylim(-1.5,1.5)
plt.xlabel('seconds')
plt.title('sawtooth signal')