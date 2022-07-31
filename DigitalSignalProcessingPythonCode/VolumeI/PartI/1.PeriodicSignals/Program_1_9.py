# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 08:42:42 2022

@author: halfghostx
@name: Program_1_9.py
@function: Multiplication of sines
@Python version: Python 3.8
"""

import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

import sounddevice as sd
import soundfile as sf

# Multiplication of sines. 
fx = 70# Signal frequency in Hz. 
wx = 2*np.pi*fx# Signal frequency in rad/s. 
fz = 2# Signal frequency in Hz. 
wz = 2*np.pi*fz# Signal frequency in rad/s. 
fs = 6000# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,8,tiv)# Time intervals set (8 seconds). 
y = np.sin(wx*t)*np.sin(wz*t)# Signal data set. 

write('MultiplicationOfSines.wav',fs,y)

# Play audio. 
filename = 'MultiplicationOfSines.wav'
data,fs = sf.read(filename,dtype='float32')
sd.play(data,fs)# Sound. 
status = sd.wait()

t = np.arange(0,1,tiv)# Time intervals set (1 secnods). 
y = np.sin(wx*t)*np.sin(wz*t)# Signal data set. 
plt.plot(t,y,'k')# Plots figure. 
plt.xlim(0,1)
plt.ylim(-1.5,1.5)
plt.xlabel('seconds')
plt.title('multiplication of sines signals')
plt.show()