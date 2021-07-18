from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2


"""
Step 3: Color Identification

I want to create a function that will retrive all the 
colors within an image (and return them to me 
in a graphical format).

Or I could make a list and add new colors in when
they appear. A pie graph would probably be best.

54634 colors in ths one picture. No graph 
possible
"""

image = cv2.imread('~~~~.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = np.array(image, dtype = int)
plt.imshow(image)
image

dimensions = image.shape
dimensions
height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]

print('Image Dimension: ',dimensions)
print('Image Height: ',height) #527
print('Image Width: ',width) #210
print('Number of Channels: ',channels)

"""Opencv returns a 3d matrix. But here's the thing:
    Each row has its own array of every pixel.
    
    for example: image[0] is the first row and has a length
    of 221. It has all the pixels of the first row."""


"""Get unique colors in image."""
image

image = np.unique(image.reshape(-1, image.shape[-1]), axis=0, return_counts=True)
unique_list = []
for x in image:
    unique_list.append(x)
unique_list = unique_list[0]
unique_list

len(unique_list)

""" 54634 unique colors in the picture."""


"""This will help show colors on a 
graph. Github:
https://github.com/kb22/Color-Identification-using-Machine-Learning/blob/master/Color%20Identification%20using%20Machine%20Learning.ipynb"
"""
    
