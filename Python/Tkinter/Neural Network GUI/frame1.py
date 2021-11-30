import tkinter as tk
from tkinter import *

root = tk.Tk()

nodes_label = tk.Label(root, text='Select number of nodes')
nodes_label.grid(row = 0, column = 1)


nodes_entry1 = tk.Entry(width = 3) #entry widget

nodes_entry2 = Spinbox(master, from_=0, to=10)  #change 10 to infinity
nodes_entry2.grid(row = 1,column = 1

#Or instead of a spinbox have it be an entry that checks if it's
#greater than zero and can be converted to integer.

root.mainloop()
