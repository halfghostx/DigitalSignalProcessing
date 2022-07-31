# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 18:04:46 2022

@author: halfghostx
@name: Program_2_24.py
@function: Poisson PDF
@Python version: Python 3.8
"""

from scipy.stats import poisson
import matplotlib.pyplot as plt

# Poisson PDF. 
lambda_v = 20
N = 50
x = list(range(N+1))
y = poisson.pmf(x,mu=lambda_v,loc=0)

# Plots figure. 
markerline,stemlines,baseline = plt.stem(x,y,'k',markerfmt='ko')
markerline.set_markerfacecolor('none')
plt.xlable('values')
plt.title('Poisson PDF')
plt,show()