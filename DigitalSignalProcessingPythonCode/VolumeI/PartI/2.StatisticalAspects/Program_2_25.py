# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 18:15:54 2022

@author: halfghostx
@name: Program_2_25.py
@function: The geometric PDF
@Python version: Python 3.8
"""

from scipy.stats import geom
import matplotlib.pyplot as plt

# The geometric PDF. 
P = 0.5
N = 10
n = list(range(1,N+2))
ypdf = geom.pmf(n,P)

# Plots figure. 
markerline,stemline,baseline = plt.stem(range(N+1),ypdf,'k',markerfmt='ko')
markerline.set_markerfacecolor('none')
plt.xlabel('values')
plt.title('Geometric PDF')
plt.xlim(-1,N)
plt.ylim(0,0.6)
plt.show()