# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 09:15:01 2022

@author: halfghostx
@name: Program_2_18.py
@function: Beta PDF
@Python version: Python 3.8
"""

import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

# Beta PDF. 
v = np.arange(0,1,0.01)# Values set. 
# Random variable parameters. 
alpha = 5
beta_p = 3
ypdf = beta.pdf(v,alpha,beta_p)# Beta PDF. 
# Plots figure. 
plt.plot(v,ypdf,'k')
plt.xlim(0,1)
plt.ylim(0,2.5)
plt.xlabel('values')
plt.title('beta PDF')
plt.show()