# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:14:56 2022

@author: halfghostx
@name: Program_2_15.py
@function: Gamma function
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

# Gamma function. 
v = np.arange(0.1,1,0.01)
y = gamma(v)
# Plots figure. 
plt.plot(v,y,'k')
plt.xlabel('values')
plt.title('gamma function')
plt.show()