----------------------Tkinter GUI-----------------------
Tkinter is a built-in GUI package in python that uses
widgets and events to do stuff.

from tkinter import *
import tkinter as tk
from tkinter import ttk

-Creating the main window.
root = tk.Tk()  
root.title("Title here")  
root.geometry('100x300')  #width and height. X & Y

  ##Code in here

root.mainloop()

.pack()  #puts things in the root. Centers it by default.
.grid(row=x, column = y) #makes a grid.
.place(x= , y = ) #specifies exact coordinates. Not the best


-Positioning. How to put stuff in the root and frames

    padx = ,  #Padding to left and right of widget
    pady = ,  #Padding above and below widget

    ipady =  #internal up/down spacing of widget
    ipadx =  #internal left/right spacing
 
   
   -Pack. Putting stuff in the window. Centered 
     -Fill. Which direction the frames should fill
     
        .pack(fill = 
            tk.X   #fills whole frame horizontally
            tk.Y   #fills frame vertically
            tk.BOTH) #fills entire frame.
   #You don't need width/height with .X/.Y respectively
  #frames will auto-fill when window resized.
  
     -Side. Which side the frame sticks to.
     
        .pack(side =
              tk.LEFT  #left-to-right
              tk.RIGHT #right-to-left
              tk.TOP   #top-down
              tk.BOTTOM)  #bottom-up
        
    
    -Grid. grid layout of multiple widgets.
       .grid(row = x,  #row index. Starts at 0
             column = y, #column index. Starts at 0
             rowspan = , #adjacent rows it takes up
             columnspan = #adjacent columns it take up.
             ) 
           sticky = 'nsew'  #Where it's placed
     #sticky is where in the frame it is.
     #based on cardianl direction. Can combine
         """ (n)orth, (s)outh, (e)ast, (w)est
         ne  -top right corner
         sw  -bottom left corner
         
         ns  -fill in entire vertical section
         ew  -fills horizontal
         """  
        
   -Place. Precise location. Specific placement.
   
      .place(x = a, y = b) #a & b are numbers
     #How far away from the top-left corner it is.
      
      -----------------Widgets------------------ 
These are things that do stuff and create events

    All widgets have common arguments.
    width = x
    height = y
    fg = "color"  #color of text
    bg = "color"  #fill color of background
    bd = ,     #border width. default is two
    borderwidth = x, #how big border is
    relief =  #type of border
        'groove',
        'sunken',
        'ridge',
        'raised',
        'solid',
    justify =     #text alignment. align text.
        'Center',
        'LEFT',
        'RIGHT',

