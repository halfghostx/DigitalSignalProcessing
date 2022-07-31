# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:38:41 2022

@author: halfghostx
@name: Program_3_38.py
@function: Generation of random data with a desired PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Generation of random data with a desired PDF ... 
# using numerical inversion. 
# First: a table with the inversion of F. 
M = 1001
y = np.arange(0,1+0.001,0.001)# F between 0 and 1. 
x = np.zeros((M,))
# Incremental inversion. 
aux = 0
dax = 0.001*np.pi
for ni in range(M):
    while y[ni] > np.sin(aux):
        aux = aux+dax
    x[ni] = aux

# Second: generate uniform random data. 
N = 2000# Number of data. 
ur = np.random.rand(N)# Uniform distribution. 
# Third: use inversion table. 
z = np.zeros(N)
for nn in range(N):
    # Compute position in the table:
    pr = 1+int(np.round(ur[nn]*1000))
    z[nn] = x[pr]# Read output table. 

# Display histogram of generated data. 
plt.hist(z,30,color='green',edgecolor='black')
plt.xlabel('z')
plt.title('histogram of the generated data')