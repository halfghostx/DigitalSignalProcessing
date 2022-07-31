# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 09:12:03 2022

@author: halfghostx
@name: Program_2_34.py
@function: Integration as expected value
@Python version: Python 3.8
"""

import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt

# Integration as expected value. 
# Integral of g(x)*p(x), where p(x) can be taken as a PDF. 
## The integrand functions. 
x = np.arange(0,1.5*np.pi+(np.pi/100),np.pi/100)# Domain of the integral. 
g = (0.8*np.sin(x))**2# The function g(x). 
mu = 1# Parameter of the exponential distribution. 
p = expon.pdf(x,scale=mu)# The function p(x) (exponential PDF). 
# Deterministic approximation of the integral. 
aux = abs(g*p)
DS = sum(aux)*(np.pi/100)
print("deterministic integral result: ", DS)

# Display of the integrand functions. 
plt.plot(x,g,'k')
plt.plot(x,p,'r')
plt.plot(x,aux,'b')
# Mark the integral area. 
for vx in range(10,151,10):
    l = (vx*np.pi)/100
    plt.plot([l,l],[0,aux[vx]],'g',linewidth=2)

plt.xlim(0,1.5*np.pi)
plt.ylim(0,1.2)
plt.title('Integral of the product g(x)p(x)')
plt.xlabel('x')
plt.legend(['g(x)','p(x)'])
plt.show()

# Monte Carlo Integration. 
# Draw N samples from p(x) as PDF. 
N = 3000# Number of samples. 
x= np.random.exponential(scale=mu,size=N)# The samples. 
# Evaluate g(x) at the samples. 
nv = 0# Counter of valid data points. 
L = 1.5*np.pi# Limit of the integral. 
g = np.zeros((N,))
for nn in range(N):
    if x[nn] <= L:
        g[nn] = (0.8*np.sin(x[nn]))**2
        nv += 1
    else:
        g[nn] = 0# The value of x is outside integral domain. 

# Integral. 
S = sum(g)/nv
# Print result. 
print("Mote Carlo integral result: ", S)