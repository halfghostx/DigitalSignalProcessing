# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 17:48:32 2022

@author: halfghostx
@name: Program_2_22.py
@function: Bivariate normal PDF
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
from matplotlib import cm

# Bivariate normal PDF. 
x1 = np.arange(0,6,0.02)
x2 = np.arange(0,6,0.02)
N = len(x1)
# The PDF. 
mu1 = 3
mu2 = 3
C = np.array([[0.4,0.1],[0.1,0.6]])
D = np.linalg.det(C)
K = 1/(2*np.pi*np.sqrt(D))
Q = (C[0,0]*C[1,1])/(2*D)
ypdf = np.zeros([N,N])# Space for the PDF. 
for ni in range(1,N):
    for nj in range(1,N):
        aux1 = (((x1[ni]-mu1)**2)/C[0,0])+(((x2[nj]-mu2)**2)/C[1,1])
        -(((x1[ni]-mu1)*(x2[nj]-mu2)/C[0,1]*C[1,0]))
        ypdf[ni,nj] = K*np.exp(-Q*aux1)
# Display. 
X1, X2 = np.meshgrid(x1,x2)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X1,X2,ypdf,cmap=cm.jet,linewidth=0,antialiased=False)
ax.set_zlim(0,0.4)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter('{x: .02f}')
fig.colorbar(surf,shrink=0.5,aspect=5)
plt.show()

plt.contour(x1,x2,ypdf)
plt.xlim(1,5)
plt.ylim(1,5)
plt.title('Bivariate Gaussian PDF: top view')
plt.show()