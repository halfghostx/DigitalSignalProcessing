# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 09:35:21 2022

@author: halfghostx
@name: Program_2_21.py
@function: Rayleigh PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rayleigh

# Rayleigh PDF. 
v = np.arange(0,5,0.01)# Values set. 
# Random variable parameters. 
beta = 1
ypdf = rayleigh.pdf(v,scale=beta)

# Plots figure. 
plt.plot(v,ypdf,'k')
plt.xlim(0,5)
plt.ylim(0,0.7)
plt.xlabel('values')
plt.title('Rayleigh PDF')
plt.show()