# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:40:01 2022

@author: halfghostx
@name: Program_2_27.py
@function: Weibull probability plot
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import weibull_min

# Weibull probability plot. 
N = 200# 200 values. 
rng = np.random.default_rng()
# Random signal with weibull PDF. 
c = 1
x = stats.weibull_min.rvs(c=c,loc=0,scale=1,size=N,random_state=rng)
# Plots figure. 
ax = plt.subplot(111)
res = stats.probplot(x,c,plot=plt,dist='weibull_min')
plt.xlabel('Data')
plt.ylabel('Probability')
plt.show()