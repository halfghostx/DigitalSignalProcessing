# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 16:17:24 2022

@author: halfghostx
@name: Program_2_9.py
@function: Histogram of a random signal with log-normal PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Histogram of random signal with log-normal PDF. 
fs = 100# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,100,tiv)# Time intervals set (10000 values). 
N = len(t)# Number of data points. 
mu = 0# Mean. 
sigma = 1# Standard deviation. 
y = np.random.lognormal(mu,sigma,(N,1))# Random signal data set. 
v = np.arange(0,12,0.1)# Value intervals set. 

# Plots figure. 
plt.hist(y,v,color='green',ec='black')
plt.xlim(0,8)
plt.ylim(0,700)
plt.xlabel('values')
plt.title('Histogram of random signal with log-normal PDF')
plt.show()