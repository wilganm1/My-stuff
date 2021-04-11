#How will we handle changing tuning? 
#Just reuse the note changing code and assign it to tuning

def tune():
    while True:
        tunings = {'standard' : ["E","A","D","G","B","E"],  #Dictionary must be before input
                   'drop d' : ["D","A","D","G","B","E"],
                   'd Standard' : ['D','G','C','F','A','D'],
                   'drop c' : ['C','G','C','F','A','D'],
                   'c standard' : ["C","F","Bb","Eb","G","C"]}
        
        strings = {'1' : 'st', 
                   '2' : 'nd', 
                   '3' : 'rd',
                   '4' : 'th', 
                   '5' : 'th', 
                   '6' : 'th'}
                  
        notes = ["Ab","A","Bb","B","C","Db","D","Eb","E","F","Gb","G"]
        tuning = str(input("Choose desired tuning (space-sensitive, not case-sensitive):\nStandard, Drop D, D Standard, Drop C, C Standard\n: "))  #Chooses what tuning you want
        tuning = tuning.lower()    #turns 
        
        string = 0
        j = 0                           #for printing 1st string, 2nd string, etc
        for open_note in reversed(tunings[tuning]):
            string += 1
            zo = notes.index(open_note)   
            ad = notes[zo:]     
            ad.reverse()       
            del notes[zo:]    
            for i in ad:       
                notes.insert(0, i)
            j += 1
            print(str(notes) + " " + str(string) +  strings[str(j)] + " string")    
        new = input("Change tuning? (y/n): ")
        new = new.lower()
        if new == "y":
            continue
        else:
            break