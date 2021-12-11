''' This code lets you open a csv file and returns the 
length of the file. That number will be used for 
the number of inputs.

def selected(event):
    if clicked.get() == "CSV File":
        clicked.set('')
        f = fd.askopenfile()
        csv_string = f.read()
        csv_list = csv_string.split(",")
        csv_map_object = map(int, csv_list)
        csv_map = list(csv_map_object)
        tk.Label(frame1, text = len(csv_map)).grid(
            row=3,
            column=9)
        f.close()
        
options = ['CSV File', 'Direct Input']
clicked = tk.StringVar()
clicked.set('')

drop = tk.OptionMenu(root, clicked, *options,
                     command = selected)
drop.pack()

'''
