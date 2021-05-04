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
"""
Neural networks need inputs and weights to start off.
Each numpy matrix for every note will have to be
an input itself. Do this for all notes.
For now we will only use the frets 0-12.
13 * 6 = 78 inputs nodes. 
"""

a = read("testing.wav")    
b = np.array(a[1], dtype = float) #gets only array 
print(b)
print("Arrays in b: " + str(len(b)))
n = len(b)
n

b[3550] #last array

#Try to get every array in a list.
my_list = []

#Make a list of the arrays
for array in b[0:8]:
    my_list.append(array)
print(my_list)
#prints array([~~~]) before everything.

#Try another way of getting it 
b[0]  #prints the array with the word array
print(b[0])  #prints the array without the word array
b[0][1]   #gets 2nd number in first array

inputs = []
inputs = [b[i][0:] for i in range(0, n-1)]
print(inputs[:6])

"""
Lets try to loop all the arrays as inputs for 
the first layer of the network. Weights will 
be random using random.uniform()
"""

weights = []
for ii in range(0, 3550):
    ii = (random.uniform(0.00, 4.00))
    weights.append(ii)
print(weights)

"""
Okay, I have the inputs and the weights to go with 
it. Now its time to see if I can multiply the 
arrays with weights.
"""

inputs[0]
weights[0]

inputs[3549]  #last value
weights[3550]  #out of range
inputs[-1]

len(inputs)
len(weights)
node1 = inputs[0] * weights[0]
print(node1)

#YES!!! Now to figure out how to loop the inputs 
#and weights

inputs[1] * weights[1]

bna= []
for i in inputs[0:6]: #can loop through inputs
    bna.append(i *3)
print(bna)

thv = []
for j in weights:
    thv.append(j+5)  # can loop through weights
print(thv)

layer1_output = []
for i in range(len(inputs)):
    layer1_output.append(inputs[i] * weights[i])
print(layer1_output[0])
    
