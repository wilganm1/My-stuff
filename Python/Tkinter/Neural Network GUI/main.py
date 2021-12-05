""" I want to make a Neural Network GUI for myself to visually represent how they work.

This will be small scale but I want to incorporate many things like being able to animate it
using the time package, change colors of the canvas, input your own inputs with CSVs or just typing, 
and do complete backwards propagation. """


from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry('1200x800')  

''' Frame 1 with buttons and node selection '''

frame1 = tk.Frame(root)

# Input layer
input_label = tk.Label(frame1, text = "Select number of inputs").grid(row=0, column = 0)

input_select = tk.Spinbox(frame1, from_ = 2, to = 20, width = 3, wrap = True) # Input Spinbox. 2 is always minimum
input_select.grid(row = 1, column = 0) 

# Output layer
output_label = tk.Label(frame1, text = "Select number of outputs").grid(row=0, column = 2)

output_select = tk.Spinbox(frame1, from_ = 1, to = 19, width = 3, wrap = True)
output_select.grid(row = 1, column = 2)                                                             

frame1.pack()

''' Frame 2 with button to get the data '''
frame2 = tk.Frame(root)

mybutton = tk.Button(frame2, text = "Submit",
                     command = lambda : create_canvas(input_select.get(), output_select.get()))
mybutton.pack()
frame2.pack()

''' Function to create the actual neural network '''
def create_canvas(abc, nop):
    frame3 = tk.Frame(root)
    
    """
    You will need specific heights and widths for the math to work.
    If you can find a different way feel free to try that 
    """
    
    canvas_width = 1200
    canvas_height = 600
    canvas = tk.Canvas(frame3, width = canvas_width, height = canvas_height)
    
    dot_middle_x = canvas_width/4 #1/4th for inputs
    output_middle = dot_middle_x * 3 #3/4ths for outputs
    
    if abc > nop:
        radius = canvas_height/int(abc)/4
    else:
        radius = canvas_height/int(nop)/4
        
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
    delete_Button(canvas, frame3)

    
def delete_Button(zzz,yyy):
    frame4 = tk.Frame(root)
    delete_button = tk.Button(frame4, text = "Reset", command = lambda : delete_canvas(zzz, yyy, delete_button, frame4))
    delete_button.pack()
    frame4.pack()
    
def delete_canvas(zzz, yyy, xxx, aaa):
    zzz.destroy()
    yyy.destroy()
    xxx.pack_forget()
    aaa.destroy()
    

root.mainloop()
