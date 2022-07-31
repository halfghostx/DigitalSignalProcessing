# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 09:20:22 2022

@author: halfghostx
@name: Program_2_19.py
@function: Student's PDF
@Python version: Python 3.8
"""

import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt

# Student's PDF. 
v = np.arange(-5,5,0.01)# Values set. 
nu = 3# Random variable parameters ("degree of freedom"). 
ypdf = t.pdf(v,nu)# Student's PDF. 

# Plots figure. 
plt.plot(v,ypdf,'k')
plt.xlim(-5,5)
plt.ylim(0,0.4)
plt.xlabel('values')
plt.title('Student\'s PDF')
plt.show()