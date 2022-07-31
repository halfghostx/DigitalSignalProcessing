# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:02:55 2022

@author: halfghostx
@name: Program_2_14.py
@function: See and hear a random signal with normal PDF
@Python version: Python 3.8
"""

import numpy as np
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# See and hear a random signal with normal PDF. 
fs = 100# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,2,tiv)# Time intervals set (200 values). 
N = len(t)# Number of data points. 
y = np.random.normal(0,1,(N,))# Random signal data set. 

# Plots figure. 
plt.plot(t,y,'k')
plt.xlim(0,1)
plt.ylim(-3,3)
plt.xlabel('seconds')
plt.title('random signal with normal PDF')
plt.show()

fs = 6000# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,5,tiv)# Time intervals set (5 seconds). 
N = len(t)# Number of data points. 
y = np.random.normal(0,1,(N,))# Random signal data set. 

# Hear random signal. 
write('RandomSignal.wav',fs,y)
# Play audio. 
filename = 'RandomSignal.wav'
data,fs = sf.read(filename,dtype='float32')
sd.play(data,fs)
status = sd.wait()