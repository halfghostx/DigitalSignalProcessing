# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:12:15 2022

@author: halfghostx
@name: Program_1_1.py
@function: Square signal
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Square signal. 
A = [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0]
fs = 10# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,3,tiv)# Time intervals set(30 values). 
plt.scatter(t,A,marker='*')# Plots figure. 
plt.xlim(0,3)
plt.ylim(-0.5,1.5)
plt.xlabel("sec.")
plt.title("square wave samples")
plt.show()