# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 09:01:41 2022

@author: halfghostx
@name: Program_2_17.py
@function: Chi-square PDF
@Python version: Python 3.8
"""

import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

# Chi-square PDF. 
v = np.arange(-3,16,0.01)# Values set. 
nu = 3# Random variable parameter ("degrees of freedom"). 
ypdf = chi2.pdf(v,nu)# Chi-square PDF. 

# Plots fugure. 
plt.plot(v,ypdf,'k')
plt.xlim(0,16)
plt.ylim(0,0.3)
plt.xlabel('values')
plt.title('chi-square PDF')
plt.show()