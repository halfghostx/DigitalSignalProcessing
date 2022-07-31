# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 20:16:55 2022

@author: halfghostx
@name: Program_1_7.py
@function: Sine audio signal
@Python version: Python 3.8
"""

import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

# Library needed to be installed if you want to play .wav file. 
import sounddevice as sd
import soundfile as sf

# Sine audio signal. 
fy = 300# Signal frequency in Hz. 
wy = 2*(np.pi)*fy# Signal frequency in Hz. 
fs = 6000# Sampling frequency in Hz. 
tiv = 1/fs# Time interval between samples. 
t = np.arange(0,5,tiv)# Time intervals set (5 seconds). 
y = np.sin(wy*t)# Signal data set. 
write('SineAudioSignal.wav',fs,y)

# Play audio. 
filename = 'SineAudioSignal.wav'
# Extract data and sampling rate from file. 
data, fs = sf.read(filename, dtype='float32')
sd.play(data, fs)# Sound. 
status = sd.wait()  # Wait until file is done playing. 

t = np.arange(0,0.01,tiv)# Time intervals set (0.01 seconds). 
y = np.sin(wy*t)# Signal data set. 
plt.plot(t,y,'k')# Plots figure. 
plt.xlim(0,0.01)
plt.ylim(-1.5,1.5)
plt.xlabel('seconds')
plt.title('sine signal')