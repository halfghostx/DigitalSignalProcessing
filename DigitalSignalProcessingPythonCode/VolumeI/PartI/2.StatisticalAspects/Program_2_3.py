# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 13:13:10 2022

@author: halfghostx
@name: Program_2_3.py
@function: Histogram of a random signal with uniform PF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Histogram of a random signal with uniform PDF. 
fs = 100# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,100,tiv)# Time intervals set (10000 values). 
N = len(t)# Number of data points. 
y = np.random.rand(N,1)# Random signal data set. 
v = np.arange(0,1,0.02)# Value intervals set. 

# Plots histogram. 
plt.hist(y,v,color='green',ec='black')
plt.xlabel('values')
plt.title('Histogram of random signal with uniform PDF')
plt.show()