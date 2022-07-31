# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 13:56:24 2022

@author: halfghostx
@name: Parzen.py
@function: Parzen method to estimate PDF. 
@Python version: Python 3.8
"""

# Parzen method to estimate PDF. 

import numpy as np
import matplotlib.pyplot as plt

def gaussian_pdf(x, mu, sigma):
    prob = 1/np.sqrt(2*np.pi)/sigma*np.exp(-(x-mu)**2/2/sigma**2)
    return prob

def parzen_window_pdf(x, data, sigma):
    px = [gaussian_pdf(x, mu=mu, sigma=sigma) for mu in data]
    return np.mean(np.array(px), axis=0)

data = [2, 2.5, 3, 1, 6]
x = np.arange(-5, 12, 0.1)
prob = parzen_window_pdf(x, data, sigma=1)
plt.figure(figsize=(15,5))
plt.plot(x, prob)
plt.plot(data, [0]*len(data), '.r')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.grid()
plt.show()