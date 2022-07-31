# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 19:37:03 2022

@author: halfghostx
@name: Program_2_16.py
@function: Gamma-type PDFs
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Gamma-type PDFs. 
v = np.arange(0,10,0.01)# Values set. 
# Random variable parameters. 
alpha = 1
beta = 1
ypdf = gamma.pdf(v,alpha,0,beta)# Gamma-type PDF. 
plt.plot(v,ypdf,'k')# Plots figure. 
plt.xlim(0,10)
plt.ylim(0,1.2)
# Random variable parameters. 
alpha = 2
beta = 1
ypdf = gamma.pdf(v,alpha,0,beta)# Gamma-type PDF. 
plt.plot(v,ypdf,'--k')# Plots figure. 
plt.xlim(0,10)
plt.ylim(0,1.2)
# Random variable parameters. 
alpha = 4
beta = 1
ypdf = gamma.pdf(v,alpha,0,beta)# Gamma-type PDF. 
plt.plot(v,ypdf,':k')# Plots figure. 
plt.xlim(0,10)
plt.ylim(0,1.2)
plt.legend([r'$\alpha = 1$',r'$\alpha = 2$',r'$\alpha = 4$'])
plt.show()