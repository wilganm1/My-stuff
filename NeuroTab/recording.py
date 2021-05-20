"""
Step 1. Recording audio
    I need to record the frets. Do this is Python so it's 
    more accurate. Can always convert later.
    Get all 13 frets of the six strings.
    
    Make sure to wait half a second during the 
    recording so get a clear pluck
 """
import sounddevice as sd     #plays audio files
import time         #counts time
import numpy as np    
from scipy.io.wavfile import write  #write wav files
from scipy.io.wavfile import read   #read wav files

def record():
    while True:
        the_string = input("Enter string: ")
        the_fret = input("Enter fret: ")
        
        # Now for the countdown
        countdown = 5
        while countdown > 0:
            print(countdown)
            countdown -= 1
            time.sleep(1)
        print("Recording:")
        
        #This is for the recording part
        fs = 44100     # Sample rate
        seconds = 1     # Duration of recording
        my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()      # Wait until recording is finished
        write('' + str(the_string)+str(the_fret) + '.wav', fs, my_recording)
          # Store it in Array dictionary 
          # Now loop it
        restart = str(input("Record another? (y/n): "))
        if restart == 'y':
            continue
        else:
            break
"""
May 11 update:
    The wav file recorded in Audacity won't work.
    I must record everything in Python.
    The good news is that Python returns one single 
    long array that will make things easier
"""
