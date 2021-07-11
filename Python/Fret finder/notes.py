def get_notes():
    while True:  
     while True:      #Loop that checks if a correct note is entered
            notes = ["A","A#","B","C", "C#","D","D#","E","F","F#","G","G#"]
            root = str(input("Enter one of the following notes (case-sensitive):\nA, A#, B, C, C#, D, D#, E, F, F#, G, G#\n: "))
            if root not in notes:
                print("Error! Please enter a valid note")
                continue
            else:
                break      #Main loop that encompasses everything. Starting point at every loop
     while True:
         r = 0 #The index of the note we pick that starts a scale
         w = 2 #W & h are called "steps", or how many frets away one note is from another
         h = 1 #A whole-step, w, is 2 frets, and a half-step, h, is one fret. 
         wh= 3 #A whole-half step is 3 frets. This is used in unorthodox scales.
    
         scales = {'Major' : [r,w,w,h,w,w,w],
              'Minor' : [r,w,h,w,w,h,w],
              'Phrygian' : [r,h,w,w,w,h,w],
              'Lydian' : [r,w,w,w,h,w,w],
              'Mixolydian' : [r,w,w,h,w,w,h],
              'Dorian' : [r,w,h,w,w,w,h],
              'Locrian' : [r,h,w,w,h,w,w],
              'Harmonic Minor' : [r,w,h,w,w,h,wh,h],
              'Melodic Minor' : [r,w,h,w,w,w,w,h],
              'Major Pentatonic' : [r,w,w,wh,w,wh],
              'Minor Pentatonic' : [r,wh,w,w,wh,w]}
            
         scale_type = str(input("Enter one of the following scales (not case-sensitive):\nMajor, Minor, Phrygian, Lydian, Mixolydian, Dorian, Locrian\n: "))
        
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
             this_scale.append(this_scale[0])
         print("\n" + str(root) + " " + str(scale_type) + "\n" + str(this_scale))  #prints completed scale in the correct order
            
         global tuning_notes
         tuning_notes = {'Standard' : {1 : ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'],
                                  2 : ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#'],
                                  3 : ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
                                  4 : ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
                                  5 : ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
                                  6 : ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#']},
                    'Drop D' : {1 : ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'],
                               2 : ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#'],
                               3 : ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
                               4 : ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
                               5 : ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
                               6 : ['D', 'E#', 'E', 'F', 'G#', 'G', 'A#', 'A', 'B#', 'B', 'C', 'D#']},
                    'D Standard' : {1 : ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'DC'],
                                   2 : ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
                                   3 : ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E'],
                                   4 : ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
                                   5 : ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
                                   6 : ['D', 'E#', 'E', 'F', 'G#', 'G', 'A#', 'A', 'B#', 'B', 'C', 'D#']},
                    'Drop C' : {1 : ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'DC'],
                               2 : ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
                               3 : ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E'],
                               4 : ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
                               5 : ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
                               6 : ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']},
                    'C Standard' : {1 : ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
                                   2 : ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
                                   3 : ['D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D'],
                                   4 : ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A'],
                                   5 : ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E'],
                                   6 : ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']}}

         strings = {'1' :'st',
                   '2' : 'nd', 
                   '3' : 'rd',
                   '4' : 'th', 
                   '5' : 'th',
                   '6' : 'th'}
         tuning = str(input("Choose desired tuning (space-sensitive, not case-sensitive):\nStandard, Drop D, D Standard, Drop C, C Standard\n: ") )  #Chooses what tuning you want
        
         string = 1
         superscript = 1
         print('\n' + str(root) + ' ' + str(scale_type) + ' - ' + tuning + " tuning")
         for x in range(1,7):
             for y in tuning_notes[tuning][x]:
                 if y not in this_scale:
                     tuning_notes[tuning][x].remove(y)
             print(str(tuning_notes[tuning][x]) + ' ' + str(string) + strings[str(superscript)] + ' string')
             string +=1
             superscript += 1
         break
     restart = str(input("Restart? (y/n): "))
     if restart == 'y':
         continue
     else:
         print("Farewell")
         break
     break