-Frames. Boxes that you can put stuff in. Closed off.

    frame1 = tk.Frame(master = root) #frame inside root
    
     ##code in frame1 here
    
    frame1.pack()  #Actually puts frame in the root
    
    frame2 = tk.Frame(master = frame1) #frame inside frame1
    frame2.pack()

    
 -Label. Adds text to root. Information.
 
    label1 = tk.Label(master, 
                      text='Text here',
                      font = ("font", 12))

 -Spinbox. Choose predetermined values with arrows.
 
     spinbox = tk.Spinbox(
         master,
         values=,  #Can add non-numerical options from a list
         from_ = , #minimum value. Default
         to = ,   #maximum value.
         wrap =) #If true, it cycles back to first or last value
     .get()   #retrives values 

  '''  DO NOT PUT .grid OR .pack() ON THE SAME LINE 
  AS WHEN YOU CREATE THE SPINBOX BECAUSE YOU WILL
  NOT BE ABLE TO RETRIVE ITS VALUE WITH .get() '''

 -Entry. Can type in text to do stuff.
 
   '''OPTIONAL. You can set aside specific variable of 
   types to make it easier for you '''
   
         IntVar()
   var = StringVar() ''' You .get() these values from the entry '''
         DoubleVar()
         BoolVar()
   
    var.get()  #retrieves info put in
    var.set()  #default that shows as text   

    entry = tk.Entry(
        textvariable = var)
    .delete(a,b) #deletes characters a to b-1. Integer values
       .delete(0, tk.END) #deletes all characters
    .insert(a, "text") #inserts 'text' at position a
         
 -Text input. Multiline text entry.
 
    text_box = tk.Text() 
    .get("a.b","c.d") #get indices.
        ('1.0', 'end-1c')  #Get all 
   '''format: start<"line.char">, end <"line.char">
   First argument is the start index, second is end.
    a & c are lines, and b & d are characters
           get(1.4)
          line 1, space 5 (index 4)'''
    .delete('a.b','c.d')   
    
 -Button. Does stuff when clicked on.
 
    button1 = tk.Button(
        master,
        text='',  #What the button says
        command=lambda: xyz) #event holder

  """ lambda holds functions that do stuff when clicked.
  Use lambda to activate button only when it's clicked."""
  
  '''  Having a button insert new things on click 

  Create a button linked to a function that will
  add stuff when function is called. Use .grid to make
  sure things are never duplicated. If you use .pack()
  each time you click the button a new things will 
  appear instead of erasing the old thing '''
    
    def xyz():
        ''' put code in here '''
        tk.Label(root, text = "blah blah blah").grid()
        #You can save this as a function variable.
    
    
 -Binding a function to a key on the keyboard.
 
         def func(event):
             print("You hit return.")
         root/frame.bind('<Return>', func)
         
  ''' To do this you need to know the key address for Tkinter 
  If you want the bind to happen only on a specific widget you
  need to use widget.bind('key', func)
  '''
     
 -Options Menu. Dropdown
 
    menu = tk.OptionMenu(
        master,
        stringvar, #What type of data is in there
        *choices,  #List of choices. * includes all of them
        command = clicked) #Calls a function when clicked
    
    def clicked(event): '''NEED (event)'''
        #code here
    
    
    stringvar = tk.StringVar(root) #option selected
    stringvar.set('') #sets default option
    choices = ['a','b','c','d','e'] #options to select
  
 
 -Messageboxes. Pop up messages. 
 
    Many different forms. Same syntax:
        tk.messagebox.~~~('Title', 'Message displayed')
 
    -showinfo()  -Confirmation/information display
    -showerror() -Error prompt. For mistakes
    -showwarning() -Warning about errors
    
  The next ones ask questions and each reply gives back
  an internal boolean.    

    -askquestion() -'Yes' == True, 'No' == False
    -askokcancel()  'Ok' == True, 'Cancel' == False
    -askyesno()     'Yes' == True, 'No' == False
    -askyesnocancel() 'Cancel' == None.
    -askretrycancel() 'Retry' == True, 'Cancel' == False
 
  To get the value from the ask message boxes, just
  save a variable to them. It will be overwritten 
  when the button is pushed.  
  
 -Check Button. Multiple selection

    ''' Check boxes use StringVar(), etc. 
    Each check box has it's own variable '''
    
    box1 = StringVar()
    box2 = IntVar()
    
    chkbttn1 = tk.Checkbutton(
        master,
        variable = box1)
    chkbttn1.pack()
    
    chkbttn2 = tk.Checkbutton(
        master,
        variable = box 2) 
 
    
 -Radio Button. Single selection option.
     
     '''Each check box has it's own variable '''
 
     Var1 = StringVar()
    
     rad_button1 = tk.Radiobutton(
         master,
         text = ,
         variable = Var1,
         value = )  #value of the specific button
     rad_button.pack()
     
 -Menu Button. Dropdown menu with multiple selections
    
     Menu_button = tk.Menubutton(
         master,
         text )
     
     var1 = IntVar()
     
     Menu1 = Menu(Menu_button, tearoff = 0)
     
     Menu1.add_checkbutton(
         label = "",
         variable = var1)
     
     Menu_button["menu"] = Menu1
 
 -Scrollbar. Scroll down
 
     yscroll = Scrollbar(root) 
     
     myscroll.pack(
         side = RIGHT, #Puts scroll bar on right side
         fill = Y) #brings scrollbar all vertically
     mylist = Listbox(
         root,
         yscrollcommand = myscroll.set)  
           
     myscroll.config(
         command = mylist.yview) 
  
      ------------------CANVAS---------------------
Can draw stuff like shapes and lines.
    
    canvas = tk.Canvas(master, width = x, height = y) #creates canvas
    
    All shapes have color outlines and fills.
        outline = "color name", fill = "color name"    
    
     """ Rectangle """
    canvas.create_rectangle(x1,y1,x2,y2)
       # x1 is top left corner
       # y2 is the bottom right corner
       
     """ Oval """
    canvas.create_oval(x1,y1,x2,y1)
    
     """ Line """
    canvas.create_line(x1,y1,x2,y2,x3,y3,...)
    
     """ Arc """
    canvas.create_arc(x1,y1,x2,y2) 
     
    """ Polygon """
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,...)
    
-------------------TTK Widgets-------------------
 TTK Widgets are extra widgets from the ttk submodule
 of tkinter.
 from tkinter import ttk
 
 -Separator.  Draws a straight line
     
     separator = ttk.Separator(
         master, 
         orient =  #How the line is
             'horizontal',
             'vertical')
    
    
     ------------Updating Widgets------------
    You can dynamically change widgets in Tkinter 
    withouth having to recreate them.
    
    -Configure().  
    
    widget.configure(~~~) #change property of anything
    #to what you want. Like chaning the color.
    
    -After(). Change after certain milliseconds
    
    
