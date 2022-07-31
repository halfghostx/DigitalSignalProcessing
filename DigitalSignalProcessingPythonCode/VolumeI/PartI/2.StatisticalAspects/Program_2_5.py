# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:29:17 2022

@author: halfghostx
@name: Program_2_5.py
@function: Normal PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Normal PDF. 
v = np.arange(-3,3,0.01)# Values set. 
# Random variable parameters. 
mu = 0# Mean. 
sigma = 1# Standard deviation. 
ypdf = norm.pdf(v,loc=mu,scale=sigma)# Normal PDF. 
# Plots figure. 
plt.plot(v,ypdf,'k')
plt.xlim(-3,3)
plt.ylim(0,0.5)
plt.xlabel('values')
plt.title('normal PDF')
plt.show()