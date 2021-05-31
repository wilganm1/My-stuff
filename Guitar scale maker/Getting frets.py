"""How will we handle changing tuning? 
Just reuse the note-changing code and assign it to tuning"""

notes = ["A","A#","B","C", "C#","D","D#","E","F","F#","G","G#"]
root = str(input("Enter one of the following notes (case-sensitive):\nA, A#, B, C, C#, D, D#, E, F, F#, G, G#\n: "))
r = 0 #The index of the note we pick that starts a scale
w = 2 #W & h are called "steps", or how many frets away one note is from another
h  =1 #A whole-step, w, is 2 frets, and a half-step, h, is one fret. 

scales = {'Major' : [r,w,w,h,w,w,w],
  'Minor' : [r,w,h,w,w,h,w],
  'Phrygian' : [r,h,w,w,w,h,w],
  'Lydian' : [r,w,w,w,h,w,w],
  'Mixolydian' : [r,w,w,h,w,w,h],
  'Dorian' : [r,w,h,w,w,w,h],
  'Locrian' : [r,h,w,w,h,w,w]}

scale_type = str(input("Enter one of the following scales (not case-sensitive):\nMajor, Minor, Phrygian, Lydian, Mixolydian, Dorian, Locrian\n: "))
    
                
global note_list
note_list = []   #Empty list that will become our indices of notes
scale_index = 0   #Starting index so the root note will be first
scale = scales[scale_type] #Formula for the scale. r must be included
for i in scale:
    scale_index += i   #computes the indices from the values r, w, and h
    note_list.append(scale_index)  #Adds in index values. [0,...,12] 
    zo = notes.index(root)   #Accesses index of chosen root note
    ad = notes[zo:]     #Takes all notes from root index to the end
    ad.reverse()       #reverses the order of ad. You do this so they are added in correctly 
    del notes[zo:]    #delets notes at their indices from notes variable. 
    for i in ad:       #Loop that inserts the reversed ad variable. 
        notes.insert(0, i)  #Inserts in letters one at a time in correct order. Has all notes
    global this_scale
    this_scale = []      #New list that will be have our finished scale.
    for i in note_list:     #loops through the numbers in scale. Those number are index values
        this_scale.append(notes[i])   #adds in letters from notes variable that correspond to scale indices

tunings = {'Standard' : ["E","A","D","G","B","E"],  #Dictionary must be before input
           'Drop D' : ["D","A","D","G","B","E"],
           'D Standard' : ['D','G','C','F','A','D'],
           'Drop C' : ['C','G','C','F','A','D'],
           'C Standard' : ["C","F","A#","D#","G","C"]}

numbers = [0,1,2,3,4,5,6,7,8,9,10,11]
select = str(input("Select a tuning: "))
results = []
for open_note in reversed(tunings[select]):
    zo = notes.index(open_note)   
    ad = notes[zo:] 
    ad.reverse()
    del notes[zo:]    
    for i in ad:   
        notes.insert(0, i)
    a_list = []
    for oq in this_scale:
        if oq in notes:
            a_list.append(notes.index(oq))
    results.append(a_list)
for yha in results:
    yha.sort()    #Add in a few extra lines if you want to append the 12th fret.
for zzz in numbers:
    for qot in results:
        if zzz not in qot:
            qot.insert(zzz, "-")
for bng in results:
    print(bng)
    
