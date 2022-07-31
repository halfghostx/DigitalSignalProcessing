# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:14:27 2022

@author: halfghostx
@name: Program_3_36.py
@function: Generation of random data with a desired PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Generation of random data with a desired PDF ... 
# using analytic inversion. 
# Example of desired distribution function. 
x = np.arange(0,np.pi/2+np.pi/100,np.pi/100)
F = np.sin(x)# An always growing curve. 
pf = np.cos(x)# PDF = derivative of F. 
# Generation of random data. 
N = 2000# Number of data. 
y = np.random.rand(N)# Uniform distribution. 
# Random data generation: 
z = np.arcsin(y)# The inverse of F. 
# Display. 
plt.subplot(121)
plt.plot(x,F,'k')
plt.xlabel('x')
plt.title('desired distribution function')
plt.subplot(122)
plt.plot(x,pf,'k')
plt.xlabel('x')
plt.title('desired PDF')
plt.show()

plt.hist(z,bins=30,color='green',edgecolor='black')
plt.xlabel('x')
plt.title('histogram of the generated data')
plt.show()