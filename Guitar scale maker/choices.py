from tkinter import *

root = Tk()
root.title("Tk dropdown example")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack()

# Create Tkinter variables
tuning_var = StringVar(root)
root_note_var = StringVar(root)
scale_var = StringVar(root)

# Dictionary with tunings
tuning_choices = ['Standard', 'Drop D', 'D Standard', 'Drop C', 'C Standard']
tuning_var.set('') # set the default option

tuningMenu = OptionMenu(mainframe, tuning_var, *tuning_choices)
Label(mainframe, text="Select tuning").grid(row = 1, column = 1)
tuningMenu.grid(row=2, column=1)

#Dictionary with root note options
root_note_choices = ["Ab","A","Bb","B","C","Db","D","Eb","E","F","Gb","G"]
root_note_var.set('')

rootNoteMenu= OptionMenu(mainframe, root_note_var, *root_note_choices)
Label(mainframe, text="Select root note").grid(row=1, column = 2)
rootNoteMenu.grid(row=2, column=2)

# Dictionary with scales
scale_choices = ["Major", "Minor", "Phrygian", 'Lydian', "Mixolyidan", 'Dorian', "Locrian"]
scale_var.set('')

scaleMenu = OptionMenu(mainframe, scale_var, *scale_choices)
Label(mainframe, text="Select scale").grid(row=1, column = 3)
scaleMenu.grid(row=2, column=3)



root.mainloop()
