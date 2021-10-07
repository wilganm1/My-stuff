import tkinter as tk

-Creating the window
  root = tk.Tk()      #creates window
  root.iconbitmap("filename.ico")  #top left image
  root.title("")  #title of the window
  
    #  put code in here

  root.mainloop()   #keeps the window running
  
-Positioning
  .pack()          #Puts the widget in the window in its exact size
  .grid(row = x, column = y, columnspan = z, rowspan = a)

-Label  
  Label1 = tk.Label(root, text = "") #Can use entry.get() as a text

-Button
  Button1 = tk.Button(root, text = "", 
                      command = )
-Entry/Input
  entry1 = tk.Entry(root)
  entry1.get()    #stores what is typed into the entry widget
  entry1.insert(0, "")   #Adds in ghost text that isn't stored in widget
  entry1.delete(0, tk.END)  #tk.END deletes the entire text input
  
-Radio button
 #Radio buttons need a variable tied to them
  r = IntVar()
  r.get()
  rb = tk.Radiobutton(root, text = "", variable = r, value = x)
  
-Message popup
  def popup():
     tk.messagebox.showinfo("Title of box", "The actual message") #Add this to a button as a command
               .showwarning   #yellow triangle ! message
               .showerror     #Red X message
               .askquestion  #Asks to click yes or no
               .asktocancel    #cancel or ok buttons pop up
               .askyesno           
-SpinBox
  sp = tk.Spinbox(root, from_ = x, to = y)  #x is minimum, y is maxium
  
-Browse files
  root.filename = tk.filedialog.askopenfilename(
    initialdir = "",
    title = "",
    filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) #can choose which files to search 
    
    
