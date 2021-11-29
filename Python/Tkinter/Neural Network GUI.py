diameter = x   #How big will the circles be?

for i in range(x,y):  #x = 1 and y = number of nodes wanted
  canvas.create_oval(10, i*20 + i*50, 60, (i*20 + i*50)+ 60)
    #                       m      n   the m and n added must be >= x2-x1 to create a space
    
    
   """ Lines """
  #Need to know the y coordinate of x2. If it's a perfect circle its
  #just the radius (diameter/2) from y1.
