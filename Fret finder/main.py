from tkinter import *

root = Tk()
root.title('Fret Finder')

counter = 0

''' Make frame 1 with all the dropdown menus '''
frame1 = Frame(master = root)

#Tuning choices
tuning_var = StringVar(root)
tuning_var.set('') # set the default option
tuning_choices = ['E Standard', 'Open E', 'Drop D', 'Double Drop D', 'D Standard', 
                  'Open D', 'Drop C#', 'Drop C', 'C# Standard', 'C Standard', 
                  'Open C', 'Drop B', 'B Standard', 'Open B', 'Drop A#', 
                  'Drop A', 'A# Standard', 'A Standard']
tuningMenu = OptionMenu(frame1, tuning_var, *tuning_choices)
Label(frame1, text='Select tuning').grid(row = 1, column = 1)
tuningMenu.grid(row=2, column=1)

#Root note choices
root_note_var = StringVar(root)
root_note_var.set('')
root_note_choices = ['A','A#','B','C', 'C#','D','D#','E','F','F#','G','G#']
rootNoteMenu= OptionMenu(frame1, root_note_var, *root_note_choices)
Label(frame1, text='Select root note').grid(row=1, column = 2)
rootNoteMenu.grid(row=2, column=2)

#Scale choices
scale_var = StringVar(root)
scale_var.set('')
scale_choices = ['Major', 'Minor', 'Phrygian', 'Lydian', 'Mixolydian', 'Dorian', 'Locrian',
                 'Harmonic Minor', 'Melodic Minor', 'Major Pentatonic', 'Minor Pentatonic']
scaleMenu = OptionMenu(frame1, scale_var, *scale_choices)
Label(frame1, text='Select scale').grid(row=1, column = 3)
scaleMenu.grid(row=2, column=3)

frame1.pack()

''' Make frame 2 with the button '''
frame2 = Frame(master = root) 

# Create button, it will change all label text
button = Button(frame2 , text = 'Get', command=lambda:[ioq(),mqs()]).pack()
  
frame2.pack()

''' Make frame 3 with the grid for the frets'''
frame3 = Frame(master = root)

''' This function will show all the correct frets based on the chosen scale for each string in each tuning '''
def ioq():
    for i in range(0, 6): #strings. Rows.
        for j in range(0, 25):  #frets. Columns
            frame3.columnconfigure(j, weight=1)
            frame3.rowconfigure(j, weight=1)
            frame = Frame(     
            master=frame3,
            relief=RAISED,
            borderwidth=1
            )
            frame.grid(row=i, column=j, padx=2, pady=2)
            label = Label(master=frame)
            notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
            root = root_note_var.get()  #This is will be whatever you pick from the dropdown
            r = 0 #The index of the note we pick that starts a scale
            w = 2 #W & h are called 'steps', or how many frets away one note is from another
            h = 1 #A whole-step, w, is 2 frets, and a half-step, h, is one fret. 
            m= 3 #A whole-half step. 3 frets away. Also called minor third
            scales = {'Major' : [r,w,w,h,w,w,w],
              'Minor' : [r,w,h,w,w,h,w],
              'Phrygian' : [r,h,w,w,w,h,w],
              'Lydian' : [r,w,w,w,h,w,w],
              'Mixolydian' : [r,w,w,h,w,w,h],
              'Dorian' : [r,w,h,w,w,w,h],   
              'Locrian' : [r,h,w,w,h,w,w],
              'Harmonic Minor' : [r,w,h,w,w,h,m],
              'Melodic Minor' : [r,w,h,w,w,w,w],
              'Major Pentatonic' : [r,w,w,m,w],
              'Minor Pentatonic' : [r,m,w,w,m]}
            scale_type = scale_var.get()
            note_list = []   #Empty list that will become our indices of notes
            scale_index = 0   #Starting index so the root note will be first
            scale = scales[scale_type] #Formula for the scale. r must be included
            for akj in scale:
                scale_index += akj   #computes the indices from the values r, w, h, & wh
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
            '''  This is the tuning dictionary. Add in more if you'd like. The letters are the open notes. '''
            tunings = {'E Standard' : ['E','A','D','G','B','E'], 
                       'Open E' : ['E','B','E','G#','B','E'],
                       'Drop D' : ['D','A','D','G','B','E'],
                       'Double Drop D' : ['D','A','D','G','B','D'],
                       'D Standard' : ['D','G','C','F','A','D'],
                       'Open D' : ['D','A','D','F#','A','D'],
                       'Drop C#' : ['C#','G#','C#','F#','A#','D#'],
                       'Drop C' : ['C','G','C','F','A','D'],
                       'C# Standard' : ['C#','F#','B','E','G#','C#'],
                       'C Standard' : ['C','F','A#','D#','G','C'],
                       'Open C' : ['C','G','C','G','C','E'],
                       'Drop B' : ['B','F#','B','E','G#','C#'],
                       'B Standard' : ['B','E','A','D','F#','B'],
                       'Open B' : ['B','F#','B','F#','B','D#'],
                       'Drop A#' : ['A#','F','A#','D#','G','C'],
                       'A# Standard' : ['A#','D#','G#','C#','F','A#'],
                       'Drop A' : ['A','E','A','D','F#','B'],
                       'A Standard' : ['A','D','G','C','E','A']}
            numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]    #this is a reference for the list of frets. We come back to it later
            select = tuning_var.get()    #saves the tuning selection
            global results
            results = []    #This will eventually have 6 lists of frets.
            for open_note in reversed(tunings[select]):  #Reverse it so the 1st string is output first
                zo = notes.index(open_note)   #Get indices of the open_note in notes. notes has changed based on the root note picked
                ad = notes[zo:] 
                ad.reverse()
                del notes[zo:]    
                for ce in ad:   
                    notes.insert(0, ce)
                a_list = []
                for oq in this_scale:
                    if oq in notes:
                        a_list.append(notes.index(oq))  #Adds in correct fret for string
                results.append(a_list)  #Adds in a_list as a nested list
            for yha in results:  #Will go through every a_list for each string.
                yha.sort()    #Sorts frets in ascending order. 
            for qpr in results:
                length = int(len(qpr))
                for k in range(length):
                    qpr.append(qpr[k] + 12)
                if qpr[0] == 0:
                    qpr.append(24)
            for zzz in numbers:       #loops through the numbers variable
                for qot in results:     #loops through each a_list in results
                    if zzz not in qot:     #loops through every fret in each a_list. checks if a number in numbers is not in the list
                        qot.insert(zzz, '-') #inserts '-' into the place where a number is missing. Doing this allows us to display the list in tkinter
            label.configure(text = results[i][j], font = 4)    #mathces up the correct fret for each grid in tkinter.
            label.pack(padx=2, pady=2) 
