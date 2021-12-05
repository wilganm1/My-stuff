""" I want to make a GUI that will display how a 
neural network works using circles and lines to 
represent nodes and weights. Also in the future try
to get it to update in real-time during backwards
propagation """

""" I want to make a Neural Network GUI for myself to visually represent how they work.

This will be small scale but I want to incorporate many things like being able to animate it
using the time package, change colors of the canvas, input your own inputs with csvs or just typing, 
and do complete backwards propagation. """


from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry('1200x800')


frame1 = tk.Frame(root)

input_label = tk.Label(frame1,
                       text = "Select number of inputs").grid(row=0, column = 0)
input_select = tk.Spinbox(frame1, from_ = 2, to = 8, width = 3, wrap = True)
input_select.grid(row = 1, column = 0)

output_label = tk.Label(frame1,
                       text = "Select number of outputs").grid(row=0, column = 2)
output_select = tk.Spinbox(frame1, from_ = 1, to = 6, width = 3, wrap = True)
output_select.grid(row = 1, column = 2)                                                             

frame1.pack()

frame2 = tk.Frame(root)

mybutton = tk.Button(frame2, text = "Submit",
                     command = create_canvas)
mybutton.pack()
frame2.pack()

def create_canvas():
    frame3 = tk.Frame(root)
    
    canvas_width = 1200
    canvas_height = 600
    canvas = tk.Canvas(frame3, width = canvas_width, height = canvas_height)
    
    dot_middle_x = canvas_width/4 #1/4th for inputs
    output_middle = dot_middle_x * 3 #3/4ths for outputs
    
    radius = canvas_height/int(input_select.get())/4
        
    input_dot_middle_y = canvas_height/int(input_select.get())/2
    output_dot_middle_y = canvas_height/int(output_select.get())/2
    
    
    for i in range(1, int(input_select.get())*2 + 2, 2):
        canvas.create_oval(dot_middle_x - radius,
                           (input_dot_middle_y *i) - radius,
                           dot_middle_x + radius,
                           (input_dot_middle_y *i) + radius)
    
    for j in range(1, int(output_select.get())*2 + 2, 2):
        canvas.create_oval(output_middle - radius,
                           (output_dot_middle_y *j) - radius,
                           output_middle + radius,
                           (output_dot_middle_y *j) + radius)
    
    canvas.pack()
    frame3.pack()
    delete_Button()
    
def delete_Button():
    frame4 = tk.Frame(root)
    delete_button = tk.Button(frame4, text = "Reset", command = delete_canvas)
    delete_button.pack()
    frame4.pack()
    

root.mainloop()
