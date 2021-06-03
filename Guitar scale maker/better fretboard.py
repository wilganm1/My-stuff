from tkinter import *

root = Tk()

""" Make a fretboard that spans the width of the 
root frame. Then put in strings and frets and nut. """

canvas = Canvas(root, width = 510,
                height = 150)

neck_length = 480   #Arbitrary
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
for i in [3,5,7,9,15,17,19,21]: 
    canvas.create_oval(((i-1)*(fret_length/24)) + 6, 42.5,
                       ((i-1)*(fret_length/24)) + 16, 44.5 + height_radius,
                       outline = "white", fill = "white")
        #Fret 12
canvas.create_oval(218.5, 27.5, 228.5, 37.5,
            outline = "#f1f0f0", fill="#f1f0f0")  
canvas.create_oval(218.5, 57.5, 228.5, 67.5,
            outline = "#f1f0f0", fill="#f1f0f0")

        #Fret 24
canvas.create_oval(452, 27.5, 462, 37.5,
            outline = "#f1f0f0", fill="#f1f0f0")  
canvas.create_oval(452, 57.5, 462, 67.5,
            outline = "#f1f0f0", fill="#f1f0f0")
canvas.pack()

mainloop()                  
