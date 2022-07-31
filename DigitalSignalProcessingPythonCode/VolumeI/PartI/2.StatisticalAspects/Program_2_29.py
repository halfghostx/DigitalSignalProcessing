# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 18:43:38 2022

@author: halfghostx
@name: Program_2_29.py
@function: Mixture of 2 Gaussians
@Python version: Python 3.8
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Mixture of 2 Gaussians. 
viv = 0.02
v = np.arange(-6,10+viv,viv)
# Parameters of Gaussian 1. 
mu1 = 0
sigma1 = 1.5
# Parameters of Gaussian 2. 
mu2 = 5
sigma2 = 1
ypdf1 = norm.pdf(v,loc=mu1,scale=sigma1)# PDF1. 
ypdf2 = norm.pdf(v,loc=mu2,scale=sigma2)# PDF2. 
p = 0.4# Mix parameter. 
# Mixed Gaussian PDF. 
ypdf = (p*ypdf1)+((1-p)*ypdf2)
# Random data generation. 
N = 5000
y = np.zeros((N,))
for nn in range(N):
    r = np.random.rand(1)# Uniform PDF. 
    if r<p:
        y[nn] = mu1+(sigma1*np.random.normal(0,1,1))
    else:
        y[nn] = mu2+(sigma2*np.random.normal(0,1,1))

# Histogram normalization. 
nB = 100# Number of bins. 
h = 16/100# Bin width. 
k = N*h
# Display. 
n, bins, patches = plt.hist(y,bins=nB,density=True)# Density histogram. 
plt.close()
plt.plot(bins[1:],n,'k')
plt.plot(v,ypdf,'r')# Multi-modal PDF. 
plt.xlabel('values')
plt.title('Mix of 2 Gaussians: histogram and PDF')
plt.xlim(-6,10)
plt.ylim(0,0.3)
plt.show()