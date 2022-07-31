# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 09:22:20 2022

@author: halfghostx
@name: Program_2_11.py
@function: Power spectral density (PSD) of random signal with log-normal PDF
@Python version: Python 3.8
"""

import numpy as np
from scipy.signal import welch, hanning
import matplotlib.pyplot as plt

# Power spectral density (PSD) of random signal with log-normal PDF. 
fs = 100# Sampling frequency in HZ. 
tiv = 1/fs# Time interval between samples. 
t = np.linspace(0,40.96,4096)# Time intervals set (4096 values). 
N = len(t)# Number of data points. 
# Random variable parameters. 
mu = 0# Mean. 
sigma = 1# Standard deviation. 
# Random signal data set. 
y = np.random.lognormal(mu,sigma,(N,))

# Welch. 
nfft = 256# Length of FFT. 
window = hanning(nfft)# Window function. 
numoverlap = 128# Number of samples overlap. 
f,Pxx_den = welch(y,fs=fs,window=window,noverlap=numoverlap,
                  nfft=nfft,return_onesided=True,detrend=False)

# Plots figure. 
plt.semilogy(f, Pxx_den,'k')
plt.xlim(0,50)
plt.xlabel('Frequency(Hz)')
plt.ylabel('Power Spectral Density (dB/Hz)')
plt.show()