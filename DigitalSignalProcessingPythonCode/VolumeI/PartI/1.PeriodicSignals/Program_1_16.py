# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 10:06:48 2022

@author: halfghostx
@name: Program_1_16.py
@function: Pulse train signal
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Pulse train signal to be analyzed. 
fy = 1# Signal frequency in Hz. 
wy  = 2*np.pi*fy# Signal frequency in rad/s. 
Ty = 1/fy# Signal period in seconds. 
N = 256
fs = N*fy# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,3*Ty,tiv)# Time intervals set (3 periods). 
W = 20

# Signal first part: 
y1 = np.zeros((256,),dtype=int)
y1[0:W-1] = 1
y1[(256-W):256] = 1
# Signal to be ploted. 
yt = pd.concat([pd.DataFrame([y1]),pd.DataFrame([y1]),
                pd.DataFrame([y1])],axis=1)
yt = np.array(yt)
yt = yt.reshape((len(t),))

plt.plot(t,yt,'k')
plt.xlabel('seconds')
plt.title('pulse train signal (3 period)')