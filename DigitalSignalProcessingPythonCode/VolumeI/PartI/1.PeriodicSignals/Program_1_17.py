# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:26:01 2022

@author: halfghostx
@name: Program_1_17.py
@function: Fourier transform of pulse train signal
@Python version: Python 3.8
"""

import numpy as np
from scipy import fftpack as fft
import pandas as pd
import matplotlib.pyplot as plt

# Fourier transform of pulse train signal. 
fy = 1# Signal frequency in Hz. 
wy = 2*np.pi*fy# Signal frequency in rad/s. 
Ty = 1/fy# Signal period in seconds. 
N = 256
W = 20
fs = N*fy# Sampling frequency in Hz. 
y1 = np.zeros((256,),dtype=int)
# Signal period. 
y1[0:W-1] = 1
y1[(256-W):256] = 1
fou = fft.fft(y1)
hmag = fou.real
ah = hmag/N# Get set of harmonic amplitudes. 

markerline,stemlines,baseline = plt.stem(np.arange(0,50,1),
                                         ah[0:50],'k',markerfmt='ko')
markerline.set_markerfacecolor('none')
plt.xlabel('Hz')
plt.title('pulse train harmonics')
plt.show()
