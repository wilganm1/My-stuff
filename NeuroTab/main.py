"""
I want to make an auto-tab writer software. 
I want to play a note on guitar and have the computer 
return what fret I played through Python code, To do this 
I need an acoustic fingerprint. This is basically the
sound waves produced by a sound that is imprinted and 
saved somewhere. But I wonder if I can use a numpy array as the
archived fingerprint. I want to play a fret, and make
a function that will listen to the note, read it,
then check if it matches any archived note. If it does match
I want Python to return what fret it is.
"""
from scipy.io import wavfile
import numpy as np

Step 1. Setup:
    a. Save all the wav files into a dictionary
        Frets = {'strings' : {'1' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                              '2' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                              '3' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                              '4' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                              '5' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                              '6' : [0,1,2,3,4,5,6,7,8,9,10,11,12]}}
        string_number = 1     #starts with first string. First string in dictionary
        while string_number < 7:   #Since there's only 6 strings loop will terminate terminate.
            fret_number = 0     #Starts at fret zero. Also index 0. Restarts at 0.
            while fret_number < 13:   #This will make it so it goes through every fret of each string. 
                Frets['strings'][str(string_number)][fret_number] = str(string_number)+str(fret_number)+'.wav'  #by giving the dictionary numbers in '' it allows me to assign them in loops
                fret_number +=1  #increments fret by one.
                continue        #restarts the inner loop with a + 1 fret
            string_number +=1 #after you hit fret 12 the string number increases by 1 
            continue  #outer loop restarts with +1 string and fret back to zero.
            
    b. Get all numpy matrix arrays for each wav file. Save them into their own dictionary
        Arrays = {'strings' : {'1' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                               '2' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                               '3' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                               '4' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                               '5' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
                               '6' : [0,1,2,3,4,5,6,7,8,9,10,11,12]}}
        string_number = 1     
        while string_number < 7:   
            fret_number = 0    
            while fret_number < 13:  
                x = wavfile.read(Frets['strings'][str(string_number)][fret_number])
                y = np.array(x[1], dtype = float)
                Arrays['strings'][str(string_number)][fret_number] = y 
                fret_number +=1  
                continue        
            string_number +=1 
            continue
    
Step 2. Recording:
    a. Write a function that will record audio. Play guitar into it.
            import sounddevice as sd
            import time
            
            global fs
            fs = 44100  # Sample rate
            global seconds
            seconds = 2  # Duration of recording
            #Now for the countdown
            secs = 5   #countdown time
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
    b. Remove all silence and white noise.
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
        
Step 3. Matching and identification:
    a. Write a function to match the numpy array from the recorded sound to an array that is saved
         within the Recordings dictionary.     