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

Step 4: Colorization
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
