""" Let's say you want to change a tkinter canvas everytime you hit a button or whatever. Here's what you do """

from tkinter import *  #import tkinter. You can import is as tk if you want.

canvas = Canvas(width = ~~, height = ~~)  #Create your canvas widget but don't fill it.

def refresh():  #make a function that will fill in the Canvas.
  canvas.delete("all")   #.delete('all') will make an existing canvas completely clean. It keeps the widget.
  """
  
  Enter canvas stuff here       This is where you add in your actual canvas.
  
  
  """
  canvas.pack()      #This needs to be in the function.
''' Everytime you call the refresh function it will delete the previous canvas and add in the new one. The first time this function is called there is nothing to 
delete, so the canvas will be filled in with whatever is in the funciton. But the next time the function is called is will delete the previous canvas and fill in 
the new one. This happens everytime the function is called. '''  

