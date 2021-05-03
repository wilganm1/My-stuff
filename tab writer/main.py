import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io.wavfile import read
from playsound import playsound
import numpy as np
import sys

"""
Goal: Make an automated tab writer using a 
neural network that can detect sounds in real-time
and predict the notes played when it happens in 
real-time. 
"""

#Reading a wav file and getting its sound as an array
a = read('60.wav')    
b = np.array(a[1], dtype = float) #gets only array 
#np.set_printoptions(threshold=sys.maxsize)
   #Prints out all arrays. Don't do it.     
print(b)
print("Arrays in b: " + str(len(b)))

#Accesses the arrays in b variable
print(b[0])
print(b[1])
print(b[507776])

e = read('testing.wav')
f = np.array(e[1], dtype=float)
print(f)
print(len(f))

#8.05% percent of a second = 3551 arrays

#How we get recording things in real-time.
fs = 44100  # Sample rate
seconds = 4  # Duration of recording
print("Recording")

#this is the recording that happens
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1) 
sd.wait()  # Wait until recording is finished
print("Finished")

