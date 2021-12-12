""" I want to make a Neural Network GUI for myself to visually represent how they work.

This will be small scale but I want to incorporate many things like being able to animate it
using the time package, change colors of the canvas, input your own inputs with CSVs or just typing, 
and do complete backwards propagation. """


# !!! Be able to read a csv file and pop up message box



from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry('1200x800')  
root.title("Neural Network GUI")


number_of_inputs = 0
the_inputs = 0
inputs_range = 0
Direct_inputs = 0

number_of_outputs = 0
the_outputs = 0
outputs_range = 0
Direct_outputs = 0

''' Frame 1 with buttons and node selection '''

frame1 = tk.Frame(root)

inputs_label = tk.Label(frame1,
                        text = "Enter inputs").grid(row=0, column = 0)
# -----------------  INPUTS --------------------

def inputselected(event):
    if inputs_clicked.get() == "CSV File":
        while 1:
            f = fd.askopenfile()
            if f is None:
                reply = tk.messagebox.askretrycancel(
                'Error',
                 "Please select a CSV File")
                if reply == True:
                    continue
                else:
                    break 
            else:
                csv_string = f.read()
                csv_list = csv_string.split(",")
                csv_map_object = map(int, csv_list)
                global the_inputs
                the_inputs = list(csv_map_object)
    elif inputs_clicked.get() == 'Random':
        while 1:
            inputs_range = tk.simpledialog.askinteger(
                "Input range",
                'Enter range of 0 to X.',
                parent = frame1,
                minvalue=1)
            if not isinstance(inputs_range, int):
                tk.messagebox.showwarning(
                    "Error",
                    "Enter integer")
                continue  
            else:
                break
        while 1:
            number_of_inputs = tk.simpledialog.askinteger(
                "Input Amount",
                "Enter amouont of inputs",
                parent = frame1,
                minvalue = 1)
            if not isinstance(number_of_inputs, int):
                tk.messagebox.showwarning(
                    "Error",
                    "Enter integer")
                continue    
            else:
                break
        the_inputs = np.random.uniform(
        0, inputs_range, number_of_inputs+1)
    elif inputs_clicked.get() == 'Direct Input':
        inputWindow(root)

def inputWindow(master):
    Direct_input_window = Toplevel(master)
    Direct_input_window.title("New Window")
    
    tk.Frame(Direct_input_window).pack(
        padx = 20)
 
    tk.Label(Direct_input_window,
          text ="Numbers only").pack()
    
    Direct_inputs = tk.Text(Direct_input_window,
                            height = 20)
    Direct_inputs.pack()
    
    inputButtonCommit = tk.Button(Direct_input_window,
                             text = "Commit",
                             command = lambda: [retrieve_input(), Direct_input_window.destroy()])
    inputButtonCommit.pack()

    
    def retrieve_input():
        global the_inputs
        the_inputs=Direct_inputs.get("1.0","end-1c")
        print(the_inputs)
                        

options = ['CSV File', 'Direct Input', 'Random']
inputs_clicked = tk.StringVar()
inputs_clicked.set('')

input_drop = tk.OptionMenu(frame1, inputs_clicked, *options,
                     command = inputselected)
input_drop.grid(row=1, column=0)

#------------------  OUTPUTS  ------------------

outputs_label = tk.Label(frame1,
                        text = "Enter outputs").grid(row=0, column = 1)

