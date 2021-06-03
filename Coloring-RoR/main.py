"""
I want to write a python program that 
will color manga panels of 
Record of Ragnarok. I want to color in
the manga panels with the official colors
of the characters. I might need to use
machine learning to learn what the characters look like.

Watch this YouTube video for help:
    https://www.youtube.com/watch?v=9RN2Wr8xvro
    
    
Step 1: Image collection
    Get multiple pictures of the characters from various angles. 
    Erase everything that's not them. Try to only have 
    them in the picture so it will as accurate as possible.
    
                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        If you use Krita UNCHECK 'store alpha channel'.
         -This is so what you erase will be white.
    

Step 2: Reading the images.
    Scan through the images and get the gray-scale
values of every single pixel in every single image.
Write it as a matrix in numpy.


!!!!!!!
Step 3: Color Identification
    Find pictures with the official manga/anime colors.
Manga colors are default. If a character isn't colored yet
in the manga, use anime colors. Get all the colors for each
character.

Step 4: Image Labeling
    Use a labeling system like LabelImg or YOLOv4
to identify each character and label them. This will 
help train a neural network to identify the character.

Step 5: Colorization
    Set up a learning algorithm based on your
annotated images that will automatically recognize
characters and color them in based on 
the color references.    
    
So I want to identify each character using 
python.This means that each character has a
label, which is their name. I have to choose
which vector identifies which character.

This will start off a classification problem.
For now get the pixels.
"""
pixels = []
import cv2
img = cv2.imread('C:/Users/WilganZMT/Documents/Coding/Python/Coloring RoR/Jack the Ripper/Jack_t-posing.png', 0)
for i in range(img.shape[0]): #height
    for j in range(img.shape[1]): #width
        pixels.append(img[i][j])
len(pixels)
gray_scale = []   #gray_scale values
for pixel in pixels:
    gray_scale.append(pixel/255)

gray_scale
len(gray_scale) #1640
"""
So I now have all my gray scale pixels.
Now to add all the values into a neural network.
The pixels go from left to right, then down
a row.

For the network, the input layer will have 
340319 nodes, the output will have 2, one being
the vector [1,0] for 'Yes', and the other being 
the vector [0,1] for 'No'. The hidden layer 
will have 820 nodes. 
"""
import numpy as np
import random
"""Input layer. 1640 nodes"""

1640/2 # 820

inputs = []
for m in gray_scale:
    inputs.append(m) 
biases1 = []
for n in range(0,820):
    biases1.append(1)
len(biases1)

""" For each input node, I need 1640 weights.
But I need as many lists of weights as there are
hidden layer nodes. That is 820.

So I need 820 lists of weights

That's 1344800 weights"""
nodes = len(inputs)
hidden_nodes = []
weights = {}
#loop through every input for each node. Generate random weights for each node.
m = 0
while m < 820:
    weights[str(m)] = []    
    for node in range(nodes):
        weights[str(m)].append(random.uniform(-1,1))
    m += 1      
for x in weights:
    hidden_nodes.append(weights[str(x)])

len(hidden_nodes)
len(hidden_nodes[0])

"""I now have everything I need. Now just do
dot product and add biases. Use HIDDEN_NODES for the weights"""

hidden_output = np.dot(hidden_nodes, inputs) + biases1

len(hidden_output)


""" Now get the output layer. 2 nodes will be in it."""
weights2 = {}
biases2 = [1,1]

final_outputs = []
uy = 0
while uy < 2:
    weights2[str(uy)] = []    
    for n in range(len(hidden_output)):
        weights2[str(uy)].append(random.uniform(-1,1))
    uy += 1      
for bn in weights2:
    final_outputs.append(weights2[str(bn)])
    
len(final_outputs)
final_outputs

final = np.dot(final_outputs, hidden_output) + biases2

final
