# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 20:02:36 2022

@author: halfghostx
@name: Program_1_6.py
@function: Sawtooth signals
@Python version: Python 3.8
"""

import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt

# Sawtooth signals. 
fy = 100# Signal frequency in Hz. 
wy = 2*(np.pi)*fy# Signal frequency in rad/s. 
duy = 0.03# Signal duration in seconds. 
fs = 20000# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,duy,tiv)# Time intervals set. 

y = sig.sawtooth(wy*t,0.1)# Signal data set (width 0.1)
plt.subplot(2,2,1)
plt.plot(t,y,'k')
plt.xlim(0,duy)
plt.ylim(-1.5,1.5)
plt.xlabel('seconds')
plt.title('sawtooth signal')

y = sig.sawtooth(wy*t,0.3)# Signal data set (width 0.3)
plt.subplot(2,2,2)
plt.plot(t,y,'k')
plt.xlim(0,duy)
plt.ylim(-1.5,1.5)
plt.xlabel('seconds')
plt.title('sawtooth signal')

y = sig.sawtooth(wy*t,0.5)# Signal data set (width 0.5)
plt.subplot(2,2,3)
plt.plot(t,y,'k')
plt.xlim(0,duy)
plt.ylim(-1.5,1.5)
plt.xlabel('seconds')
plt.title('sawtooth signal')

y = sig.sawtooth(wy*t,0.9)# Signal data set (width 0.9)
plt.subplot(2,2,4)
plt.plot(t,y,'k')
plt.xlim(0,duy)
plt.ylim(-1.5,1.5)
plt.xlabel('seconds')
plt.title('sawtooth signal')

plt.tight_layout()
plt.show()