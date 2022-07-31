# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 09:48:30 2022

@author: halfghostx
@name: Program_2_35.py
@function: Integration as expected value: Impotance sampling
@Python version: Python 3.8
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Integration as expected value: Importance sampling. 
# Integral of f(x), an appropriate p(x) PDF is taken. 
# The integrand functions. 
x = np.arange(0,0.25*np.pi+np.pi/100,np.pi/100)# Domain of f(x). 
xx = np.arange(0,1+np.pi/100,np.pi/100)
f = 25*(x**3)*np.cos(2*x)# The function f(x). 
# Parameters of the PDF. 
alpha = 4
beta = 3
p = stats.beta.pdf(xx,alpha,beta)# The function p(x) (beta PDF). 
# Deterministic approximation of the integral. 
DS = sum(f)*(np.pi/100)
print("deterministic integral of the result: ", DS)

#b Display of f(x) and p(x). 
plt.plot(x,f,'k')
plt.plot(xx,p,'r')
plt.xlim(0,1)
plt.ylim(0,2.5)
plt.title('importance sampling: f(x) and p(x)')
plt.xlabel('x')
plt.show()

# Monte Carlo Integration. 
# Draw N samples from p(x) PDF. 
N =2000# Number of samples. 
x = np.random.beta(alpha,beta,size=N)# The samples. 
# Evaluate g(x) at the samples. 
nv = 0# Counter of valid data points. 
g = 0# Initial value. 
for nn in range(N):
    if x[nn] > 0:
        pass# Avoid division by zero. 
    if x[nn] <= (0.25*np.pi):# Values inside f(x) domain. 
        f = 25*(x[nn]**3)*np.cos(2*x[nn])# Evaluate f(x) at xi. 
    else:
        f = 0
    
    p = p = stats.beta.pdf(x[nn],alpha,beta)
    g = g+(f/p)# Adding. 
    nv += 1
    
# Integral. 
S = (g/nv)
print("Monte Carlo integral result: ", S)# Print result. 