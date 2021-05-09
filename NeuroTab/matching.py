"""
I want to make a program that works via audio
fingerprinting. I want to play a note on guitar and
have the computer return what fret I played. To do this
I need an acoustic fingerprint. This is basically the
sound waves produced by a sound that is imprinted and 
saved. But I wonder if I can use a numpy array as the
archived fingerprint. I want to play a fret, and make
a function that will listen to the note, read it,
then check if it matches any archived note.
"""
import numpy as np
from scipy.io import wavfile
from playsound import playsound

#Test archive the numpy for the test file.
#6th string open note
playsound('testing.wav')
a = wavfile.read('testing.wav')
b = np.array(a[1], dtype = float)
print(b)
n = len(b)
range(n)

playsound('test10.wav')
x = wavfile.read('test10.wav')
y = np.array(x[1], dtype = float)
m = len(y)

playsound('10.wav')

"""
So I've tested the open notes on the 6th and 1st string.
Now I need a way for Python to return what fret
I'm playing. Since I can read every file as a matrix 
of thousands of arrays, I'm thinking of checking if
a certain number of arrays of a note I play matches 
the arrays in the matrix of the archived notes.

match = 0
for x in range(0,3551):  #Lesser range
    if y[x].all() == b[x].all():
        match +=1
print(match)
"""

test60 = wavfile.read('test60.wav')
test_60 = np.array(test60[1], dtype = float)
print(test_60)

matches = 0
for arrays in range(n):
    if test_60[arrays].all() == b[arrays].all():
        matches +=1
        
print(matches)

match_percentage = (3541/3551) * 100
print(match_percentage)  #99% match. 


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Range = (0, 3551)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


