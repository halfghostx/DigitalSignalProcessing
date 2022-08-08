# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:10:22 2022

@author: halfghostx
@name: Program_2_41.py
@function: Two overlapped PDFs
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Two overlapped PDFs. 
x = np.arange(0,2.5+0.01,0.01)
# Densities. 
alpha = 5
beta = 3
Apdf = stats.beta.pdf(x,a=alpha,b=beta)# Beta PDF. 
mu = 1.3
sigma = 0.3
Bpdf = stats.norm.pdf(x,loc=mu,scale=sigma)# Normal PDF. 
# Product of PDFs at intersection zone. 
piz = Apdf[49:100] * Bpdf[49:100]
# Display. 
plt.figure(1)
plt.plot(x,Apdf,'r')
plt.plot(x,Bpdf,'b')
plt.title('Two random variable A and B: their PDFs')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.figure(2)
plt.subplot(211)
plt.plot(x,Bpdf,'b')
plt.plot(x[49:100],Apdf[49:100],'r')
plt.plot([x[49],x[49]],[0,Apdf[49]],'r--')
plt.plot(x[49:100],piz,'k')
plt.title('f(A|B) * f(B)')
plt.show()

plt.subplot(212)
plt.plot(x,Apdf,'r')
plt.plot(x[49:100],Bpdf[49:100],'b')
plt.plot([x[99],x[99]],[0,Bpdf[99]],'b--')
plt.plot(x[49:100],piz,'k')
plt.title('f(B|A) * f(A)')
plt.show()

plt.figure(3)
join = Apdf * Bpdf
plt.plot(x[49:100],join[49:100],'k')
plt.plot(x,Apdf,'r')
plt.plot(x,Bpdf,'b')
plt.title('f(A,B)=f(A) * f(B)')
plt.show()