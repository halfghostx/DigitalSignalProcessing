# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:52:07 2022

@author: halfghostx
@name: Program_2_33.py
@function: Monte Carlo points, and area approximation
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt

# Monte Carlo points, and area approximation. 
# The curve. 
x = np.arange(0,10+0.1,0.1)
y = 0.5+(0.3*np.sin(0.8*x))
# The random points. 
N = 500# Number of points. 
px = 10*np.random.rand(N)
py = np.random.rand(N)
plt.plot(x,y,'k')
plt.plot(px,py,'b.')
plt.xlim(0,10)
plt.ylim(0,1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('curve and random points')
# Area calculation. 
na = 0# Counter of accepted points. 
for nn in range(1,N+1):
    xnn = px[nn-1]
    ynn = 0.5+(0.3*np.sin(0.8*xnn))
    if py[nn-1]<ynn:
        na += 1

# Print computed area. 
# The plot rectangle area is 10. 
A = (10.0*na)/N
print('The approximated area is: %f' % A)