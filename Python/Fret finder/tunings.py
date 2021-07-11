"""How will we handle changing tuning? 
Just reuse the note changing code and assign it to tuning"""

def tune():
    while True:
        tunings = {'Standard' : ["E","A","D","G","B","E"],  #Dictionary must be before input
                   'Drop D' : ["D","A","D","G","B","E"],
                   'D Standard' : ['D','G','C','F','A','D'],
                   'Drop C' : ['C','G','C','F','A','D'],
                   'C Standard' : ["C","F","Bb","Eb","G","C"]}
        
        strings = {'1' : 'st', 
                   '2' : 'nd', 
                   '3' : 'rd',
                   '4' : 'th', 
                   '5' : 'th', 
                   '6' : 'th'}
                  
        notes = ["Ab","A","Bb","B","C","Db","D","Eb","E","F","Gb","G"]
        tuning = str(input("Choose desired tuning (space-sensitive, not case-sensitive):\nStandard, Drop D, D Standard, Drop C, C Standard\n: "))  #Chooses what tuning you want
        
        string = 0
        j = 0            #for printing 1st string, 2nd string, etc
        for open_note in reversed(tunings[tuning]):
            string += 1
            zo = notes.index(open_note)   
            ad = notes[zo:] 
            ad.reverse()
            del notes[zo:]    
            for i in ad:       
                notes.insert(0, i)
            j += 1
            print((notes) + " " + str(string) +  strings[str(j)] + " string")  
        new = str(input("Change tuning? (y/n): "))
        new = new.lower()
        if new == "y":
            continue
        else:
            break