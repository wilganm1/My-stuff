""" Make a neural network with a lot of inputs. This is one has 441000 inputs"""

from scipy.io import wavfile
import numpy as np

a = wavfile.read('my_voice_data.wav')    #Audio file that's 10 seconds long with 44100 frames per second. 44100 * 10 = 441000
b = np.array(a[1], dtype = float)      #Gets an array of just the numbers

input_neurons = len(b)     #Each number in the array is one input
number_hidden_layers = 1   #How many hidden layers 
hidden_neurons = 5     #How many neurons in each hidden layer
output_neurons = 1      #How many output neurons

""" Make a dictionary of weights for each hidden neuron. Have each value be a list. The number of 
lists = number of neurons and the length of the lists are the number of neurons in the input layer """

numb_hid_neurons = []   #Will eventually have the numbers 0 to the number of hidden neurons

for i in range(hidden_neurons):    
     numb_hid_neurons.append(i)    #Adds in the numbers

Hidden_layer = {}     #This dictionary will have as many keys as hidden neurons, and will have a list of weights as the value.
for a in numb_hid_neurons:         
    Hidden_layer[f'{a}' ] = np.random.uniform(-2, 2,input_neurons)  #Generates a list with as many weights as there are input_neurons. -2 & 2 are arbitrary.
  """ Hidden_layer['0'] will have 441000 numbers in a list. These are the weights. The 
  dictionary has as many keys as hidden_neurons. Now make a dictionary for the actual hidden layer inputs """
  
Hidden_inputs = {'1':0,      #Eventually be the dot product of each neuron.
                 '2':0,
                 '3':0,
                 '4':0,      #Note that the keys begin at 1 and not 0. This is important.
                 '5':0}

for j in range(len(b)):     #This whole thing is the dot product for each hidden neuron.
    for i in range(1,6):
        Hidden_inputs[str(i)] += Hidden_layer[str(i-1)][j] * b[j]  #Adds every single weight * input to the correct neuron.

for x in Hidden_inputs:
    Hidden_inputs[str(x)] += 1
