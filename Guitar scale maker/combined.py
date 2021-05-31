from tkinter import *
from notes import get_notes

root = Tk()

''' Make frame 1 with all the buttons '''

frame1 = Frame(master = root, width = 200, height = 100)

# Dictionary with tunings
tuning_var = StringVar(root)

tuning_choices = ['Standard', 'Drop D', 'D Standard', 'Drop C', 'C Standard']
tuning_var.set('') # set the default option

tuningMenu = OptionMenu(frame1, tuning_var, *tuning_choices)
Label(frame1, text="Select tuning").grid(row = 1, column = 1)
tuningMenu.grid(row=2, column=1)

#Dictionary with root note options
root_note_var = StringVar(root)

root_note_choices = ["A","A#","B","C", "C#","D","D#","E","F","F#","G","G#"]
root_note_var.set('')

rootNoteMenu= OptionMenu(frame1, root_note_var, *root_note_choices)
Label(frame1, text="Select root note").grid(row=1, column = 2)
rootNoteMenu.grid(row=2, column=2)

# Dictionary with scales
scale_var = StringVar(root)

scale_choices = ["Major", "Minor", "Phrygian", 'Lydian', "Mixolydian", 'Dorian', "Locrian"]
scale_var.set('')

scaleMenu = OptionMenu(frame1, scale_var, *scale_choices)
Label(frame1, text="Select scale").grid(row=1, column = 3)
scaleMenu.grid(row=2, column=3)

frame1.pack()

""" Make frame 2 with button """

frame2 = Frame(master = root)
 
def scl():        #This shows the root note and the scale when button pressed
    label2.config(text = tuning_var.get() + " - " + root_note_var.get() + " " + scale_var.get())


# Create button, it will change label text
button = Button(frame2 , text = "Get", command=lambda:[scl(), ioq()]).pack()
label2 = Label(frame2 , text = " ")
label2.pack()
  
frame2.pack()

''' Make frame 3 with the grid '''

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
                'D Standard' : {1 : ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
                               2 : ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
                               3 : ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E'],
                               4 : ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
                               5 : ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
                               6 : ['D', 'E#', 'E', 'F', 'G#', 'G', 'A#', 'A', 'B#', 'B', 'C', 'D#']},
                'Drop C' : {1 : ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
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

frame3 = Frame(master = root)

""" This will show all the notes for each string in each tuning """

def ioq():
    for i in range(0, 6): #strings. Rows.
        for j in range(0, 12):  #frets. Columns
            frame3.columnconfigure(j, weight=1)
            frame3.rowconfigure(j, weight=1)
            frame = tk.Frame(     
            master=frame3,
            relief=tk.RAISED,
            borderwidth=1
            )
    
            frame.grid(row=i, column=j, padx=2, pady=2)
            label = tk.Label(master=frame)
            label.configure(text = tuning_notes[str(tuning_var.get())][i+1][j])
            label.pack(padx=2, pady=2) 
     
""" Fret row """
for p in range(0,12):
    frame3.columnconfigure(p, weight = 1)
    frame3.rowconfigure(p, weight = 1)
    frame = Frame(     
    master=frame3,
    relief=RAISED,
    borderwidth=1
    )

    frame.grid(row=6, column=p, padx=5, pady=5)
    label = Label(master=frame, text=str(p))
    label.pack(padx=2, pady=2) 

 
frame3.pack()
root.mainloop()

