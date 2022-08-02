# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 10:34:19 2022

@author: halfghostx
@name: Program_2_39.py
@function: Rejection sampling
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generation of random data with a desired PDF. 
# Using rejection method. 
# Example of desired PDF. 
x = np.arange(0,np.pi+np.pi/100,np.pi/100)
dpf = 0.5 * np.sin(x)# Desired PDF. 
# Example of proposal PDF. 
xp = np.arange(0,np.pi+3+np.pi/100,np.pi/100)
ppf = stats.rayleigh.pdf(xp, scale=1.5)
# Factor. 
c = 1.5
# Generation of random data. 
N = 2000# Number of data. 
z = np.zeros(N)# Space for data to be generated. 
for nn in range(N):
    accept = 0
    while accept == 0:
        v = np.random.rayleigh(scale=1.5,size=1)# Rayleigh distribution. 
        u = np.random.rand(1)# Uniform distribution. 
        if v <= np.pi:
            # Must be inside dpf domain. 
            P = u * c * stats.rayleigh.pdf(v,scale=1.5)
            L = 0.5 * np.sin(v)
            if P < L:
                z[nn] = v
                accept = 1

# Display. 
plt.figure(1)
plt.plot(x,dpf,'k')
plt.plot(xp,c*ppf,'r')
plt.xlabel('x')
plt.title('desired PDF and proposal PDF')
plt.tight_layout()
plt.show()
plt.figure(2)
plt.hist(z, 30,color='green',edgecolor='black')
plt.xlabel('x')
plt.title('histogram of the generated data')
plt.tight_layout()
plt.show()