"""
I need to remove silence from the 
matrix. Silene is recorded as 0.0000000 or 
3.645e-05. It is very small, like less
than 0.0000 so I need to delete them.

Make an empty list, then just append every single
value in each list in the array matrix. 
Then just reshape it back to its normal shape.
"""

import numpy as np
from scipy.io import wavfile
from playsound import playsound
#Test using the test file.
playsound('testing.wav')
a = wavfile.read('testing.wav')
b = np.array(a[1], dtype = float)
b
print(b)

#Now to create a new list and append every value.
wav_array = []
for array in b:
    for value in array:
        wav_array.append(float(value))
len(wav_array)
wav_array = [item for item in wav_array if abs(item) > 0.00009]
wav_array.append(200)
len(wav_array)
7094/2
wav_array = np.reshape(wav_array, (3547, 2))
wav_array
print(wav_array)
