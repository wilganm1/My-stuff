import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io.wavfile import read
from playsound import playsound
import numpy as np
import sys
import matplotlib
import glob


#Reading a wav file and getting its sound as an array
a = read('60.wav')    
b = np.array(a[1], dtype = float) #gets only array 
#np.set_printoptions(threshold=sys.maxsize)
   #Prints out all arrays. Don't do it.     
print(b)
print("Arrays in b: " + str(len(b)))


b[0]
print(b[0])

n = b[900]
n
print(n)
cvc = (b[0:5])
vcv = str(cvc)
print(cvc)

qet = []

cvc[0] 
cvc[0][:2]


input1 = cvc[0]
input1
print(input1)

qet = []
for item in cvc:
    for j in item:    #How can I automate list creation for every single array 
        qet.append(j)    #without having the word 'array'
print(qet)

n = len(b)
N = 5
list_test = [cvc[i][0:] for i in range(0, N)]

list_test
print(list_test)

qet = []
for i in list_test:
    qet.append(i)
print(qet)

"""
We need to automate variable creation for each wav
file. Can create a dictionary to do this.
"""

wav_list = []
path = "C:/Users/WilganZMT/Documents/Coding/Python/NeuroTab/wav files/"
for n in glob.glob(os.path.join(path, '*.wav')):
    wav_list.append(n)

len(wav_list)

string_and_fret_list = ([s.strip('C:/Users/WilganZMT/Documents/Coding/Python/NeuroTab/wav files\\') for s in wav_list])
wav_list = ([s.replace('C:/Users/WilganZMT/Documents/Coding/Python/NeuroTab/wav files\\', '') for s in wav_list])

global wav_list
global string_fret_list

print(string_and_fret_list)
print(wav_list)

print(string_and_fret_list[5][2]) #gets 0 from 510

print(wav_list[0])
print(wav_list[0][0])

"""
Need to loop it so that it starts with string 1, reads all 13
frets, then increases the string number by 1, then restarts
the fret loop.
Do this to create a dictionary for the arrays.
"""
#This will check if a wav file starts with a certain string number
for item in wav_list:    
    if item[0] == str(4):
        print('yes')
    else:
        print('no')
        
correct_list = [40,41,42,50,51,52,53,54,55,56,57,58,59,510,511,512,60,61,62,63,64,65,66,67,68,69,610,611,612]  #lists the wav file in correct order. 59, 510, 511 etc

string_list = [1,2,3,4,5,6]
fret_list = [0,1,2,3,4,5,6,7,8,9,10,11,12]       

wavs={}        #empty dictionary to fill later

for file in correct_list:  #This automatically saves dictionary keys as whatever you want. pics['2'] gives the 3rd value.
    for i in range(len(correct_list)):
        wavs[f"{i}"] = "C:/Users/WilganZMT/Documents/Coding/Python/NeuroTab/" + str(file) + ".wav"  
