# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 12:59:07 2022

@author: halfghostx
@name: Program_2_2.py
@function: Uniform PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Uniform PDF. 
v = np.linspace(0,1,100)# Values set. 
ypdf = uniform.pdf(v)# Uniform PDF. 

# Plots figure. 
plt.plot(v,ypdf,'k')
plt.xlim(-0.5,1.5)
plt.ylim(0,1.1)
plt.xlabel('values')
plt.title('uniform PDF')
plt.plot([0,0],[0,1],'--k')
plt.plot([1,1],[0,1],'--k')
plt.show()