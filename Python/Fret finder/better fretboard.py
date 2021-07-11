from tkinter import *

root = Tk()

frame4 = Frame(master = root)

""" Make a fretboard that spans the width of the 
root frame. Then put in strings and frets and nut. """
canvas = Canvas(frame4, width = 600,
                height = 95)

neck_length = 600
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
    canvas.create_oval(((i-1)*(fret_length/24)) + 7.5, 42.5,
                       ((i-1)*(fret_length/24)) + 17.5, 52.5,
                       outline = "white", fill = "white")
        #Fret 12
canvas.create_oval(11 * (fret_length/24) + 7.5, 27.5, 11 * (fret_length/24) + 17.5, 37.5,
            outline = "#f1f0f0", fill="#f1f0f0")  
canvas.create_oval(11 * (fret_length/24) + 7.5, 57.5, 11 * (fret_length/24) + 17.5, 67.5,
            outline = "#f1f0f0", fill="#f1f0f0")

        #Fret 24
canvas.create_oval(23 * (fret_length/24) + 7.5, 27.5, 23 * (fret_length/24) + 17.5, 37.5,
            outline = "#f1f0f0", fill="#f1f0f0")  
canvas.create_oval(23 * (fret_length/24) + 7.5, 57.5, 23 * (fret_length/24) + 17.5, 67.5,
            outline = "#f1f0f0", fill="#f1f0f0")

    
""" Problem:
    The actual circles don't update. Instead of the circles changing, 
    the program just adds in another fretboard. So everytime you click the
    "Get" button it adds a new fretboard. Need to find a way to fix that.

    I added in a canvas.delete('all') function which got rid of the fret board
    but does update the dots. 
    
    I need to simutaneously delete the dots then update it.
    """
  
for io in range(len(results)):
    for ng in results[io]:
        if ng == 0:
            canvas.create_oval(
                0,((io * 15) +10) -3,
                8,((io * 15) +10) + 5,
                outline = 'gray', fill='gray')
        elif ng != '-' and ng in range(1,6):
            canvas.create_oval(
                (ng*(fret_length/24)) - 9,
                ((io * 15) +10) -3,
                (ng*(fret_length/24)) - 1,
                ((io * 15) +10) + 5,
                outline = 'green', fill='green')
        elif ng != '-' and ng in range(6,11):
            canvas.create_oval(
                (ng*(fret_length/24)) - 9,
                ((io * 15) +10) -3,
                (ng*(fret_length/24)) - 1,
                ((io * 15) +10) + 5,
                outline = 'blue', fill='blue')
        elif ng != '-' and ng in range(11,16):
            canvas.create_oval(
                (ng*(fret_length/24)) - 9,
                ((io * 15) +10) -3,
                (ng*(fret_length/24)) - 1,
                ((io * 15) +10) + 5,
                outline = 'red', fill='red')
        elif ng != '-' and ng in range(16, 21):
            canvas.create_oval(
                (ng*(fret_length/24)) - 9,
                ((io * 15) +10) -3,
                (ng*(fret_length/24)) - 1,
                ((io * 15) +10) + 5,
                outline = 'violet', fill='violet')
        elif ng != '-' and ng in range(21, 25):
            canvas.create_oval(
                (ng*(fret_length/24)) - 9,
                ((io * 15) +10) -3,
                (ng*(fret_length/24)) - 1,
                ((io * 15) +10) + 5,
                outline = 'orange', fill='orange')
canvas.pack()

frame4.pack()

root.mainloop()                  
