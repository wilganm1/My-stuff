""" Make a function that will recognize my voice. If it detects my voice it will run and if it  doesn't detect my voice it won't run. Voices have frequencies to them,
so I just need Python  to recognize the frequencies of my voice. I did this same thing in NeuroTab. Just read the  wav file as  numpy array.I can do this with numpy
or pydub or pyaudio. I would need to make a classification neural network that will know whether it's me or not.
This is completely optional"""

import numpy as np
import pydub
import pyaudio
import time
import sounddevice as sd     #plays audio files
import time         #controls time
from scipy.io.wavfile import write  #write wav files
from scipy.io.wavfile import read  #write wav files


"""Record audio and save it as files to get numpy data. I need to record probably hundreds of different lines with all pronunciations of all sounds in the alphabet. """

"""Make a classification neural network. Use cross entropy for loss function"""

a = read("my_voice_data.wav")
inputs = np.array(a[1], dtype = float)
weights = np.array(np.random.uniform(np.random.randn(), np.random.randn(), len(inputs)))
global bias
bias = 1
target = 1
inputs

def sigmoid(x):
    prediction = 1 / (1 + np.exp(-x))
    return prediction

def deriv_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))

""" Ouput layer """
Z = np.dot(inputs, weights) + bias
prediction = sigmoid(Z)

""" Binary cross entropy loss """
def loss(target, prediction):
    loss = -(target*np.log(prediction) + (1-target)*np.log(1-prediction))
    return loss

#Derivative of BCE
def deriv_BCE(target, prediction):
    dBCE = (-target/prediction) + ((1-target)/(1-prediction))
    return dBCE





        
        
    
