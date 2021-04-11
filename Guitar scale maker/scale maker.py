#Want to make a program that can auto-write 
#music scales of any note in the 7 standard
#musical scales

#later make a gui that displays this is neat fashion
    
def music():
    
#I want it so if you input a wrong note or scale it will loop back until you input a correct one
    
    while True:       #Main loop that encompasses everything. Starting point at every loop
        while True:      #Loop that checks if a correct note is entered
            notes = ["Ab","A","Bb","B","C","Db","D","Eb","E","F","Gb","G"]
            root = str(input("Enter one of the following notes (case-sensitive):\nAb, A, Bb, B, C, Db, D, Eb, E, F, Gb, G\n: "))
            if root not in notes:
                print("Error! Please enter a valid note")
                continue
            else:
                break
        
        while True:         #Loop that checks if a correct scale is entered
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
            
        while True:      
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
                this_scale = []      #New list that will be have our finished scale.
                for i in note_list:     #loops through the numbers in scale. Those number are index values
                    this_scale.append(notes[i])   #adds in letters from notes variable that correspond to scale indices
            print("\n" + str(root) + " " + str(scale_type) + "\n" + str(this_scale))  #prints completed scale in the correct order
            new = input("Get a new scale? (y/n): ")    #asks if you want to restart loop for new scale
            break
            if new == "y":
                continue
            else:
                break
        if new != "y":
            break

