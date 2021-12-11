number_of_inputs = 0
the_inputs = 0
inputs_range = 0

frame1 = tk.Frame(root)

def selected(event):
    if clicked.get() == "CSV File":
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
                csv_map = list(csv_map_object)
    elif clicked.get() == 'Random':
        global inputs_range
        inputs_range = tk.simpledialog.askinteger(
            "Input range",
            'Enter range of 0 to X.',
            parent = frame1,
            minvalue=1)
        global number_of_inputs
        number_of_inputs = tk.simpledialog.askinteger(
            "Input Amount",
            "Enter amouont of inputs",
            parent = frame1,
            minvalue = 1)
        global inputs
        the_inputs = np.random.uniform(
            0, inputs_range, number_of_inputs+1)
        
        
options = ['CSV File', 'Direct Input', 'Random']
clicked = tk.StringVar()
clicked.set('')

drop = tk.OptionMenu(root, clicked, *options,
                     command = selected)
drop.pack()

frame1.pack()