def outputselected(event):
    if outputs_clicked.get() == "CSV File":
        while 1:
            f = fd.askopenfile()
            if f is None:
                reply = tk.messagebox.askretrycancel(
                'Error',
                 "Please select a CSV File")
                if reply == True:
                    continue
                else:
                    break 
            else:
                csv_string = f.read()
                csv_list = csv_string.split(",")
                csv_map_object = map(int, csv_list)
                global the_outputs
                the_outputs = list(csv_map_object)
    elif outputs_clicked.get() == 'Random':
        while 1:
            outputs_range = tk.simpledialog.askinteger(
                "Input range",
                'Enter range of 0 to X.',
                parent = frame1,
                minvalue=1)
            if not isinstance(outputs_range, int):
                tk.messagebox.showwarning(
                    "Error",
                    "Enter integer")
                continue  
            else:
                break
        while 1:
            number_of_outputs = tk.simpledialog.askinteger(
                "Input Amount",
                "Enter amouont of outputs",
                parent = frame1,
                minvalue = 1)
            if not isinstance(number_of_outputs, int):
                tk.messagebox.showwarning(
                    "Error",
                    "Enter integer")
                continue    
            else:
                break
        the_outputs = np.random.uniform(
        0, outputs_range, number_of_outputs+1)
    elif outputs_clicked.get() == 'Direct output':
        outputWindow(root)

def outputWindow(master):
    Direct_output_window = Toplevel(master)
    Direct_output_window.title("New Window")
    
    tk.Frame(Direct_output_window).pack(
        padx = 20)
 
    tk.Label(Direct_output_window,
          text ="Numbers only").pack()
    
    Direct_outputs = tk.Text(Direct_output_window,
                            height = 20)
    Direct_outputs.pack()
    
    ouputButtonCommit = tk.Button(Direct_output_window,
                             text = "Commit",
                             command = lambda: [retrieve_output(), Direct_output_window.destroy()])
    outputButtonCommit.pack()

    
    def retrieve_output():
        global the_outputs
        the_outputs=Direct_outputs.get("1.0","end-1c")
        print(the_outputs)
                        

options = ['CSV File', 'Direct output', 'Random']
outputs_clicked = tk.StringVar()
outputs_clicked.set('')

output_drop = tk.OptionMenu(frame1, outputs_clicked, *options,
                     command = outputselected)
output_drop.grid(row = 1, column = 1)


frame1.pack()


''' Frame 2 with button to get the data '''
frame2 = tk.Frame(root)

mybutton = tk.Button(frame2, text = "Submit",
                     command = lambda : create_canvas(int(input_select.get()), int(output_select.get())))
mybutton.pack()
frame2.pack()

''' Function to create the actual neural network '''
def create_canvas(abcd, mnop):
    frame3 = tk.Frame(root)
    
    """
    You will need specific heights and widths for the math to work.
    If you can find a different way feel free to try that 
    """
    
    canvas_width = 1200
    canvas_height = 700
    canvas = tk.Canvas(frame3, width = canvas_width, height = canvas_height)
    
    delete_Button(canvas, frame3)
    
    dot_middle_x = canvas_width/4 #1/4th for inputs
    output_middle = dot_middle_x * 3 #3/4ths for outputs
    
    if abcd >= mnop:
        radius = canvas_height/abcd/2.2
    elif mnop >= abcd:
        radius = canvas_height/mnop/2.2
        
    input_dot_middle_y = canvas_height/abcd/2
    output_dot_middle_y = canvas_height/mnop/2
    
    """ Creating the circles """
    for i in range(1, abcd*2 + 2, 2):
        canvas.create_oval(dot_middle_x - radius,
                           (input_dot_middle_y *i) - radius,
                           dot_middle_x + radius,
                           (input_dot_middle_y *i) + radius)
        #oval  #Set this equal to the canvas
    
    for j in range(1, mnop*2 + 2, 2):
        canvas.create_oval(output_middle - radius,
                           (output_dot_middle_y *j) - radius,
                           output_middle + radius,
                           (output_dot_middle_y *j) + radius)
        
    """ Creating lines """
    for aa in range(1, abcd*2, 2):
        for bb in range(1, mnop*2, 2):
            canvas.create_line(dot_middle_x + radius, #x2 of inputs
                               input_dot_middle_y*aa, #middle of inputs
                               output_middle - radius, #x1 of outputs
                               output_dot_middle_y*bb,
                               fill = "red") #middle of outputs      
    canvas.pack()
    frame3.pack()

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
