#How will we handle changing tuning? 
#Just reuse the note changing code and assign it to tuning

def tune():
    while True:
        tunings = {'standard' : ["E","A","D","G","B","E"],  #Dictionary for the open notes of the six strings for various tunings.
                   'drop d' : ["D","A","D","G","B","E"],    #On a six-string guitar, an open note is like fret zero. You don't press down on any fret.
                   'd Standard' : ['D','G','C','F','A','D'],    #Certain tunings have specific open notes. That's how we label tunings.
                   'drop c' : ['C','G','C','F','A','D'],         #Since there are six notes, that means there are six strings, which are all looped through
                   'c standard' : ["C","F","Bb","Eb","G","C"]}   #Doing this we get all 12 notes in the correct order for all 6 strings
        
        strings = {'1' : 'st',     #This dictionary is about labeling the arrays which the correct notes.
                   '2' : 'nd', 
                   '3' : 'rd',     #We use variable j for this. 
                   '4' : 'th', 
                   '5' : 'th', 
                   '6' : 'th'}
                  
        notes = ["Ab","A","Bb","B","C","Db","D","Eb","E","F","Gb","G"]      #All 12 notes that exist in chromatic scale.
        tuning = str(input("Choose desired tuning (space-sensitive, not case-sensitive):\nStandard, Drop D, D Standard, Drop C, C Standard\n: "))  #Chooses what tuning you want
        tuning = tuning.lower()    #lowercase the tuning variable to be matched to dictionary
        
        string = 0    #create this so that each string is looped through later.
        j = 0      #for printing 1st string, 2nd string, etc
        for open_note in reversed(tunings[tuning]):   #This reverses the order of notes in the dictionary key. The last letter is printed first. Format = guitar tab
            string += 1    #increases the strings 
            zo = notes.index(open_note)     
            ad = notes[zo:]     #extracts the notes from the given index to the end of the arry
            ad.reverse()        #reverses the notes so they are added in the correct order later
            del notes[zo:]     #deletes the ad array from the original notes array.
            for i in ad:       
                notes.insert(0, i)    #adds the selected ad notes back into the notes array. 
            j += 1
            print(str(notes) + " " + str(string) +  strings[str(j)] + " string")    #prints out the 6 correct array of notes for each string with proper labels.
        new = input("Change tuning? (y/n): ")   #asks if you want to repeat it
        new = new.lower()   
        if new == "y":      #saying 'y' repeats the entire process
            continue
        else:
            break
