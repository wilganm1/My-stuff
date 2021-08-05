""" Make a function that will recognize my voice.
If it detects my voice it will run and if it 
doesn't detect my voice it won't run. Voices 
have frequencies to them, so I just need Python 
to recognize the frequencies of my voice.

I can do this with numpy or pydub or pyaudio.
I would need to make a classification neural 
network that will know whether it's me or not.

This is completely optional"""

""" Step 1: Figure it out
So to do this I will need Python to recognize my
specific voice. It will need to be able to read
and detect different sound frequencies and match them
to me. I will need a neural network, fast-fourier transforms,
and numpy for this"""

import numpy as np
import pydub
import pyaudio
import time
import sounddevice as sd     #plays audio files
import time         #controls time
from scipy.io.wavfile import write  #write wav files
from scipy.io.wavfile import read  #write wav files
import matplotlib.pyplot as plt


""" Step 2: Getting frequencies
This part is the easy one. All i have to do 
is record myself talking normally for about 
2-6 seconds to get enough range of my vocal
frequencies. Then I'll just extact all the
unique frequencies into a list so I don't
have any repeats. Then save it as a numpy 
array to be used for the neural network.
"""
a = read("my_voice_data.wav")
inputs = np.array(a[1], dtype=float)
inputs
len(inputs)
176400/44100
DURATION = 4

#Need the sample rate, and duration of recording
#       N = sample_rate * duration

from scipy.fft import rfft, rfftfreq

SAMPLE_RATE = 44100
N = SAMPLE_RATE * DURATION

yf = rfft(inputs)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

# !!!!!!!!!!!!!!!!!!!!!
  """running xf now crashes my computer
  I have no idea why, but it just does
  I can't finish the project. Maybe 
  because I installed CUDA/NVIDIA on
  my computer.
  """
 
# My natural range is A#3 - C4.
     #233.08 - 261.63

plt.plot(xf, np.abs(yf))
#Where the middle ground is
line1 = plt.axvline(x=233.08, color='r', linestyle='-')
plt.show()

"""
Okay, so I have the graph with the the frequencies
and a line that is my natrual speaking tone. I 
I need to get rid of any xf frequencies that don't 
go above a certain volume (yf) threshold. yf 
values are calculated using np.abs. It adds 
a real number with a complex number like 3j. j is 
an imaginary number like square root of -1.
All I have to do is make a threshold an arbitrary
threshold and automatically get rid of any xf values
that don't make it. 
"""

#Now get the unique frequencies

""" Step 3: Setting up the network
It will be a binary classification network with
0 hidden layers and 1 output neuron. I will
use Binary Cross Entropy as my loss function
and Sigmoid as my output activation function.

The target will be 1 and bias will be random.

Update: I might not even need a neural network.
I could just get a list of frequencies of my voice 
and compare them to frequencies of other people.
I could just make a list of someone's voice and
compare it to mine. I could then match them 
and have a % comparison.

Test this with my brothers and see how the 
vocal frequencies work.

Update 2: Just realized that almost any 
recording will have these frequencies in them.
My recording had over 80000 numbers. They definitly
have my vocal range in them. I need to find a way to 
distinquish when I talk vs when I don't.
Maybe based on intensity and volume
"""

#inputs = unique frequencies list
inputs = len('my_voice_data.wav')

w = np.array(np.random.uniform(np.random.randn(), np.random.randn(), len(inputs)))
bias = np.random.randn()
target = 1

#Sigmoid function
def sigmoid(z):
    return 1 / (1+np.exp(-z))

#dot product for neural network
def nn(x,w):
    return sigmoid(x.dot(w.T))

#prediction of nn.
def nn_predict(x,w):
    return np.around(nn(x,w))

#loss function
def loss(y, t):
    return - np.mean(
        np.multiply(t, np.log(y)) + np.multiply((1-t), np.log(1-y)))

""" Get gradients to change weights """
def gradient(w, x, t):
    """Gradient function."""
    return (nn(x, w) - t).T * x

def delta_w(w_k, x, t, learning_rate):
    """Update function which returns the update for each 
    weight {w_a, w_b} in a vector."""
    return learning_rate * gradient(w_k, x, t)      

learning_rate = 0.05

# Start the gradient descent updates and plot the iterations
nb_of_iterations = 100  # Number of gradient descent updates
w_iter = [w]
w  # List to store the weight values over the iterations
for i in range(nb_of_iterations):
    dw = delta_w(w, inputs, target, learning_rate)  # Get the delta w update
    w = w - dw  # Update the weights
    w_iter.append(w)  # Store the weights for plotting
w
len(w)
z = np.dot(inputs, weights) + 1


""" Now I just need to write a function that can read the voice
in real-time, extract the input numbers, run dot product, then 
logistic regression. I should do it so if the sigmoid is < 0.95 or
something, the AI will not run. """

def dot(inputs, weights):
    z = np.dot(inputs, weights)
    check_voice(z)

def check_voice(z):
    prediction = 1 / (1 + np.exp(-z))
    while 1:
        if prediction < 0.95:
            speak("You are not my master, you do not have authorization of my programming.")
            break
        else:
            takeCommand()

'https://realpython.com/python-scipy-fft/'
'https://peterroelants.github.io/posts/neural-network-implementation-part02/'
