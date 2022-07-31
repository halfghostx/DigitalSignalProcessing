# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 08:29:02 2022

@author: halfghostx
@name: Program_1_8.py
@function: Sum of sines signals
@Python version: Python 3.8
"""

import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

# Library needed to be installed if you want to play .wav file. 
import sounddevice as sd
import soundfile as sf

# Sum of sines signals. 
fy = 300# Signal frequency in Hz. 
wy = 2*(np.pi)*fy# Signal frequency in rad/s. 
fs = 6000# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,5,tiv)# Time intervals set (5 seconds). 

# Signal data set: 
y = 0.64*np.sin(wy*t)+0.21*np.sin(3*wy*t)+0.12*np.sin(5*wy*t)
write('SineAudioSignal.wav', fs, y)

# Play audio. 
filename = 'SineAudioSignal.wav'
# Extract data and sampling frequency from file. 
data,fs = sf.read(filename,dtype='float32')
sd.play(data, fs)# Sound. 
status = sd.wait()# Wait until file is done playing. 

# Signal data set: 
y = 0.6*np.sin(wy*t)+0.3*np.sin(3*wy*t)+0.2*np.sin(5*wy*t)
plt.plot(t,y,'k')# Plots figure. 
plt.xlim(0,0.01)
plt.ylim(-1.5,1.5)
plt.xlabel('seconds')
plt.title('sum of sines signals')
plt.show()