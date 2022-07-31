# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 17:53:28 2022

@author: halfghostx
@name: Program_2_13.py
@function: Power spectral density (PSD) of a signal+noise
@Python version: Python 3.8
"""

import numpy as np
from scipy.signal import welch, hanning
import matplotlib.pyplot as plt

# Power spectral density (PSD) of a signal+noise. 
fs = 100# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,40.96,tiv)# Time intervals set (4096 values). 
N = len(t)# Number of data points. 
yr = np.random.normal(0,1,(N,))# Random signal data set. 
ys = np.sin(15*2*np.pi*t)# Sinusoidal signal (15 Hz). 
y = ys+yr# The signal+noise. 
window = hanning(256)# Window function. 
numoverlap = 128# Number of samples overlap. 
f,Pxx_den = welch(y,fs=fs,window=window,noverlap=numoverlap,detrend=False,
                  return_onesided=True)

# Plots figure. 
plt.semilogy(f,Pxx_den,'k')
plt.xlim(0,50)
plt.xlabel('Frequency(Hz)')
plt.ylabel('Power Spectral Density(dB/Hz)')
plt.show()