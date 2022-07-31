# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:05:36 2022

@author: halfghostx
@name: Program_2_26.py
@function: Normal probability plot
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Normal probability plot. 
N = 200# 200 values. 
rng = np.random.default_rng()
# Random signal with normal PDF. 
x = stats.norm.rvs(loc=0,scale=1,size=N,random_state=rng)
# Plots figure. 
ax = plt.subplot(111)
res = stats.probplot(x,plot=plt)
plt.xlabel('Data')
plt.ylabel('Probability')
plt.show()