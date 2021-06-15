""" This is how to capitalize each string element in a list""" 

variable = ['habt','aqnu','zjll','gioqng']  #change 'variable' to whatever you want. The words in the list are what you want to capitalize

for i in range(len(variable)):  #Iterates through the words in the list by their index.
    if i.type() == str:    #So you can ignore if there are any non-strings.
        variable[i] = variable[i].capitalize()    #capitalize() automatically captializes the first letter for each string element. So do it for every index.
     #You have to do it this way so it gets saved in the list.
variable
    
   #Testing  
In[134]: variable
Out[134]: ['Habt', 'Aqnu', 'Zjll', 'Gioqng']
