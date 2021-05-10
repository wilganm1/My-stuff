""""Now I need to see if I can record a sound and save it as a variable in 
dictionary in real-time, get its numpy arrays, then see if it matches with a matrix
of a wav file saved in the 'dictionary of wav files' file.
"""

import sounddevice as sd

global Recordings
Recordings = {'strings' : {'1' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                           '2' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                           '3' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                           '4' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                           '5' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                           '6' : [0,1,2,3,4,5,6,7,8,9,10,11,12]}}

global fs
fs = 44100  # Sample rate
global seconds
seconds = 1  # Duration of recording

myrecording = 0
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished

string_number = 1     
while string_number < 7:   
    fret_number = 0    
    while fret_number < 13:    
        Recordings['strings'][str(string_number)][fret_number] = myrecording  
        fret_number +=1  
        continue        
    string_number +=1 
    continue  


Arrays = {'strings' : {'1' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                       '2' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                       '3' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                       '4' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                       '5' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                       '6' : [0,1,2,3,4,5,6,7,8,9,10,11,12]}}
  
"""
I need to write a function that is a 
countdown to prepare for the recording.
"""
import sounddevice as sd
import time

global fs
fs = 44100  # Sample rate
global seconds
seconds = 2  # Duration of recording

secs = 5
while secs > 0:
    print(secs)
    secs -= 1
    time.sleep(1)
    if secs == 0:
        print("Recording:")        
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
record_time = 1
while seconds > 0:
    print(seconds)
    seconds -= 1
    time.sleep(1)
    if seconds == 0:
        print("Done")
sd.wait()  # Wait until recording is finished
