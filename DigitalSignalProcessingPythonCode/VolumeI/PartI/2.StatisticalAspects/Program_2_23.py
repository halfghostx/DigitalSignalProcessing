# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 17:48:56 2022

@author: halfghostx
@name: Program_2_23.py
@function: Binomial PDF
@Python version: Python 3.8
"""

import matplotlib.pyplot as plt
from scipy.stats import binom

# Binomial PDF. 
# Set the values of n and p. 
n = 20
p = 0.5
# Defining list of r values. 
r_values = list(range(n+1))
dist = [binom.pmf(r,n,p) for r in r_values]

# Plots figure. 
markerline,stemlines,baseline = plt.stem(r_values,dist,'k',
                                         markerfmt='ko')
markerline.set_markerfacecolor('none')
plt.xlabel('values')
plt.title('Binomial PDF')
plt.show()