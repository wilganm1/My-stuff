from tkinter import *

root = Tk()
''' Make frame 1 with all the buttons '''
frame1 = Frame(master = root, width = 200, height = 100)

#Tuning choices
tuning_var = StringVar(root)

tuning_choices = ['Standard', 'Drop D', 'D Standard', 'Drop C', 'C Standard']
tuning_var.set('') # set the default option

tuningMenu = OptionMenu(frame1, tuning_var, *tuning_choices)
Label(frame1, text="Select tuning").grid(row = 1, column = 1)
tuningMenu.grid(row=2, column=1)

#Root note choices
root_note_var = StringVar(root)

root_note_choices = ["A","A#","B","C", "C#","D","D#","E","F","F#","G","G#"]
root_note_var.set('')

rootNoteMenu= OptionMenu(frame1, root_note_var, *root_note_choices)
Label(frame1, text="Select root note").grid(row=1, column = 2)
rootNoteMenu.grid(row=2, column=2)

#Scale choices
scale_var = StringVar(root)

scale_choices = ["Major", "Minor", "Phrygian", 'Lydian', "Mixolydian", 'Dorian', "Locrian"]
scale_var.set('')

scaleMenu = OptionMenu(frame1, scale_var, *scale_choices)
Label(frame1, text="Select scale").grid(row=1, column = 3)
scaleMenu.grid(row=2, column=3)

frame1.pack()

""" Make frame 2 with the button """
frame2 = Frame(master = root) 
def scl():        #This shows the root note and the scale when button pressed
    label2.config(text = tuning_var.get() + " - " + root_note_var.get() + " " + scale_var.get())

# Create button, it will change all label text
button = Button(frame2 , text = "Get", command=lambda:[scl(), ioq()]).pack()
label2 = Label(frame2 , text = " ")
label2.pack()
  
frame2.pack()

''' Make frame 3 with the grid '''
frame3 = Frame(master = root)

""" This function will show all the correct frets based on the chosen scale for each string in each tuning """
def ioq():
    for i in range(0, 6): #strings. Rows.
        for j in range(0, 12):  #frets. Columns
            frame3.columnconfigure(j, weight=1)
            frame3.rowconfigure(j, weight=1)
            frame = Frame(     
            master=frame3,
            relief=RAISED,
            borderwidth=1
            )
            frame.grid(row=i, column=j, padx=2, pady=2)
            label = Label(master=frame)
            notes = ["A","A#","B","C", "C#","D","D#","E","F","F#","G","G#"]
            root = root_note_var.get()
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
            scale_type = scale_var.get()
            note_list = []   #Empty list that will become our indices of notes
            scale_index = 0   #Starting index so the root note will be first
            scale = scales[scale_type] #Formula for the scale. r must be included
            for akj in scale:
                scale_index += akj   #computes the indices from the values r, w, and h
                note_list.append(scale_index)  #Adds in index values. [0,...,12] 
                zo = notes.index(root)   #Accesses index of chosen root note
                ad = notes[zo:]     #Takes all notes from root index to the end
                ad.reverse()       #reverses the order of ad. You do this so they are added in correctly 
                del notes[zo:]    #delets notes at their indices from notes variable. 
                for eipq in ad:       #Loop that inserts the reversed ad variable. 
                    notes.insert(0, eipq)  #Inserts in letters one at a time in correct order. Has all notes
                global this_scale
                this_scale = []      #New list that will be have our finished scale.
                for hhq in note_list:     #loops through the numbers in scale. Those number are index values
                    this_scale.append(notes[hhq])   #adds in letters from notes variable that correspond to scale indices
            
            tunings = {'Standard' : ["E","A","D","G","B","E"],  #Dictionary must be before input
                       'Drop D' : ["D","A","D","G","B","E"],
                       'D Standard' : ['D','G','C','F','A','D'],
                       'Drop C' : ['C','G','C','F','A','D'],
                       'C Standard' : ["C","F","A#","D#","G","C"]}
            
            numbers = [0,1,2,3,4,5,6,7,8,9,10,11]
            select = tuning_var.get()
            results = []
            for open_note in reversed(tunings[select]):
                zo = notes.index(open_note)   
                ad = notes[zo:] 
                ad.reverse()
                del notes[zo:]    
                for ce in ad:   
                    notes.insert(0, ce)
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
            label.configure(text = results[i][j])
            label.pack(padx=2, pady=2) 
            
frame3.pack()
root.mainloop()

