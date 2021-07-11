# sets the tuning
from tkinter import *

tunings = {'Standard' : ["E","A","D","G","B","E"],  #Dictionary must be before input
           'Drop D' : ["D","A","D","G","B","E"],
           'D Standard' : ['D','G','C','F','A','D'],
           'Drop C' : ['C','G','C','F','A','D'],
           'C Standard' : ["C","F","Bb","Eb","G","C"]}
root = Tk()

for i in range(6):
    frame = Frame(
    master=root,
    relief=RAISED,
    borderwidth=1
    )
    frame.grid(row=i, column=0)
for x in reversed(tunings['Drop C']):
    label = Label(master=frame, text=str(x))
    label.pack()

root.mainloop()