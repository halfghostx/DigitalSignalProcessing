# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 08:41:01 2022

@author: halfghostx
@name: Program_2_31.py
@function: Kernel method example
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Kernel method example. 
viv = 0.02# Set of values. 
v = np.arange(-4,10+viv,viv)# Number of values. 
L = len(v)
# Random data: 
X = [0.1,0.25,1,1.6,2.1,3,4,5.2,5.9,6.5]
N = len(X)# Number of data points. 
Kpdf = np.zeros((N,L))# Reserve space. 
h = 1# Bandwidth. 
q = 1/(np.sqrt(2*np.pi)*h)# Constant. 
for ni in range(N):
    for nj in range(L):
        Kpdf[ni,nj] = (q/N)*math.exp((-(v[nj]-X[ni])**2)/(2*(h)**2))

# Total PDF. 
ypdf = sum(Kpdf)
# Display. 
for ni in range(N):
    plt.plot(v,Kpdf[ni,:],'k')# PDF componets. 
plt.plot(v,ypdf,'r')# Total PDF. 
plt.plot(X,np.zeros(N),'bd')# The data. 
plt.xlim(-4,10)
plt.ylim(0,0.18)
plt.xlabel('vlaues')
plt.ylabel('PDF estimation with Kernel method')
plt.show()