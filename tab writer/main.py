import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io.wavfile import read
from playsound import playsound
import numpy as np
import sys
import matplotlib
import random

"""
Goal: Make an automated tab writer using a 
neural network that can detect sounds in real-time
and predict the notes played when it happens in 
real-time. 
"""

"""
Construction ideas: How should I make the networks
 1. Make a super massive singular neural network
 with 78 input nodes with the entire matrix 
 arrays for each node.
 running gradient descent on something this big
 might not be possible.
 
 2. Make 1 network for each fret, with each array
 you get from the numpy matrix when you read it 
 being a node, and then using each output layer 
 node as a node in a conglomerate neural network.
 Will have to run gradient descent and stuff 
 for each neural network.
"""

#Reading a wav file and getting its sound as an array
a = read('60.wav')    
b = np.array(a[1], dtype = float) #gets only array 
#np.set_printoptions(threshold=sys.maxsize)
   #Prints out all arrays. Don't do it.     
print(b)
print("Arrays in b: " + str(len(b)))


b[0]
print(b[0])
print(b[-1])

n = b[900]
n
print(n)
cvc = (b[0:5])
vcv = str(cvc)
print(cvc)

qet = []

cvc[0] 
cvc[0][:2]

qet = []
for item in cvc:
    for j in item:    #How can I automate list creation for every single array 
        qet.append(j)    #without having the word 'array'
print(qet)

n = len(b)
N = 5
list_test = [cvc[i][0:] for i in range(0, 5)]

list_test
print(list_test)

qet = []
for i in list_test:
    qet.append(i)
print(qet[-1])

#Accesses the arrays in b variable
print(b[0]) #first array
print(b[20][0]) #first value in 19th array
print(b[-1]) #last array

e = read('testing.wav')
f = np.array(e[1], dtype=float)
print(f)
print(len(f))

#8.05% percent of a second = 3551 arrays
playsound('testing.wav')


"""
Set up the first layer of the neural network

Right now all we want is to predict whether 
the network can detect a 60 note. 
      yes = [1]   no = [0]
"""

inputs = []
inputs = [b[i][0:] for i in range(0, n-1)]
print(inputs[:6])


weights = []
for ii in range(0, 3550):
    ii = (random.uniform(0.00, 4.00))
    weights.append(ii)
print(weights)

layer1_output = []
for i in range(len(inputs)):
    layer1_output.append(inputs[i] * weights[i])
print(layer1_output)


#----------------------------------------------
#How we get recording things in real-time.
fs = 44100  # Sample rate
seconds = 4  # Duration of recording
print("Recording")

#this is the recording that happens
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1) 
sd.wait()  # Wait until recording is finished
print("Finished")


