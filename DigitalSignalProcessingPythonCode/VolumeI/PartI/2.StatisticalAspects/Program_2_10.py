# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 16:28:57 2022

@author: halfghostx
@name: Program_2_10.py
@function: A skewed PDF with mean, median and mode
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rayleigh

# A skewed PDF with mean, median and mode. 
v = np.arange(0,9,0.01)# Values set. 
alpha = 2# Random variable parameters. 
ypdf = rayleigh.pdf(v,scale=alpha)# Rayleigh PDF. 

# Plots figure. 
plt.plot(v,ypdf,'k')
plt.xlim(0,8)
plt.ylim(0,0.4)
plt.xlabel('values')
plt.title('a skewed PDF')

# Mean, median and mode marked on a PDF. 
fs = 100# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,20,tiv)# Time intervals set (2000 values). 
N = len(t)# Number of data points. 
y = np.random.rayleigh(alpha,(N,1))# Random signal data set. 
mu = np.mean(y)# Mean of y. 
vo = np.median(y)# Median of y. 
# Peak of the PDF. 
pky = np.max(y)
pki = np.argmax(ypdf)
# Plots figure. 
plt_mean = plt.plot([mu,mu],[0,0.33],'--k')# Mean. 
plt_median = plt.plot([vo,vo],[0,0.37],':k')# Median. 
plt_mode = plt.plot([v[pki],v[pki]],[0,pky],'-.k')# Mode. 
plt.legend(['Rayleigh PDF','Mean','Median','Mode'])
plt.show()