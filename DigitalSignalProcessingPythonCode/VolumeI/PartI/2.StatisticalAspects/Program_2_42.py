# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 19:58:01 2022

@author: halfghostx
@name: Program_2_42.py
@function: Generation of random data with a desired PDF
@Python version: Python 3.8
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Generation of random data with a desired PDF.  
# Using MCMC. 
# Metropolis algorithm. 
# Example of desired PDF. 
x = np.arange(0,np.pi+np.pi/100,np.pi/100)
dpf = 0.5 * np.sin(x)# Desired PDF. 
# Example of proposal PDF (normal). 
xp = np.arange(-4,4+np.pi/100,np.pi/100)
sigma = 0.6# Deviation. 
q = stats.norm.pdf(xp,loc=0,scale=sigma)
# Generation of random data. 
N = 5000# Number of data. 
z = np.zeros(N);# Space for data to be generated. 
x0 = np.pi / 2# Initial value. 
for nn in range(N):
    inr = 0
    while inr == 0:
        # New value proposal (Markovian transition). 
        x1 = x0 + (sigma * np.random.randn(1))# Normal distribution (symetric). 
        if (x1 < np.pi) and (x1 > 0):
            inr = 1# x1 is valid (is inside dpf domain). 
        
    f1 = 0.5 * np.sin(x1)
    f0 = 0.5 * np.sin(x0)
    alpha = f1 / f0
    if alpha >= 1:
        z[nn] = x1# Accept. 
    else:
        aux = np.random.rand(1)
    
    if aux < alpha:
        z[nn] = x1# Accept. 
    else:
        z[nn] = x0

    x0 = x1

nz = z[999:5000]# Eliminate initial data. 

# Display. 
plt.figure(1)
plt.plot(x,dpf,'k')
plt.plot(xp,q,'r')
plt.xlim(-2,4)
plt.ylim(0,0.8)
plt.xlabel('x')
plt.title('desired PDF and proposal PDF')
plt.show()

plt.figure(2)
plt.hist(nz,30,color='green',edgecolor='black')
plt.xlabel('x')
plt.title('histogram of the generated data')
plt.show()