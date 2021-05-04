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

#add the array values together
b[0][0] + b[0][1]
b[1][0] + b[1][1]

add_values = []
for i in b:
    toq = i[0] + i[1]
    add_values.append(toq)
add_values

"""
Okay so...I couldn't get the sigmoid function to
work because I can't put in arrays. So what I've
decided to do is to combine the two values in 
each [] in the b matrix together, then 
multiply those by a random weight, and plug those
values into the sigmoid function 
"""

"""
Lets try to loop all the arrays as inputs for 
the first layer of the network. Weights will 
be random using random.uniform()
"""

inputs = [b[i][0:] for i in range(0, n-1)]
inputs[0:2]

weights = []
for ii in range(0, 3550):
    ii = (random.uniform(-1.00, 1.00))
    weights.append(ii)

bias1 = np.array([1])

"""
Okay, I have the inputs and the weights to go with 
it. Now its time to see if I can multiply the 
arrays with weights.
"""

layer1_outputs = []
for i in range(len(inputs)):
    layer1_outputs.append(inputs[i] * weights[i])
    
layer1_outputs.append(np.array([1]))

layer1_outputs

"""
I might only need one node for input, no hidden
layers, and one ouput node for one single note.

so y = [1] if its a 60 note.
"""

#theta = weights. 
#x = inputs

weights = np.asarray(weights)


"""
May need to combine the values in each array so I
can run sigmoid function
"""

weights
add_values

weights[0] *add_values[0]
weights[0:2]*add_values[0:2]

#hθ(x) = 1/(1+e^(-(θ^T)*x)) 

bie = []
for i in range(len(weights)):
    bie.append(weights[i] *add_values[i])
print(bie)

   
eib = np.asarray(bie)
eib[0]


def sigmoid():
    uqo = (1 / (1 + (math.e**-(eib))))
    print(uqo)
    print(len(uqo))
    total = 0
    for i in uqo:
        if i >= 0.5:
            total+= 1
    print(total)
    

3550/1791

1791/3550
def sig():
      answer = (1 / (1 + np.exp(-eib)))
      print(answer)

