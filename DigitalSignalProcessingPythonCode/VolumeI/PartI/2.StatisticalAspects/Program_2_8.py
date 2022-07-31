# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 16:06:43 2022

@author: halfghostx
@name: Program_2_8.py
@function: Log-normal PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

# Log-normal PDF. 
v = np.arange(-3,6,0.01)# Values set. 
# Random variable parameters. 
mu = 0# Mean. 
sigma = 1# Standard deviation. 
ypdf = lognorm.pdf(v,s=sigma,scale=np.exp(mu))# Log-normal PDF. 
# Plots figure. 
plt.plot(v,ypdf,'k')
plt.xlim(0,6)
plt.yxlim(0,0.7)
plt.xlabel('values')
plt.title('log-normal PDF')
plt.show()