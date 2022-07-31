# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 09:37:39 2022

@author: halfghostx
@name: Program_1_13.py
@function: Fourier transform of rectified signal. 
@Python version: Python 3.8
"""

import numpy as np
from scipy import fftpack as fft
import matplotlib.pyplot as plt

# Fourier transform of rectified sine signal. 
fy = 1# Signal frequency in Hz. 
wy = 2*np.pi*fy# Signal frequency in rad/s. 
Ty = 1/fy# Signal period in seconds. 
N = 256
fs = N*fy# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,Ty,tiv)# Time intervals set. 
y = np.abs(np.sin(wy*t))# Signal data set. 
fou = fft.fft(y)# Fourier transform (set of complex numbers). 
hmag = fou.real
ah = hmag/N# Get set of harmonic amplitudes. 

markerline,stemlines,baseline = plt.stem(np.arange(0,10,1),ah[0:10],'k',
                                         markerfmt='ko')
markerline.set_markerfacecolor('none')
plt.xlabel('Hz')
plt.title('rectified sine signal harmonics')
plt.show()