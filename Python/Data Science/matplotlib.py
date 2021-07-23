""" Matplotlib """  
'https://matplotlib.org/stable/api/pyplot_summary.html'
'https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot'
import matplotlib.pyplot as plt

        """ Making a basic line plot """
x = [1,2,3]  #list of numbers for x-axis
y = [1,4,9]  #a list of numbers for y-axis
z = [10, 5, 0]   #a different list of numbers for y-axis
plt.plot(x-axis, y-axis, #structure of plot
         color =,  #dot color. g = green, b = blue, etc
         marker =,  #what shape the points are.
             o,         #circles marks
             --,        #dashes
             +,         #plusses
             s,         #squares
             ^          #traingles
         linestyle =,  #the style of the line
         linewidth =,  #width of line
         markersize =) #size of markers
 plt.plot(x,y, 'colorMarker') #color & marker in one.
plt.plot(x,z)   #plots x on x-axis, z on y-axis

#plot multiple data sets at once.
plt.plot(x1, y1, 'g^', x2, y2, 'r--')

#Labels of the graph
plt.title("title")  #adds title
plt.xlabel('x')   #x-axis label
plt.ylabel('y and z')   #y-axis label
plt.legend(["this is y", "this is z"]) #adds legend. Will auto bind to correct color
plt.show()   #shows the actual graph
#You can plot multiple combinations on the same graph

#Different types of plots. plt
.hist(data)   #histogram
.scatter(data)  #scatter plot
.boxplot(data)      #box and whisker plot
.pie(data)      #pie chart
.specgram(data)      #spectrogram
.stackplot(data)   #stacked area plot

#Change axis tiltles, numbers
plt.axis([x1, x2, y1, y2])  #number range of axes
plt.xticks(("current numbers"), ('replacement')) #replace x-axis numbers with anything
plt.yticks(("current numbers"), ('replacement')) #replace x-axis numbers with anything


#Make a heatmap. color-coded 2D display
import matplotlib.pyplot.colormaps()

imshow(data, cmap =  #how to show it
       inferno,    #black-red-yellow
       magma,      #black-red-white
       plasma,     #blue-red-yellow
       viridis,    #blue-green-yellow
       brg,        #blue-red-green
       hot,        #black-red-yellow-white
       bone,       #black-white w/ blue tinge. x-ray
       gray)       #gray-scale
       
