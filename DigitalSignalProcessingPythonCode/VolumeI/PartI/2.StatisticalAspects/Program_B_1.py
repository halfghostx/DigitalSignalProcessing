# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 20:00:08 2022

@author: halfghostx
@name: Program_B_1.py
@function: Example of Markov Chain (weather prediction)
@Python version: Python 3.8
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import time

# Example of Markov Chain
# with 3 states. 
# Transition matrix. 
T = np.array([[0.65,0.20,0.15],
             [0.30,0.24,0.46],
             [0.52,0.12,0.36]])
# Initial probabilities. 
pC = 0.5
pS = 0.4
pR = 0.1
# Initial state. 
np.random.seed(int(time.perf_counter() * 100))
u = np.random.rand(1)
if u < pC:
    X = 1
elif u < pC + pS:
    X = 2
else:
    X = 3
# Initialize result R. 
# Clouds. 
if X == 1:
    R = 'C'
# Sun. 
if X == 2:
    R = 'S'
# Rain. 
if X == 3:
    R = 'R'

rX = np.zeros(60)# For state historic. 
rX[0] = X
# Run the process. 
for nn in range(1,60):
    u = np.random.rand(1)
    # State transitions. 
    if X == 1:
        if u < T[0,0]:
            X = 1
        elif u < (T[0,0] + T[0,1]):
            X = 2
        else:
            X = 3
    
    if X == 2:
        if u < T[1,0]:
            X = 1
        elif u < (T[1,0] + T[1,1]):
            X = 2
        else:
            X = 3
    
    if X == 3:
        if u < T[2,0]:
            X = 1
        elif u < (T[2,0] + T[2,1]):
            X = 2
        else:
            X = 3
    
    rX[nn] = X# Store result. 
    # Concatenation. 
    if X == 1:
        R = R + 'C'# Clouds. 
    if X == 2:
        R = R + 'S'# Sun. 
    if X == 3:
        R = R + 'R'# Rain. 

# Display. 
print(R)
plt.plot(rX,'k')
plt.xlim(0,60)
plt.ylim(0.8,3.2)
plt.title('3 states Markov Chain: transitions')
plt.xlabel('n')
plt.show()