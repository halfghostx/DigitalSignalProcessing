# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:44:12 2022

@author: halfghostx
@name: Program_2_6.py
@function: Histogram of a random signal with normal PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Histogram of a random signal with normal PDF. 
fs = 100# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,100,tiv)# Time intervals set (10000 values). 
N = len(t)# Number of data points. 
y = np.random.randn(N,1)# Random signal data set. 
v = np.arange(-4,4,0.1)# Value intervals set. 

# Plots figure. 
plt.hist(y,v,color='green',ec='black')
plt.xlabel('values')
plt.title('Histogram of a random signal with normal PDF')
plt.show()