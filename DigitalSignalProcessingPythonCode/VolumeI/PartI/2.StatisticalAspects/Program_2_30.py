# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:27:45 2022

@author: halfghostx
@name: Program_2_30.py
@function: Histogram of Bimodal distribution
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Histogram of Bimodal distribution. 
# Geyser eruption data (time between eruptions). 
# Read data. 
filename = 'Geyser1.txt'
def load_txt_method(filename):
    data = np.loadtxt(filename,dtype=np.float32,delimiter='\n')
    return data

data = load_txt_method(filename)
# Display. 
plt.hist(data,30,edgecolor='k',color='green')
plt.title('Time between Geyser eruption')
plt.show()