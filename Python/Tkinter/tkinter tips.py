import tkinter as tk
from tkinter import *

-Creating the window
  root = tk.Tk()      #creates window
   .geometry('numb1xnumb2')
   .iconbitmap("filename.ico")  #top left image
   .title("")  #title of the window
  
    #  put code in here

  root.mainloop()   #keeps the window running
  
-Positioning
  
  .pack()          #Puts the widget in the window in its exact size
  .grid(row = x, column = y, columnspan = z, rowspan = a)
  root.rowconfigure(n, minsize = x)    #n is which row
  root.columnconfigure([a,b,c], maxsize = y)  #you can have a list of columns/rows.

-Frames
  frame1 = tk.Frame(
    .width = x    #width of frame
    .height = y)  #height of frame
  
 #You can put things inside the frame by setting master option equal to frame
  Labelx = tk.Label(frame1, text = "")
  
-Label  
  Label1 = tk.Label(root, text = "") #Can use entry.get() as a text

-Button
  Button1 = tk.Button(root, text = "")
      command = buttonfunction  #Has the button do something when clicked
      state = DISABLED    #Grays out and disables the button

   #  Having the button do something. Make a function
     def buttonfunction():
        aLabel = tk.Label(root, text="do stuff")
        aLabel.pack()
  
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
  
-Checkboxes
 #Need variables to tied to them
  v = IntVar()
  
  c = Checkbutton(root, text = "", variable = v)
                 onvalue   #default value when box is checked
                 offvalue    #default when box is unchecked
  c.deselect()          #box is unchecked  by default

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
  
-Dropdown menu
  clicked = tk.StringVar()      #change to IntVar() if using numbers
  clicked.set()             #default option
  
  drop = tk.OptionMenu(root, clicked, "option1", "option2")
  drop.pack()
  
-Browse files
  root.filename = tk.filedialog.askopenfilename(
    initialdir = "",
    title = "",
    filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) #can choose which files to search 
    
-Menu
  menubar = tk.Menu(root)
  file = Menu(menubar, tearoff = 0)
  menubar.add_cascade(label ='', menu = file)  #parent menu 
  file.add_command(label ='', command = None)  #menu item
  file.add_separator()   #adds horizontal line in menu
  file.add_command(label ='', command = root.destroy)  #destorys the menu and selection
      
  # display Menu
  root.config(menu = menubar)
  
    
