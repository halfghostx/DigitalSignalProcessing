# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 09:25:19 2022

@author: halfghostx
@name: Program_2_20.py
@function: Weibull PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Weibull PDF. 
v = np.arange(0,2.5,0.01)# Values set. 
# Random variable parameters. 
alpha = 1
m = 3
ypdf = weibull_min.pdf(v,m,scale=alpha)# Weibull PDF. 

# Plots figure. 
plt.plot(v,ypdf,'k')
plt.xlim(0,2.5)
plt.ylim(0,1.2)
plt.xlabel('values')
plt.title('Weibull PDF')
plt.show()