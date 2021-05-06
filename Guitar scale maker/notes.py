#This script combines the other two scripts to get the notes that are in the scale on each string. Next I'll have to make a GUI to show the notes themselves.

def scales():
    while True:  
     while True:      #Loop that checks if a correct note is entered
            notes = ["Ab","A","Bb","B","C","Db","D","Eb","E","F","Gb","G"]
            root = str(input("Enter one of the following notes (case-sensitive):\nAb, A, Bb, B, C, Db, D, Eb, E, F, Gb, G\n: "))
            if root not in notes:
                print("Error! Please enter a valid note")
                continue
            else:
                break      #Main loop that encompasses everything. Starting point at every loop
     while True:
         r = 0 #The index of the note we pick that starts a scale
         w = 2 #W & h are called "steps", or how many frets away one note is from another
         h  =1 #A whole-step, w, is 2 frets, and a half-step, h, is one fret. 
    
         scales = {'major' : [r,w,w,h,w,w,w],
              'minor' : [r,w,h,w,w,h,w],
              'phrygian' : [r,h,w,w,w,h,w],
              'lydian' : [r,w,w,w,h,w,w],
              'mixolydian' : [r,w,w,h,w,w,h],
              'dorian' : [r,w,h,w,w,w,h],
              'locrian' : [r,h,w,w,h,w,w]}
            
         scale_type = str(input("Enter one of the following scales (not case-sensitive):\nMajor, Minor, Phrygian, Lydian, Mixolydian, Dorian, Locrian\n: "))
         scale_type = scale_type.lower()
        
         if scale_type not in scales:
             print("Error! Please enter valid scale")
             continue
         else: 
             break
         break
                    
     while True:
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
         print("\n" + str(root) + " " + str(scale_type) + "\n" + str(this_scale))  #prints completed scale in the correct order
            
         tunings = {'standard' : {1 : ['E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb'],
                                 2 : ['B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb'],
                                 3 : ['G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb'],
                                 4 : ['D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db'],
                                 5 : ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'],
                                 6 : ['E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb']},
                   'd standard' : {1 : ['D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db'],
                                   2 : ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'],
                                   3 : ['F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E'],
                                   4 : ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'],
                                   5 : ['G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb'],
                                   6 : ['D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db']},
                   'drop c' : {1 : ['D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db'],
                               2 : ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'],
                               3 : ['F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E'],
                               4 : ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'],
                               5 : ['G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb'],
                               6 : ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']},
                   'drop d' : {1 : ['E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb'],
                               2 : ['B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb'],
                               3 : ['G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb'],
                               4 : ['D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db'],
                               5 : ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'],
                               6 : ['D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db']},
                   'c standard' : {1 : ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'],
                                   2 : ['G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb'],
                                   3 : ['Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D'],
                                   4 : ['Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A'],
                                   5 : ['F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E'],
                                   6 : ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']}  
        
         strings = {'1' : 'st',
                   '2' : 'nd', 
                   '3' : 'rd',
                   '4' : 'th', 
                   '5' : 'th',
                   '6' : 'th'}
         tuning = str(input("Choose desired tuning (space-sensitive, not case-sensitive):\nStandard, Drop D, D Standard, Drop C, C Standard\n: ") )  #Chooses what tuning you want
         tuning = tuning.lower()
        
         string = 1
         superscript = 1
         print('\n' + str(root) + ' ' + str(scale_type) + ' - ' + tuning + " tuning")
         for x in range(1,7):
             for y in tunings[tuning][x]:
                 if y not in this_scale:
                     tunings[tuning][x].remove(y)
             print(str(tunings[tuning][x]) + ' ' + str(string) + strings[str(superscript)] + ' string')
             string +=1
             superscript += 1
         break
     break
   
