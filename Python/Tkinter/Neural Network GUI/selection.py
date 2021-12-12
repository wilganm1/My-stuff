number_of_inputs = 0
the_inputs = 0
inputs_range = 0
Direct_inputs = 0

frame1 = tk.Frame(root)

inputs_label = tk.Label(frame1,
                        text = "Enter inputs").pack()

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
                global the_inputs
                the_inputs = list(csv_map_object)
    elif clicked.get() == 'Random':
        while 1:
            inputs_range = tk.simpledialog.askinteger(
                "Input range",
                'Enter range of 0 to X.',
                parent = frame1,
                minvalue=1)
            if not isinstance(inputs_range, int):
                tk.messagebox.showerror(
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
                tk.messagebox.showerror(
                    "Error",
                    "Enter integer")
                continue    
            else:
                break
        the_inputs = np.random.uniform(
            0, inputs_range, number_of_inputs+1)
    elif clicked.get() == 'Direct Input':
        openNewWindow(root)

def openNewWindow(master):
    Direct_input_window = Toplevel(master)
    Direct_input_window.title("New Window")
    
    tk.Frame(Direct_input_window).pack(
        padx = 20)
 
    tk.Label(Direct_input_window,
          text ="Numbers only").pack()
    
    Direct_inputs = tk.Text(Direct_input_window,
                            height = 20)
    Direct_inputs.pack()
    
    buttonCommit = tk.Button(Direct_input_window,
                             text = "Commit",
                             command = lambda: [retrieve_input(), Direct_input_window.destroy()])
    buttonCommit.pack()

    
    def retrieve_input():
        global the_inputs
        the_inputs=Direct_inputs.get("1.0","end-1c")
        print(the_inputs)
