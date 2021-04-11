#Want to make a program that can auto-write 
#music scales of any note in the 7 standard
#musical scales

#later make a gui that displays this is neat fashion
    
def music():
    
    while True:
        
        notes = ["Ab","A","Bb","B","C","Db","D","Eb","E","F","Gb","G"]
        root = str(input("Enter one of the following notes \nAb, A, Bb, B, C, Db, D, Eb, E, F, Gb, G\n: "))
        
        if root not in notes:
            print("Error! Did not enter valid note. Please enter a valid note.")
            continue
        
        r = 0 #The index of the note we pick that starts a scale
        w = 2 #W & h are called "steps", or how many frets away one note is from another
        h  =1 #A whole-step, w, is 2 frets, and a half-step, h, is one fret. 
        
        scales = ["major", "minor", "phrygian", "dorian", "lydian", "mixolydian", "locrian"]     
        scale_type = str(input("Enter one of the following scales\nmajor, dorian, phrygian, lydian, mixolydian, minor, locrian\n: "))
              
        if scale_type not in scales:
            print("Error! Did not enter a valid scale. Please enter a valid scale.")
            continue
        
        if scale_type == "minor":  
            scale = []   #Empty list that will become our indices of notes
            scale_index = 0   #Starting index so the root note will be first
            minor_scale = [r,w,h,w,w,h,w] #Formula for the scale. r must be included
            for i in minor_scale:
                scale_index += i   #computes the indices from the values r, w, and h
                scale.append(scale_index)  #Adds in index values. [0,...,12] 
                zo = notes.index(root)   #Accesses index of chosen root note
                ad = notes[zo:]     #Takes all notes from root index to the end
                ad.reverse()       #reverses the order of ad. You do this so they are added in correctly 
                del notes[zo:]    #delets notes at their indices from notes variable. 
                for i in ad:       #Loop that inserts the reversed ad variable. 
                    notes.insert(0, i)  #Inserts in letters one at a time in correct order. Has all notes
                this_scale = []      #New list that will be have our finished scale.
                for i in scale:     #loops through the numbers in scale. Those number are index values
                    this_scale.append(notes[i])   #adds in letters from notes variable that correspond to scale indices
            print(str(this_scale) + str(root + " " + scale_type))  #prints completed scale in the correct order
            new = input("Get a new scale? (y/n): ")    #asks if you want to restart loop for new scale
            if new == "y":
                continue
            else:
                break        
        
        elif scale_type == "major":
            scale = []
            scale_index = 0
            major_scale = [r,w,w,h,w,w,w]
            for i in major_scale:
                scale_index += i
                scale.append(scale_index)
                zo = notes.index(root)
                ad = notes[zo:]
                ad.reverse()
                del notes[zo:]
                for i in ad:
                    notes.insert(0, i) 
                this_scale = []
                for i in scale:
                    this_scale.append(notes[i])
            print(str(this_scale) + str(root + " " + scale_type)) 
            new = input("Get a new scale? (y/n): ")
            if new == "y":
                continue
            else:
                break
        
        elif scale_type == "dorian":
            scale = []
            scale_index = 0
            dorian_scale = [r,w,h,w,w,w,h]
            for i in dorian_scale:
                scale_index += i
                scale.append(scale_index)
                zo = notes.index(root)
                ad = notes[zo:]
                ad.reverse()
                del notes[zo:]
                for i in ad:
                    notes.insert(0, i) 
                this_scale = []
                for i in scale:
                    this_scale.append(notes[i])
            print(str(this_scale) + str(root + " " + scale_type)) 
            new = input("Get a new scale? (y/n): ")
            if new == "y":
                continue
            else:
                break
        
        elif scale_type == "phrygian":
            scale = []
            scale_index = 0
            phrygian_scale = [r,h,w,w,w,h,w]
            for i in phrygian_scale:
                scale_index += i
                scale.append(scale_index)
                zo = notes.index(root)
                ad = notes[zo:]
                ad.reverse()
                del notes[zo:]
                for i in ad:
                    notes.insert(0, i) 
                this_scale = []
                for i in scale:
                    this_scale.append(notes[i])
            print(str(this_scale) + str(root + " " + scale_type)) 
            new = input("Get a new scale? (y/n): ")
            if new == "y":
                continue
            else:
                break
        
        elif scale_type == "lydian":
            scale = []
            scale_index = 0
            lydian_scale = [r,w,w,w,h,w,w]
            for i in lydian_scale:
                scale_index += i
                scale.append(scale_index)
                zo = notes.index(root)
                ad = notes[zo:]
                ad.reverse()
                del notes[zo:]
                for i in ad:
                    notes.insert(0, i) 
                this_scale = []
                for i in scale:
                    this_scale.append(notes[i])
            print(str(this_scale) + str(root + " " + scale_type)) 
            new = input("Get a new scale? (y/n): ")
            if new == "y":
                continue
            else:
                break
        
        elif scale_type == "mixolydian":
            scale = []
            scale_index = 0
            mixolydian_scale = [r,w,w,h,w,w,h]
            for i in mixolydian_scale:
                scale_index += i
                scale.append(scale_index)
                zo = notes.index(root)
                ad = notes[zo:]
                ad.reverse()
                del notes[zo:]
                for i in ad:
                    notes.insert(0, i) 
                this_scale = []
                for i in scale:
                    this_scale.append(notes[i])
            print(str(this_scale) + str(root + " " + scale_type)) 
            new = input("Get a new scale? (y/n): ")
            if new == "y":
                continue
            else:
                break
        
        elif scale_type == "locrian":
            scale = []
            scale_index = 0
            locrian_scale = [r,h,w,w,h,w,w]
            for i in locrian_scale:
                scale_index += i
                scale.append(scale_index)
                zo = notes.index(root)
                ad = notes[zo:]
                ad.reverse()
                del notes[zo:]
                for i in ad:
                    notes.insert(0, i) 
                this_scale = []
                for i in scale:
                    this_scale.append(notes[i])
            print(str(this_scale) + str(root + " " + scale_type)) 
            new = input("Get a new scale? (y/n): ")
            if new == "y":
                continue
            else:
                break
            
music()
