import sounddevice as sd     #plays audio files
import time         #controls time
from scipy.io.wavfile import write  #write wav files


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
        my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)   #Mono recording in this.
        sd.wait()      # Wait until recording is finished
        write('' + str(the_string)+str(the_fret) + '.wav', fs, my_recording)
          # Store it in Array dictionary 
          # Now loop it
        restart = str(input("Record another? (y/n): "))
        if restart == 'y':
            continue
        else:
            break
