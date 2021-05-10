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

#Test archive the numpy for the test file.
#6th string open note
playsound('testing.wav')
a = wavfile.read('testing.wav')
b = np.array(a[1], dtype = float)
b
print(b)

#Now to create a new list and append every value.


new_b = []
for array in b:
    for value in array:
        new_b.append(float(value))
len(new_b)
new_b = [item for item in new_b if abs(item) > 0.00009]
new_b.append(200)
len(new_b)
7094/2
new_b = np.reshape(new_b, (3547, 2))
new_b
print(new_b)
