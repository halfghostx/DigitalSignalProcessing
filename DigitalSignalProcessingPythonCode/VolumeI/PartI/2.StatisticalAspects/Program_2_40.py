# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 14:35:31 2022

@author: halfghostx
@name: Program_2_40.py
@function: Central limit of wav sounds
@Python version: Python 3.8
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf

# Cental limits of wav sounds. 
# Read a set of sound files. 
y1, fs = sf.read('srn01.wav', dtype='float32')
y2, fs = sf.read('srn02.wav', dtype='float32')
y3, fs = sf.read('srn04.wav', dtype='float32')
y4, fs = sf.read('srn06.wav', dtype='float32')
y5, fs = sf.read('log35.wav', dtype='float32')
y6, fs = sf.read('ORIENT.wav', dtype='float32')
y7, fs = sf.read('elephant1.wav', dtype='float32')
y8, fs = sf.read('harp1.wav', dtype='float32')
# Note: all signals have in this example fs = 16000. 
N = 25000# Clip signals to this length. 
y = np.zeros((8,N))# Signal set. 
y[0,:] = np.transpose(y1[0:N])
y[1,:] = np.transpose(y2[0:N])
y[2,:] = np.transpose(y3[0:N])
y[3,:] = np.transpose(y4[0:N])
y[4,:] = np.transpose(y5[0:N])
y[5,:] = np.transpose(y6[0:N])
y[6,:] = np.transpose(y7[0:N])
y[7,:] = np.transpose(y8[0:N])
# Normalization. 
for nn in range(8):
    s = y[nn,:]
    s = s - np.mean(s)# Zero mean. 
    vr = np.var(s)
    s = s / np.sqrt(vr)# Variance = 1. 
    y[nn,:] = s
# Sum of signals. 
S = np.sum(y,axis=0)
# Histogram. 
plt.figure(1)
plt.hist(S,30,color='green',edgecolor='black')
plt.title('histogram of the sum of signals')
plt.show()
# Sounds of the sum. 
sd.play(S,fs)# Sound. 
status = sd.wait()# Wait until file is done playing. 