frame3.pack()
frame4 = Frame(master = root)

''' Now create a canvas to draw the neck diagram '''
canvas = Canvas(frame4, width = 530,height = 95)

def mqs():
    canvas.delete("all")
    """ Adding canvas.delete("all") updates the dots 
    but it also deletes the neck diagram. I think this 
    is because it deletes the canvas that was made
    before the delete() function is called.
    That's why the dots stay even though 
    they have the same canvas name. 
    I might just have to make the entire
    neck diagram after I delete it. 
    I tried just moving the neck code to the mqs 
    function but nothing shows up at all.
    """
    
    neck_length = 530
    fret_length = neck_length - 15
    
    """ Neck """
    canvas.create_rectangle(0,0, neck_length, 95,
                    outline="#5c3626", fill="#5c3626")
    """ Strings """
    for i in range(0,6):
        canvas.create_rectangle(0, (i*15)+10, neck_length, (i*15)+10)
    
    """ Frets """
    for fret in range(1,25):
         canvas.create_rectangle(fret * (fret_length/24), 10, (fret * (fret_length/24)), 85,
                outline = "#b8b0ad", fill = "#b8b0ad")
    
    """ Nut """
    canvas.create_rectangle(0,10,5,85,
            outline = "black", fill="black")
         
    """ Fret circles """ 
    for i in [3,5,7,9,15,17,19,21]: #Frets 3,5,7,9
        canvas.create_oval(((i-1)*(fret_length/24)) + 6.25, 42.5,
                           ((i-1)*(fret_length/24)) + 16.25, 52.5,
                           outline = "white", fill = "white")
            #Fret 12
    canvas.create_oval(11 * (fret_length/24) + 6.25, 27.5, 11 * (fret_length/24) + 16.25, 37.5,
                outline = "#f1f0f0", fill="#f1f0f0")  
    canvas.create_oval(11 * (fret_length/24) + 6.25, 57.5, 11 * (fret_length/24) + 16.25, 67.5,
                outline = "#f1f0f0", fill="#f1f0f0")
    
            #Fret 24
    canvas.create_oval(23 * (fret_length/24) + 6.25, 27.5, 23 * (fret_length/24) + 16.25, 37.5,
                outline = "#f1f0f0", fill="#f1f0f0")  
    canvas.create_oval(23 * (fret_length/24) + 6.25, 57.5, 23 * (fret_length/24) + 16.25, 67.5,
                outline = "#f1f0f0", fill="#f1f0f0")
    for io in range(len(results)):
        for ng in results[io]:
            if ng == 0:
                canvas.create_oval(
                    0,
                    ((io * 15) +10) -3,
                    6,
                    ((io * 15) +10) + 5,
                    outline = 'gray', fill='gray')
            if ng in range(1,6):
                canvas.create_oval(
                    (ng*(fret_length/24)) - 9,
                    ((io * 15) +10) -3,
                    (ng*(fret_length/24)) - 1,
                    ((io * 15) +10) + 5,
                    outline = 'green', fill='green')
            elif ng in range(6,11):
                canvas.create_oval(
                    (ng*(fret_length/24)) - 9,
                    ((io * 15) +10) -3,
                    (ng*(fret_length/24)) - 1,
                    ((io * 15) +10) + 5,
                    outline = 'steelblue', fill='steelblue')
            elif ng in range(11,16):
                canvas.create_oval(
                    (ng*(fret_length/24)) - 9,
                    ((io * 15) +10) -3,
                    (ng*(fret_length/24)) - 1,
                    ((io * 15) +10) + 5,
                    outline = 'red', fill='red')
            elif ng in range(16, 21):
                canvas.create_oval(
                    (ng*(fret_length/24)) - 9,
                    ((io * 15) +10) -3,
                    (ng*(fret_length/24)) - 1,
                    ((io * 15) +10) + 5,
                    outline = 'violet', fill='violet')
            elif ng in range(21, 25):
                canvas.create_oval(
                    (ng*(fret_length/24)) - 9,
                    ((io * 15) +10) -3,
                    (ng*(fret_length/24)) - 1,
                    ((io * 15) +10) + 5,
                    outline = 'orange', fill='orange')
    canvas.pack()
frame4.pack()
root.mainloop()
