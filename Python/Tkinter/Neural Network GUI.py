""" I want to make a GUI that will display how a 
neural network works using circles and lines to 
represent nodes and weights. Also in the future try
to get it to update in real-time during backwards
propagation """

from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry('800x600')  #arbitrary numbers.

canvas = tk.Canvas(master = root)
        
canvas_width = 800
canvas_height = 600


""" Get locations of circles. More circles means
they will get smaller. Need to be same size.

Packing the canvas with .pack() always centers it,
So that makes the math easier. I want the inputs 
on the left-most side and outputs on right-most side.
Right now I will not have any hidden layers. So this 
means that based on pure aesthetics the layers will 
be on the two halves of the screen.

x coordinate of middle of circles always same
middle of left half, so 1/4th of width of canvas

y coordinate is dependent on how many circles there 
are. Will always be number of nodes/2.
    Example: 3 nodes = screen_height/6 """
    
#numb_nodes = .get() from a IntVar
    
radius_x = canvas_width/4
radius_y = canvas_height/(numb_nodes/2) 
#!!! change y according to number of nodes selected 

radius = radius_y/2

#!!! If there were only two circles
""" radius_y = canvas_height/2/2
radius = radius_y/2 == canvas_height/8 """

x1 = radius_x - radius
y1 = radius_y - radius
x2 = radius_x + radius
y2 = radius_y + radius

# !!!!!!!!!!!!!!!!!!!
''' Just realized something. How am I going to 
consistently get the circles in the correct spots
every single time. If I have two cirlces, and 
the middle is 1/4th the screen height, how will that
work with the node at the bottom?????

Solution: Mulitply radius_y by the odd numbers 
of the sections of the screen height.
  Example: 2 nodes == 4 sections. 
      sections = [1,2,3,4]
 I need to multiply the radius_y by the odd numbers
 in the sections list.
  
    1st circle radius_y = 1/4 screen height (1/4 * 1)
    2nd cirlce radius_y = 3/4 screen height (1/4 * 3)
    
    list(range(1,(numb_nodes * 2),2))


for i in list(range(1,(numb_nodes * 2),2)):
    canvas.create_oval(x1, (radius_y * i) - radius, x2, (radius_y * i) + radius)
'''


for i in range(1,4):
    canvas.create_oval(x1, i*y1 + i*y1, x2, (i*y1 + i*y1) + (x2-x1))
canvas.pack(fill = tk.BOTH)



root.mainloop()
