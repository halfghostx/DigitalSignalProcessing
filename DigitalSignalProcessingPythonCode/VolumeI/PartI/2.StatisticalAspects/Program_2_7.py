# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:50:34 2022

@author: halfghostx
@name: Program_2_7.py
@function: Random signal with log-normal PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Random signal with log-normal PDF. 
fs = 100# Sampling frequency in Hz. 
tiv = 1/fs# Time interval betweem samples. 
t = np.arange(0,2,tiv)# Time intervals set (200 values). 
N = len(t)# Number of data points. 
# Random signal parameters. 
mu = 0# Mean. 
sigma = 1# Standard deviation. 
y = np.random.lognormal(mu,sigma,(N,1))# Random signal data set. 
# Plots figure. 
plt.plot(t,y,'k')
plt.xlim(0,2)
plt.ylim(0,12)
plt.xlabel('seconds')
plt.title('random signal with log-normal PDF')
plt.show()