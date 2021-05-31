import tkinter as tk

frame2 = tk.Tk()

""" I might need to make 6 separate rows instead 
of one giant grid. This way I can change each row
indiviudually. """


""" 1st string """

for i in range(0, 1):  #strings. Rows.
    for j in range(1, 14):  #frets. Columns
        frame2.columnconfigure(j, weight=1)
        frame2.rowconfigure(j, weight=1)
        frame = tk.Frame(     
        master=frame2,
        relief=tk.RAISED,
        borderwidth=1
        )

        frame.grid(row=i, column=j, padx=2, pady=2)
        label = tk.Label(master=frame)
        label.pack(padx=2, pady=2) 
 
""" 2nd string """
 
for i in range(1, 2):  #strings. Rows.
   for j in range(1, 14):  #frets. Columns
       frame2.columnconfigure(j, weight=1)
       frame2.rowconfigure(j, weight=1)
       frame = tk.Frame(     
       master=frame2,
       relief=tk.RAISED,
       borderwidth=1
       )

       frame.grid(row=i, column=j, padx=2, pady=2)
       label = tk.Label(master=frame)
       label.pack(padx=2, pady=2) 
   
""" 3rd string """
for i in range(2, 3):  #strings. Rows.
   for j in range(1, 14):  #frets. Columns
       frame2.columnconfigure(j, weight=1)
       frame2.rowconfigure(j, weight=1)
       frame = tk.Frame(     
       master=frame2,
       relief=tk.RAISED,
       borderwidth=1
       )

       frame.grid(row=i, column=j, padx=2, pady=2)
       label = tk.Label(master=frame)
       label.pack(padx=2, pady=2) 

    
""" 4th string """

for i in range(3, 4):  #strings. Rows.
   for j in range(1, 14):  #frets. Columns
       frame2.columnconfigure(j, weight=1)
       frame2.rowconfigure(j, weight=1)
       frame = tk.Frame(     
       master=frame2,
       relief=tk.RAISED,
       borderwidth=1
       )

       frame.grid(row=i, column=j, padx=2, pady=2)
       label = tk.Label(master=frame)
       label.pack(padx=2, pady=2) 

""" 5th string """

for i in range(4, 5):  #strings. Rows.
   for j in range(1, 14):  #frets. Columns
       frame2.columnconfigure(j, weight=1)
       frame2.rowconfigure(j, weight=1)
       frame = tk.Frame(     
       master=frame2,
       relief=tk.RAISED,
       borderwidth=1
       )

       frame.grid(row=i, column=j, padx=2, pady=2)
       label = tk.Label(master=frame)
       label.pack(padx=2, pady=2) 


""" 6th string """
for i in range(5, 6):  #strings. Rows.
   for j in range(1, 14):  #frets. Columns
       frame2.columnconfigure(j, weight=1)
       frame2.rowconfigure(j, weight=1)
       frame = tk.Frame(     
       master=frame2,
       relief=tk.RAISED,
       borderwidth=1
       )

       frame.grid(row=i, column=j, padx=2, pady=2)
       label = tk.Label(master=frame)
       label.pack(padx=2, pady=2) 

""" Fret row """
for m in range(6,7):    #This is a separate row for the frets. It won't change
    for n in range(1,14):
        frame2.columnconfigure(n, weight = 1)
        frame2.rowconfigure(n, weight = 1)
        frame = tk.Frame(     
        master=frame2,
        relief=tk.RAISED,
        borderwidth=1
        )

        frame.grid(row=m, column=n, padx=5, pady=5)
        label = tk.Label(master=frame, text=str(n-1))
        label.pack(padx=2, pady=2) 


''' Now add column 0 for the tuning ''' 

for y in range(0, 6):    #This is a separate row for the frets. It won't change
    frame2.columnconfigure(y, weight = 1)
    frame2.rowconfigure(y, weight = 1)
    frame = tk.Frame(     
    master=frame2,
    relief=tk.RAISED,
    borderwidth=1
    )

    frame.grid(row=y, column=0, padx=5, pady=5)
    label = tk.Label(master=frame)
    label.pack(padx=2, pady=2) 

frame8 = tk.Frame(
    master=frame2,
    relief=tk.RAISED,
    borderwidth=1)


    
frame2.mainloop()
