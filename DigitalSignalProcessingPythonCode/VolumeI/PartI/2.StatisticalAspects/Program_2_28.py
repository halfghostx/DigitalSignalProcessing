# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 17:53:35 2022

@author: halfghostx
@name: Program_2_8.py
@function: Likehood example
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Likehood example. 
sig2 = 1
# Constant. 
r = 1/(2 * sig2)
# Reserve space. 
Lh = np.zeros((4,101))
# N is number of data. 
N = np.array([20,60,200,500])
for ni in range(4):
    # Data generation with normal distribution, 
    # mean = 5, sigma = 1. 
    mu = 5
    sigma = 1
    x = np.random.normal(mu,sigma,N[ni])
    K = (-N[ni]/2) * np.log(2 * np.pi * sig2)
    aux = 0
    for nm in range(1,102):
        mu1 = (nm - 1) / 10# Mean. 
        aux = (x - mu1)**2
        Lh[ni,nm-1] = K-(r*sum(aux))# Log-Likelihood. 

# Display. 
ex = np.arange(0,10.1,0.1)
for ni in range(4):
    plt.subplot(int('22'+str(ni+1)))
    plt.plot(ex,Lh[ni,:],'k')
    plt.xlim(0,10)
    plt.ylim(-2000,0)
    plt.tight_layout()
plt.show()
