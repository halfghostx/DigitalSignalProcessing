# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 20:01:52 2022

@author: halfghostx
@name: Program_B_2.py
@function: Example of HMM (synthetic speech)
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
import time

# Example of HMM (synthetic speech)
# with 2 states. 
# Each state has 4 emission alternatives. 
# Transition matrix (probabilities). 
T = np.array([[0.3,0.7],
              [0.5,0.5]])
# Emissions from state 1 (probabilities). 
E1 = np.array([0.2,0.3,0.2,0.3])
# Emissions from state 2 (probabilities). 
E2 = np.array([0.3,0.3,0.2,0.2])
pC = 0.6# Consonant (X=1). 
pW = 0.4# Wovel (X=2). 
# Initial state. 
np.random.seed(int(time.perf_counter() * 100))
u = np.random.rand(1)
X = 2
if u < pC:
    X = 1
# Initial emission. 
u = np.random.rand(1)
if X == 1:
    if u < E1[0]:
        EM = 1
        R = 'W'
    elif u < (E1[0] + E1[1]):
        EM = 2
        R = 'H'
    elif u < (E1[0] + E1[1] + E1[2]):
        EM = 3
        R = 'T'
    else:
        EM = 4
        R = '_'

if X == 2:
    if u < E2[0]:
        EM = 1
        R = 'A'
    elif u < (E2[0] + E2[1]):
        EM = 2
        R = 'E'
    elif u < (E2[0] + E2[1] + E2[2]):
        EM = 3
        R = 'O'
    else:
        EM = 4
        R = 'U'

rX = np.zeros(60)# For state record. 
rE = np.zeros(60)# For emission record. 
rX[0] = X
rE[0] = EM
# Run the process. 
for nn in range(1,60):
    u = np.random.rand(1)
    # State transitions. 
    if X == 1:
        X = 2
        if u < T[0,0]:
            X = 1
    
    if X == 2:
        X = 1
        if u < T[1,1]:
            X = 2
    
    u = np.random.rand(1)
    if X == 1:
        if u < E1[0]:
            EM = 1
            R = R + 'W'
        elif u < (E1[0] + E1[1]):
            EM = 2
            R = R + 'H'
        elif u < (E1[0] + E1[1] + E1[2]):
            EM = 3
            R = R + 'T'
        else:
            EM = 4
            R = R + '_'
    
    if X == 2:
        if u < E2[0]:
            EM = 1
            R = R + 'A'
        elif u < (E2[0] + E2[1]):
            EM = 2
            R = R + 'E'
        elif u < (E2[0] + E2[1] + E2[2]):
            EM = 3
            R = R + 'O'
        else:
            EM = 4
            R = R + 'U'
    
    rX[nn] = X# Store result. 
    rE[nn] = EM

# Display. 
print(R)# Print result. 
plt.subplot(211)
plt.plot(rX,'k')
plt.title('HMM (synthetic speech): the hidden states')
plt.xlabel('n')
plt.xlim(0,60)
plt.ylim(0.8,2.2)
plt.subplot(212)
plt.plot(rE,'k')
plt.xlim(0,60)
plt.ylim(0.5,4.5)
plt.title('the emissions')
plt.xlabel('n')
plt.tight_layout()
plt.show()