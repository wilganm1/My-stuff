""" Let's say you want to change a tkinter canvas everytime you hit a button or whatever. Here's what you do """

from tkinter import *

canvas = Canvas(width = ~~, height = ~~)  #Create your canvas widget but don't fill it.

def refresh():
  canvas.delete("all")   #This will make the canvas completely clean. It will be invisible. It keeps the widget.
  """
  
  Enter canvas stuff here
  
  
  """
  
''' Everytime you call the refresh function it will delete the previous canvas and add in the new one everytime. '''  

