import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io.wavfile import read
from playsound import playsound
import numpy as np
import sys
import matplotlib
import glob
import os
import wave
import random
import math

"""
Neural networks need inputs and weights to start off.
Each numpy matrix for every note will have to be
an input itself. Do this for all notes.
For now we will only use the frets 0-12.
13 * 6 = 78 inputs nodes.

This is a classification problem.

I could do a 1 input 1 output network
  O---O  + bias node
"""

a = read("testing.wav")    
b = np.array(a[1], dtype = float) #gets only array 
print(b)
b
print("Arrays in b: " + str(len(b)))
n = len(b)
n
b[3550] #last array
weights = []
for x in range(0,3551):
    weights.append(random.uniform(-1,1))
    
#Now to get the ouput from the dot product. Can't actually run the dot method, so we need to loop it.
output = [0,0]
for qu in range(0,3551):
    output += (b[qu] * weights[qu])    #This is the dot product for this first layer.

print(output)
output + 1

"""
def sigmoid():
    uqo = (1 / (1 + (math.e**-(eib))))
    print(uqo)
    print(len(uqo))
    total = 0
    for i in uqo:
        if i >= 0.5:
            total+= 1
    print(total)
"""   
